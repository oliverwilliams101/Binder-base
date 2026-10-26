from __future__ import annotations

import hashlib
import hmac
import os
import secrets
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Annotated, Optional

from fastapi import Cookie, Depends, FastAPI, HTTPException, Response, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import EmailStr, Field as PydanticField
from sqlalchemy.exc import IntegrityError
from sqlmodel import Field, Session as DbSession, SQLModel, create_engine, select


DATABASE_URL = f"sqlite:///{Path(__file__).resolve().parent / 'binderbase.db'}"
SESSION_COOKIE = "binderbase_session"
SESSION_LIFETIME = timedelta(days=7)
PASSWORD_HASH_ITERATIONS = 600_000
COOKIE_SECURE = os.getenv("BINDERBASE_COOKIE_SECURE", "false").lower() == "true"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True, max_length=320)
    password_hash: str = Field(max_length=256)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None))


class AuthSession(SQLModel, table=True):
    token_digest: str = Field(primary_key=True, max_length=64)
    user_id: int = Field(foreign_key="user.id", index=True)
    expires_at: datetime


class Credentials(SQLModel):
    email: EmailStr
    password: str = PydanticField(min_length=8, max_length=128)


class UserResponse(SQLModel):
    id: int
    email: str


class AuthResponse(SQLModel):
    user: UserResponse


class LogoutResponse(SQLModel):
    ok: bool


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


create_db_and_tables()

app = FastAPI(title="BinderBase API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


def get_db_session():
    with DbSession(engine) as session:
        yield session


def hash_password(password: str, salt: Optional[bytes] = None) -> str:
    salt = salt or secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        PASSWORD_HASH_ITERATIONS,
    )
    return f"pbkdf2_sha256${PASSWORD_HASH_ITERATIONS}${salt.hex()}${digest.hex()}"


def verify_password(password: str, stored_hash: str) -> bool:
    try:
        algorithm, iterations, salt_hex, digest_hex = stored_hash.split("$", 3)
        if algorithm != "pbkdf2_sha256":
            return False
        candidate = hash_password(password, bytes.fromhex(salt_hex)).split("$", 3)[3]
        return hmac.compare_digest(candidate, digest_hex) and int(iterations) == PASSWORD_HASH_ITERATIONS
    except (TypeError, ValueError):
        return False


def digest_session_token(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def set_session_cookie(response: Response, token: str) -> None:
    response.set_cookie(
        key=SESSION_COOKIE,
        value=token,
        max_age=int(SESSION_LIFETIME.total_seconds()),
        httponly=True,
        secure=COOKIE_SECURE,
        samesite="lax",
        path="/",
    )


def clear_session_cookie(response: Response) -> None:
    response.delete_cookie(
        key=SESSION_COOKIE,
        httponly=True,
        secure=COOKIE_SECURE,
        samesite="lax",
        path="/",
    )


def public_user(user: User) -> UserResponse:
    return UserResponse(id=user.id, email=user.email)


def get_current_user(
    session_token: Annotated[Optional[str], Cookie(alias=SESSION_COOKIE)] = None,
    db: DbSession = Depends(get_db_session),
) -> User:
    if not session_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Sign in to continue.")

    now = datetime.now(timezone.utc).replace(tzinfo=None)
    auth_session = db.get(AuthSession, digest_session_token(session_token))
    if not auth_session or auth_session.expires_at <= now:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Your session has expired. Sign in again.")

    user = db.get(User, auth_session.user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Sign in to continue.")
    return user


@app.get("/api/auth/me", response_model=AuthResponse)
def read_current_user(current_user: User = Depends(get_current_user)):
    return AuthResponse(user=public_user(current_user))


@app.post("/api/auth/register", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
def register(credentials: Credentials, db: DbSession = Depends(get_db_session)):
    normalized_email = str(credentials.email).strip().casefold()
    existing_user = db.exec(select(User).where(User.email == normalized_email)).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="An account with this email already exists.")

    user = User(email=normalized_email, password_hash=hash_password(credentials.password))
    db.add(user)
    try:
        db.commit()
    except IntegrityError as error:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An account with this email already exists.",
        ) from error
    db.refresh(user)
    return AuthResponse(user=public_user(user))


@app.post("/api/auth/login", response_model=AuthResponse)
def login(credentials: Credentials, response: Response, db: DbSession = Depends(get_db_session)):
    normalized_email = str(credentials.email).strip().casefold()
    user = db.exec(select(User).where(User.email == normalized_email)).first()
    if not user or not verify_password(credentials.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email or password is incorrect.")

    token = secrets.token_urlsafe(32)
    auth_session = AuthSession(
        token_digest=digest_session_token(token),
        user_id=user.id,
        expires_at=datetime.now(timezone.utc).replace(tzinfo=None) + SESSION_LIFETIME,
    )
    db.add(auth_session)
    db.commit()
    set_session_cookie(response, token)
    return AuthResponse(user=public_user(user))


@app.post("/api/auth/logout", response_model=LogoutResponse)
def logout(
    response: Response,
    session_token: Annotated[Optional[str], Cookie(alias=SESSION_COOKIE)] = None,
    db: DbSession = Depends(get_db_session),
):
    if session_token:
        auth_session = db.get(AuthSession, digest_session_token(session_token))
        if auth_session:
            db.delete(auth_session)
            db.commit()
    clear_session_cookie(response)
    return LogoutResponse(ok=True)


@app.get("/")
def read_root():
    return {"message": "BinderBase API"}

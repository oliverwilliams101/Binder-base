# BinderBase API

The authentication API uses FastAPI, SQLModel, and SQLite. From the repository root, install the server requirements and start the API:

```sh
server/.venv/bin/pip install -r server/requirements.txt
cd server
.venv/bin/uvicorn main:app --reload
```

The Vue development server proxies `/api` requests to `http://127.0.0.1:8000`.

Authentication endpoints return JSON:

- `POST /api/auth/register` creates an account and returns its public user record.
- `POST /api/auth/login` validates credentials, returns the public user record, and sets an HTTP-only session cookie.
- `GET /api/auth/me` returns the signed-in user associated with the session cookie.
- `POST /api/auth/logout` revokes the session and clears the cookie.

The SQLite database is created at `server/binderbase.db`. Set `BINDERBASE_COOKIE_SECURE=true` when serving the API over HTTPS.

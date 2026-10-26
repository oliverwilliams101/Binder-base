import { computed, readonly, ref } from 'vue';

const user = ref(null);
const initialized = ref(false);
let initializePromise;

async function request(path, options = {}) {
  const response = await fetch(`/api${path}`, {
    credentials: 'include',
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...options.headers
    }
  });
  const body = await response.json().catch(() => ({}));
  if (!response.ok) {
    const detail = typeof body.detail === 'string' ? body.detail : 'The request could not be completed.';
    throw new Error(detail);
  }
  return body;
}

async function initializeAuth() {
  if (initialized.value) return;
  initializePromise ??= (async () => {
    try {
      const response = await request('/auth/me');
      user.value = response.user;
    } catch {
      user.value = null;
    } finally {
      initialized.value = true;
    }
  })();
  await initializePromise;
}

async function register(credentials) {
  return request('/auth/register', {
    method: 'POST',
    body: JSON.stringify(credentials)
  });
}

async function login(credentials) {
  const response = await request('/auth/login', {
    method: 'POST',
    body: JSON.stringify(credentials)
  });
  user.value = response.user;
  initialized.value = true;
  return response.user;
}

async function logout() {
  await request('/auth/logout', { method: 'POST' });
  user.value = null;
  initialized.value = true;
}

export function useAuth() {
  return {
    user: readonly(user),
    isAuthenticated: computed(() => user.value !== null),
    initializeAuth,
    register,
    login,
    logout
  };
}

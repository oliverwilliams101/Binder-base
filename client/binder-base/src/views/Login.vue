<script setup>
import { computed, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useAuth } from '../services/auth';

const route = useRoute();
const router = useRouter();
const { login } = useAuth();
const username = ref('');
const password = ref('');
const errorMessage = ref('');
const isSubmitting = ref(false);
const registrationComplete = computed(() => route.query.registered === '1');

async function submitLogin() {
  errorMessage.value = '';
  isSubmitting.value = true;
  try {
    await login({ username: username.value, password: password.value });
    await router.replace('/dashboard');
  } catch (error) {
    errorMessage.value = error.message;
  } finally {
    isSubmitting.value = false;
  }
}
</script>

<template>
  <main class="auth-shell">
    <h1>Login</h1>
    <p>Sign in to open your dashboard.</p>
    <p v-if="registrationComplete" class="auth-success" role="status">Account created. Sign in to continue.</p>
    <form class="auth-form" @submit.prevent="submitLogin">
      <label for="login-username">Username</label>
      <input
        id="login-username"
        v-model.trim="username"
        type="text"
        name="username"
        autocomplete="username"
        maxlength="32"
        required
      />
      <label for="login-password">Password</label>
      <input
        id="login-password"
        v-model="password"
        type="password"
        name="password"
        autocomplete="current-password"
        minlength="8"
        maxlength="128"
        required
      />
      <button class="auth-submit" type="submit" :disabled="isSubmitting">
        {{ isSubmitting ? 'Signing in…' : 'Sign in' }}
      </button>
      <p v-if="errorMessage" class="auth-error" role="alert">{{ errorMessage }}</p>
    </form>
    <div class="auth-links">
      <RouterLink to="/register">Create an account</RouterLink>
      <RouterLink to="/">Return Home</RouterLink>
    </div>
  </main>
</template>

<style scoped>
.auth-shell { max-width: 480px; margin: 0 auto; padding: 40px 24px; color: var(--text); }
.auth-shell > p { color: var(--muted); }
.auth-form { display: grid; gap: 9px; margin-top: 24px; }
.auth-form label { font-size: 13px; font-weight: 700; }
.auth-form input { min-height: 44px; padding: 0 12px; border: 1px solid var(--border); border-radius: 8px; color: var(--text); background: var(--surface); font: inherit; }
.auth-submit { min-height: 44px; margin-top: 8px; border: 0; border-radius: 8px; color: var(--accent-ink); background: var(--accent); font: inherit; font-weight: 700; cursor: pointer; }
.auth-submit:disabled { opacity: .7; cursor: wait; }
.auth-error { margin: 3px 0 0; color: #b42318; font-size: 13px; }
.auth-success { color: var(--accent) !important; }
.auth-links { display: flex; flex-wrap: wrap; gap: 18px; margin-top: 20px; font-size: 13px; }
.auth-links a { color: var(--accent); }
</style>

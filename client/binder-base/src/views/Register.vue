<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuth } from '../services/auth';

const router = useRouter();
const { register } = useAuth();
const email = ref('');
const password = ref('');
const confirmPassword = ref('');
const errorMessage = ref('');
const isSubmitting = ref(false);

async function submitRegistration() {
  errorMessage.value = '';
  if (password.value !== confirmPassword.value) {
    errorMessage.value = 'Passwords do not match.';
    return;
  }

  isSubmitting.value = true;
  try {
    await register({ email: email.value, password: password.value });
    await router.replace({ path: '/login', query: { registered: '1' } });
  } catch (error) {
    errorMessage.value = error.message;
  } finally {
    isSubmitting.value = false;
  }
}
</script>

<template>
  <main class="auth-shell">
    <h1>Register</h1>
    <p>Create an account to access your dashboard.</p>
    <form class="auth-form" @submit.prevent="submitRegistration">
      <label for="register-email">Email</label>
      <input
        id="register-email"
        v-model="email"
        type="email"
        name="email"
        autocomplete="email"
        required
      />
      <label for="register-password">Password</label>
      <input
        id="register-password"
        v-model="password"
        type="password"
        name="password"
        autocomplete="new-password"
        minlength="8"
        maxlength="128"
        required
      />
      <label for="confirm-password">Confirm password</label>
      <input
        id="confirm-password"
        v-model="confirmPassword"
        type="password"
        name="confirm-password"
        autocomplete="new-password"
        minlength="8"
        maxlength="128"
        required
      />
      <button class="auth-submit" type="submit" :disabled="isSubmitting">
        {{ isSubmitting ? 'Creating account…' : 'Create account' }}
      </button>
      <p v-if="errorMessage" class="auth-error" role="alert">{{ errorMessage }}</p>
    </form>
    <div class="auth-links">
      <RouterLink to="/login">Already registered? Login</RouterLink>
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
.auth-links { display: flex; flex-wrap: wrap; gap: 18px; margin-top: 20px; font-size: 13px; }
.auth-links a { color: var(--accent); }
</style>

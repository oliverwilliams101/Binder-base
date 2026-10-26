<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import BrandEmblem from './BrandEmblem.vue';
import { useAuth } from '../services/auth';

const router = useRouter();
const { isAuthenticated, logout } = useAuth();
const logoutError = ref('');

async function signOut() {
  logoutError.value = '';
  try {
    await logout();
    await router.replace('/');
  } catch (error) {
    logoutError.value = error.message;
  }
}
</script>

<template>
  <nav class="main-nav" aria-label="Main navigation">
    <RouterLink to="/" class="brand-link">
      <BrandEmblem />
      <span>BinderBase</span>
    </RouterLink>
    <div class="nav-links">
      <RouterLink to="/">Home</RouterLink>
      <RouterLink v-if="isAuthenticated" to="/dashboard">Dashboard</RouterLink>
      <RouterLink to="/binders">My Binders</RouterLink>
      <RouterLink to="/cards">Explore Cards</RouterLink>
      <template v-if="isAuthenticated">
        <button class="nav-logout" type="button" @click="signOut">Logout</button>
      </template>
      <template v-else>
        <RouterLink to="/login">Login</RouterLink>
        <RouterLink to="/register">Register</RouterLink>
      </template>
    </div>
    <p v-if="logoutError" class="nav-error" role="alert">{{ logoutError }}</p>
  </nav>
</template>

<style scoped>
.main-nav { display: flex; align-items: center; gap: 30px; }
.brand-link { display: flex; align-items: center; gap: 9px; color: var(--accent); font-size: 16px; font-weight: 700; text-decoration: none; }
.nav-links { display: flex; flex-wrap: wrap; gap: 7px; }
.nav-links a { padding: 8px 10px; border-radius: 6px; color: var(--muted); font-size: 13px; text-decoration: none; }
.nav-links a:hover, .nav-links a.router-link-active { color: var(--accent); background: var(--accent-soft); }
.nav-logout { padding: 8px 10px; border: 0; border-radius: 6px; color: var(--muted); background: transparent; font: inherit; font-size: 13px; cursor: pointer; }
.nav-logout:hover { color: var(--accent); background: var(--accent-soft); }
.nav-error { margin: 0; color: #b42318; font-size: 12px; }

@media (max-width: 620px) {
  .main-nav { width: 100%; align-items: flex-start; flex-direction: column; gap: 8px; }
  .nav-links { width: 100%; }
}
</style>

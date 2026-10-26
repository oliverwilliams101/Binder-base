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
    <div class="nav-main">
      <div class="nav-primary">
        <RouterLink to="/" class="brand-link">
          <BrandEmblem />
          <span>BinderBase</span>
        </RouterLink>
        <div class="nav-links">
          <RouterLink to="/">Home</RouterLink>
          <RouterLink v-if="isAuthenticated" to="/dashboard">Dashboard</RouterLink>
          <RouterLink to="/binders">My Binders</RouterLink>
          <RouterLink to="/cards">Explore Cards</RouterLink>
        </div>
      </div>
      <div class="nav-account-links">
        <template v-if="isAuthenticated">
          <button class="nav-logout" type="button" @click="signOut">Logout</button>
        </template>
        <template v-else>
          <RouterLink to="/login">Login</RouterLink>
          <RouterLink to="/register">Register</RouterLink>
        </template>
        <p v-if="logoutError" class="nav-error" role="alert">{{ logoutError }}</p>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.main-nav { display: flex; flex: 1 1 auto; align-items: center; min-width: 0; }
.nav-main { display: flex; width: 100%; align-items: center; justify-content: space-between; gap: 12px; }
.nav-primary { display: flex; min-width: 0; align-items: center; gap: 30px; }
.brand-link { display: flex; align-items: center; gap: 9px; color: var(--accent); font-size: 16px; font-weight: 700; text-decoration: none; }
.nav-links { display: flex; flex-wrap: wrap; gap: 7px; }
.nav-links a { padding: 8px 10px; border-radius: 6px; color: var(--muted); font-size: 13px; text-decoration: none; }
.nav-links a:hover, .nav-links a.router-link-active { color: var(--accent); background: var(--accent-soft); }
.nav-account-links { display: flex; flex: 0 0 auto; align-items: center; gap: 7px; }
.nav-account-links a { padding: 8px 10px; border-radius: 6px; color: var(--muted); font-size: 13px; text-decoration: none; }
.nav-account-links a:hover, .nav-account-links a.router-link-active { color: var(--accent); background: var(--accent-soft); }
.nav-logout { padding: 8px 10px; border: 0; border-radius: 6px; color: var(--muted); background: transparent; font: inherit; font-size: 13px; cursor: pointer; }
.nav-logout:hover { color: var(--accent); background: var(--accent-soft); }
.nav-error { margin: 0; color: #b42318; font-size: 12px; }

@media (max-width: 620px) {
  .main-nav { width: 100%; }
  .nav-main { align-items: flex-start; }
  .nav-primary { align-items: flex-start; flex-direction: column; gap: 8px; }
  .nav-account-links { margin-left: auto; }
  .nav-links { width: 100%; }
}
</style>

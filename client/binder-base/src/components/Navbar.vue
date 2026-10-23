<script setup>
import BrandEmblem from './BrandEmblem.vue';
</script>

<template>
  <nav class="main-nav" aria-label="Main navigation">
    <RouterLink to="/" class="brand-link">
      <BrandEmblem />
      <span>BinderBase</span>
    </RouterLink>
    <div class="nav-links">
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/binders">My Binders</RouterLink>
      <RouterLink to="/cards">Explore Cards</RouterLink>
    </div>
  </nav>
</template>

<style scoped>
.main-nav { display: flex; align-items: center; gap: 30px; }
.brand-link { display: flex; align-items: center; gap: 9px; color: var(--accent); font-size: 16px; font-weight: 700; text-decoration: none; }
.nav-links { display: flex; flex-wrap: wrap; gap: 7px; }
.nav-links a { padding: 8px 10px; border-radius: 6px; color: var(--muted); font-size: 13px; text-decoration: none; }
.nav-links a:hover, .nav-links a.router-link-active { color: var(--accent); background: var(--accent-soft); }

@media (max-width: 620px) {
  .main-nav { width: 100%; align-items: flex-start; flex-direction: column; gap: 8px; }
  .nav-links { width: 100%; }
}
</style>

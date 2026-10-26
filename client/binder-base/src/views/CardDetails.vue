<script setup>
import { useRoute } from 'vue-router';

const route = useRoute();
</script>

<template>
  <main class="page-shell">
    <h1>Card Details</h1>
    <p v-if="route.params.cardId">Card ID: {{ route.params.cardId }}</p>
    <p>Select a binder to add this card.</p>
    <RouterLink class="page-link" to="/binders">Choose a Binder</RouterLink>
  </main>
</template>

<style scoped>
.page-shell { max-width: 960px; margin: 0 auto; padding: 40px 24px; color: var(--text); }
.page-link { display: inline-flex; margin-top: 12px; padding: 12px 16px; border: 1px solid var(--border); border-radius: 8px; color: var(--accent); background: var(--surface); text-decoration: none; }
</style>

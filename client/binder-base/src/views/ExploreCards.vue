<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const cardId = ref('');

function openCardDetails() {
  const normalizedCardId = cardId.value.trim();
  if (!normalizedCardId) return;
  router.push(`/cardDetails/${encodeURIComponent(normalizedCardId)}`);
}
</script>

<template>
  <main class="page-shell">
    <h1>Explore Cards</h1>
    <p>Search by card ID to open card details.</p>
    <form class="card-search" @submit.prevent="openCardDetails">
      <label for="card-id">Card ID</label>
      <div class="search-row">
        <input id="card-id" v-model="cardId" autocomplete="off" required />
        <button class="page-link" type="submit">Search</button>
      </div>
    </form>
  </main>
</template>

<style scoped>
.page-shell { max-width: 960px; margin: 0 auto; padding: 40px 24px; color: var(--text); }
.card-search { display: grid; max-width: 500px; gap: 8px; margin-top: 24px; }
.search-row { display: flex; flex-wrap: wrap; gap: 10px; }
.search-row input { min-height: 44px; flex: 1 1 220px; padding: 0 12px; border: 1px solid var(--border); border-radius: 8px; color: var(--text); background: var(--surface); }
.page-link { display: inline-flex; min-height: 44px; align-items: center; justify-content: center; padding: 0 16px; border: 1px solid var(--border); border-radius: 8px; color: var(--accent-ink); background: var(--accent); font: inherit; cursor: pointer; }
</style>

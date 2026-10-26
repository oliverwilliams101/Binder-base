<template>
  <main class="page-shell">
    <h1>Dashboard</h1>
    <p>Open your binders or view binder price history.</p>
    <nav class="page-links" aria-label="Dashboard sections">
      <RouterLink to="/binders">My Binders</RouterLink>
      <RouterLink to="/binder-price-graph">Binder price graph</RouterLink>
      <RouterLink to="/cards">Explore Cards</RouterLink>
    </nav>
  </main>
</template>

<style scoped>
.page-shell { max-width: 960px; margin: 0 auto; padding: 40px 24px; color: var(--text); }
.page-links { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 24px; }
.page-links a { padding: 12px 16px; border: 1px solid var(--border); border-radius: 8px; color: var(--accent); background: var(--surface); text-decoration: none; }
</style>

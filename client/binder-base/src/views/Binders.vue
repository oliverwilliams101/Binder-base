<template>
  <main class="page-shell">
    <h1>My Binders</h1>
    <p>Open a binder to view its pages.</p>
    <RouterLink class="page-link" to="/binder">Open Binder</RouterLink>
  </main>
</template>

<style scoped>
.page-shell { max-width: 960px; margin: 0 auto; padding: 40px 24px; color: var(--text); }
.page-link { display: inline-flex; margin-top: 12px; padding: 12px 16px; border: 1px solid var(--border); border-radius: 8px; color: var(--accent); background: var(--surface); text-decoration: none; }
</style>

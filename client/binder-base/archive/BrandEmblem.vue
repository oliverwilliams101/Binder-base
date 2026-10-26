<template>
  <svg
    class="brand-emblem"
    :class="{ 'brand-emblem--large': large }"
    viewBox="5 0 310 300"
    role="img"
    aria-label="BinderBase two-card B logo"
    xmlns="http://www.w3.org/2000/svg"
  >
    <g class="logo-card" transform="rotate(-20 118 127.5)">
      <rect class="logo-card-face" x="45" y="25" width="146" height="205" rx="11" />
      <text class="logo-card-letter" x="118" y="178" text-anchor="middle">B</text>
    </g>
    <g class="logo-card" transform="rotate(20 203 172.5)">
      <rect class="logo-card-face" x="130" y="70" width="146" height="205" rx="11" />
      <text class="logo-card-letter" x="203" y="223" text-anchor="middle">B</text>
    </g>
  </svg>
</template>

<script setup>
defineProps({
  large: {
    type: Boolean,
    default: false
  }
});
</script>

<style scoped>
.brand-emblem {
  display: block;
  width: 72px;
  height: auto;
  flex: 0 0 auto;
  overflow: visible;
}

.brand-emblem--large { width: 280px; }

.logo-card-face { fill: var(--surface); stroke: var(--accent); stroke-width: 5px; }
.logo-card-letter {
  fill: var(--accent);
  font-family: 'Comic Sans MS', 'Comic Sans', cursive;
  font-size: 150px;
  font-weight: 700;
}

@media (max-width: 700px) {
  .brand-emblem--large { width: 200px; }
}
</style>

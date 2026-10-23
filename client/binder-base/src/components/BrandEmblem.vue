<template>
  <svg
    class="brand-emblem"
    :class="{ 'brand-emblem--large': large }"
    viewBox="0 0 224 160"
    role="img"
    aria-label="BinderBase emblem"
    xmlns="http://www.w3.org/2000/svg"
  >
    <g class="logo-card logo-card--left" transform="rotate(-20 72 80)">
      <rect class="logo-card-face" x="34" y="26" width="76" height="108" rx="6" />
    </g>
    <g class="logo-card logo-card--right" transform="rotate(20 152 80)">
      <rect class="logo-card-face" x="114" y="26" width="76" height="108" rx="6" />
    </g>
    <text class="logo-letter" x="72" y="110" text-anchor="middle" transform="rotate(-20 72 80)">B</text>
    <text class="logo-letter" x="152" y="110" text-anchor="middle" transform="rotate(20 152 80)">B</text>
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
  width: 112px;
  height: auto;
  flex: 0 0 auto;
  overflow: visible;
}

.brand-emblem--large { width: 280px; }

.logo-letter {
  fill: var(--accent);
  font-family: 'Comic Sans MS', 'Comic Sans', cursive;
  font-size: 80px;
  font-weight: 700;
  paint-order: normal;
}

.logo-card-face { fill: none; stroke: var(--accent); stroke-width: 2px; }

@media (max-width: 700px) {
  .brand-emblem--large { width: 200px; }
}
</style>

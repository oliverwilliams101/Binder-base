<template>
  <svg
    class="brand-emblem"
    :class="{ 'brand-emblem--large': large }"
    viewBox="20 0 224 160"
    role="img"
    aria-label="BinderBase emblem"
    xmlns="http://www.w3.org/2000/svg"
  >
    <g class="logo-card-back">
      <rect class="logo-card-back-face" x="94" y="26" width="76" height="108" rx="6" />
      <rect class="logo-card-back-inset" x="99" y="31" width="66" height="98" rx="5" />
      <path class="logo-card-back-swirl" d="M103 60C108 43 124 37 139 44c11 5 18 16 18 29-1 15-11 27-26 30-13 3-26-3-32-14m8-30c3-9 12-14 21-13 9 1 16 8 17 17 1 8-4 16-12 19-7 3-15 1-19-5" />
      <circle class="logo-ball" cx="132" cy="80" r="18" />
      <path class="logo-ball-top" d="M114 80a18 18 0 0 1 36 0Z" />
      <path class="logo-ball-seam" d="M114 80h36" />
      <circle class="logo-ball-button" cx="132" cy="80" r="6" />
    </g>
    <g class="logo-card logo-card--left" transform="rotate(-20 76 80)">
      <rect class="logo-card-face" x="38" y="26" width="76" height="108" rx="6" />
    </g>
    <g class="logo-card logo-card--right" transform="rotate(20 188 80)">
      <rect class="logo-card-face" x="150" y="26" width="76" height="108" rx="6" />
    </g>
    <text class="logo-letter" x="76" y="110" text-anchor="middle" transform="rotate(-20 76 80)">B</text>
    <text class="logo-letter" x="188" y="110" text-anchor="middle" transform="rotate(20 188 80)">B</text>
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

.logo-card-face { fill: var(--surface); stroke: var(--accent); stroke-width: 2px; }
.logo-card-back-face { fill: var(--accent); stroke: var(--accent-ink); stroke-width: 2px; }
.logo-card-back-inset { fill: none; stroke: var(--accent-hover); stroke-width: 1.5px; }
.logo-card-back-swirl { fill: none; stroke: var(--accent-hover); stroke-linecap: round; stroke-width: 4px; }
.logo-ball { fill: var(--surface); stroke: var(--accent-ink); stroke-width: 2px; }
.logo-ball-top { fill: #e74646; }
.logo-ball-seam { stroke: var(--accent-ink); stroke-width: 2px; }
.logo-ball-button { fill: var(--surface); stroke: var(--accent-ink); stroke-width: 2px; }

@media (max-width: 700px) {
  .brand-emblem--large { width: 200px; }
}
</style>

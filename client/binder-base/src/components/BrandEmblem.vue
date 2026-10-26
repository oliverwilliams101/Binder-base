<template>
  <svg
    class="brand-emblem"
    :class="{ 'brand-emblem--large': large }"
    viewBox="90 55 385 430"
    role="img"
    aria-label="BinderBase binder logo"
    xmlns="http://www.w3.org/2000/svg"
  >
    <g class="logo-cards">
      <g transform="rotate(-8 405 181)">
        <rect class="logo-card-face" x="350" y="96" width="104" height="174" rx="10" />
        <text class="logo-card-letter" x="402" y="222" text-anchor="middle">B</text>
      </g>
      <g transform="rotate(8 405 381)">
        <rect class="logo-card-face" x="350" y="296" width="104" height="174" rx="10" />
        <text class="logo-card-letter" x="402" y="422" text-anchor="middle">B</text>
      </g>
    </g>

    <path class="logo-binder-side" d="M343 65 357 72q11 5 11 17v354q0 12-11 12l-14-5z" />
    <rect class="logo-binder-cover" x="96" y="61" width="254" height="411" rx="12" />
    <path class="logo-binder-edge" d="M348 68v385" />
    <path class="logo-binder-zipper" d="M360 83v365" />
    <path class="logo-binder-zipper-teeth" d="M351 88h17m-17 24h17m-17 24h17m-17 24h17m-17 24h17m-17 24h17m-17 24h17m-17 24h17m-17 24h17m-17 24h17m-17 24h17m-17 24h17m-17 24h17m-17 24h17m-17 24h17" />
    <rect class="logo-binder-zipper-pull" x="352" y="258" width="16" height="28" rx="4" />

    <text class="logo-binder-name" x="222" y="235" text-anchor="middle">Binder</text>
    <text class="logo-binder-name" x="222" y="314" text-anchor="middle">Base</text>
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

.logo-card-face { fill: var(--surface); stroke: var(--accent); stroke-width: 4px; }
.logo-card-letter {
  fill: var(--accent);
  font-family: 'Comic Sans MS', 'Comic Sans', cursive;
  font-size: 112px;
  font-weight: 700;
}
.logo-binder-side { fill: var(--accent); }
.logo-binder-cover { fill: var(--accent); }
.logo-binder-edge { fill: none; stroke: var(--surface); stroke-width: 4px; }
.logo-binder-zipper { fill: none; stroke: var(--surface); stroke-width: 4px; }
.logo-binder-zipper-teeth { fill: none; stroke: var(--surface); stroke-width: 3px; }
.logo-binder-zipper-pull { fill: var(--accent-soft); }
.logo-binder-name {
  fill: var(--surface);
  font-family: 'Comic Sans MS', 'Comic Sans', cursive;
  font-size: 70px;
  font-weight: 700;
}

@media (max-width: 700px) {
  .brand-emblem--large { width: 200px; }
}
</style>

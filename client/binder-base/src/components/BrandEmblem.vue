<template>
  <svg
    class="brand-emblem"
    :class="{ 'brand-emblem--full': full }"
    :viewBox="full ? '0 0 460 290' : '5 0 310 300'"
    role="img"
    :aria-label="full ? 'BinderBase logo with cards in a closed binder' : 'BinderBase two-card B logo'"
    xmlns="http://www.w3.org/2000/svg"
  >
    <template v-if="full">
      <g transform="translate(140.4 0) scale(.56)">
        <g class="logo-card" transform="rotate(-20 118 127.5)">
          <rect class="logo-card-face" x="45" y="25" width="146" height="205" rx="11" />
          <text class="logo-card-letter" x="118" y="178" text-anchor="middle">B</text>
        </g>
        <g class="logo-card" transform="rotate(20 203 172.5)">
          <rect class="logo-card-face logo-card-face--front" x="130" y="70" width="146" height="205" rx="11" />
          <text class="logo-card-letter" x="203" y="223" text-anchor="middle">B</text>
        </g>
      </g>
      <g class="logo-binder">
        <path class="logo-binder-cover" d="M142 130h176q12 0 12 12v115l-3 3H133l-3-3V142q0-12 12-12Z" />
        <path class="logo-binder-spine" d="M142 131h18v125l-3 3h-23l-3-3V142q0-11 11-11Z" />
        <path class="logo-binder-spine-seam" d="M160 137v116" />
        <rect class="logo-binder-strap" x="130" y="156" width="200" height="26" />
        <text class="logo-binder-name" x="242" y="226" text-anchor="middle">BinderBase</text>
        <circle class="logo-binder-clasp" cx="230" cy="169" r="6" />
        <circle class="logo-binder-clasp-center" cx="230" cy="169" r="2" />
      </g>
    </template>
    <template v-else>
      <g class="logo-card" transform="rotate(-20 118 127.5)">
        <rect class="logo-card-face" x="45" y="25" width="146" height="205" rx="11" />
        <text class="logo-card-letter" x="118" y="178" text-anchor="middle">B</text>
      </g>
      <g class="logo-card" transform="rotate(20 203 172.5)">
        <rect class="logo-card-face logo-card-face--front" x="130" y="70" width="146" height="205" rx="11" />
        <text class="logo-card-letter" x="203" y="223" text-anchor="middle">B</text>
      </g>
    </template>
  </svg>
</template>

<script setup>
defineProps({
  full: {
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

.brand-emblem--full { width: 420px; }

.logo-card-face { fill: var(--logo-card-back); stroke: none; }
.logo-card-face--front { fill: var(--logo-card-front); }
.logo-card-letter {
  fill: var(--logo-card-back-ink);
  font-family: 'Comic Sans MS', 'Comic Sans', cursive;
  font-size: 150px;
  font-weight: 700;
}
.logo-binder-cover { fill: var(--accent); }
.logo-binder-spine { fill: var(--accent-hover); }
.logo-binder-spine-seam { fill: none; stroke: var(--accent-ink); stroke-width: 1.5; opacity: .45; }
.logo-binder-strap { fill: var(--logo-card-back); }
.logo-binder-clasp { fill: var(--accent-ink); }
.logo-binder-clasp-center { fill: var(--accent-hover); }
.logo-binder-name {
  fill: var(--accent-ink);
  font-family: 'Comic Sans MS', 'Comic Sans', cursive;
  font-size: 28px;
  font-weight: 700;
}

@media (max-width: 700px) {
  .brand-emblem--full { width: 300px; }
}

@media (max-width: 480px) {
  .brand-emblem--full { width: 235px; }
}
</style>

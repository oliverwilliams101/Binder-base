<script setup>
import { computed, ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import BrandEmblem from './components/BrandEmblem.vue';
import Navbar from './components/Navbar.vue';

const route = useRoute();
const themes = [
  { id: 'light', label: 'Light' },
  { id: 'dark', label: 'Dark' },
  { id: 'contrast', label: 'High contrast' }
];

const savedTheme = localStorage.getItem('binderbase-theme');
const activeTheme = ref(themes.some((theme) => theme.id === savedTheme) ? savedTheme : 'light');
const currentTheme = computed(() => themes.find((theme) => theme.id === activeTheme.value));
const nextTheme = computed(() => {
  const currentIndex = themes.findIndex((theme) => theme.id === activeTheme.value);
  return themes[(currentIndex + 1) % themes.length];
});
const switchHint = computed(() => `Switch to ${nextTheme.value.label.toLowerCase()} theme`);
let faviconTemplatePromise;
let faviconUpdateId = 0;

function updateFavicon() {
  const iconLink = document.querySelector('link[rel="icon"]');
  if (!iconLink) return;

  const updateId = ++faviconUpdateId;
  faviconTemplatePromise ??= fetch('/favicon.svg').then((response) => {
    if (!response.ok) throw new Error('Could not load the site icon');
    return response.text();
  });

  faviconTemplatePromise.then((template) => {
    if (updateId !== faviconUpdateId) return;

    const styles = getComputedStyle(document.documentElement);
    const themeColors = {
      accent: styles.getPropertyValue('--accent').trim(),
      hover: styles.getPropertyValue('--accent-hover').trim(),
      surface: styles.getPropertyValue('--surface').trim(),
      accentSoft: styles.getPropertyValue('--accent-soft').trim(),
      ink: styles.getPropertyValue('--accent-ink').trim()
    };
    const themeStyle = `<style id="favicon-theme">:root{--accent:${themeColors.accent};--accent-hover:${themeColors.hover};--surface:${themeColors.surface};--accent-soft:${themeColors.accentSoft};--accent-ink:${themeColors.ink}}</style>`;
    const themedIcon = template.replace(/<style id="favicon-theme">[\s\S]*?<\/style>/, themeStyle);
    iconLink.href = `data:image/svg+xml;charset=utf-8,${encodeURIComponent(themedIcon)}`;
  }).catch(() => {});
}

function cycleTheme() {
  activeTheme.value = nextTheme.value.id;
}

watch(activeTheme, (theme) => {
  document.documentElement.dataset.theme = theme;
  localStorage.setItem('binderbase-theme', theme);
  updateFavicon();
}, { immediate: true });
</script>

<template>
  <div class="app-shell">
    <header class="site-header">
      <Navbar v-if="route.meta.showNavbar" />
      <RouterLink v-else class="brand-home-link" to="/">
        <BrandEmblem />
        <span>BinderBase</span>
      </RouterLink>
      <div class="theme-control">
        <span class="theme-current" aria-live="polite">{{ currentTheme.label }}</span>
        <button
          class="theme-button"
          type="button"
          :aria-label="switchHint"
          :title="switchHint"
          aria-describedby="theme-tooltip"
          @click="cycleTheme"
        >
          <svg v-if="nextTheme.id === 'dark'" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M20.2 15.6A8.8 8.8 0 0 1 8.4 3.8 8.8 8.8 0 1 0 20.2 15.6Z" />
          </svg>
          <svg v-else-if="nextTheme.id === 'contrast'" class="contrast-icon" viewBox="0 0 24 24" aria-hidden="true">
            <circle cx="12" cy="12" r="9.2" />
            <path d="M12 2.8a9.2 9.2 0 0 0 0 18.4Z" />
          </svg>
          <svg v-else viewBox="0 0 24 24" aria-hidden="true">
            <circle cx="12" cy="12" r="4" />
            <path d="M12 2v2m0 16v2M4.93 4.93l1.42 1.42m11.3 11.3 1.42 1.42M2 12h2m16 0h2M4.93 19.07l1.42-1.42m11.3-11.3 1.42-1.42" />
          </svg>
        </button>
        <span id="theme-tooltip" class="theme-tooltip" role="tooltip">{{ switchHint }}</span>
      </div>
    </header>
    <RouterView />
  </div>
</template>

<style>
:root,
:root[data-theme='light'] {
  color-scheme: light;
  --page: #f7faff;
  --surface: #ffffff;
  --surface-soft: #edf4fd;
  --text: #17283d;
  --muted: #586b82;
  --border: #d9e4f1;
  --accent: #2879d0;
  --accent-hover: #226fbe;
  --accent-ink: #ffffff;
  --accent-soft: #e4f0ff;
  --focus: #165eae;
  --shadow: 0 18px 60px rgba(31, 67, 107, .07);
}

:root[data-theme='dark'] {
  color-scheme: dark;
  --page: #0d1623;
  --surface: #152131;
  --surface-soft: #1b2b40;
  --text: #eff5fc;
  --muted: #b3c0d0;
  --border: #34465d;
  --accent: #73b7fa;
  --accent-hover: #83bffd;
  --accent-ink: #102034;
  --accent-soft: #203b58;
  --focus: #9bceff;
  --shadow: 0 18px 60px rgba(0, 0, 0, .24);
}

:root[data-theme='contrast'] {
  color-scheme: dark;
  --page: #000000;
  --surface: #000000;
  --surface-soft: #101010;
  --text: #ffffff;
  --muted: #eeeeee;
  --border: #ffffff;
  --accent: #3db7ff;
  --accent-hover: #5fc4ff;
  --accent-ink: #000000;
  --accent-soft: #06263a;
  --focus: #ffec4a;
  --shadow: none;
}

* { box-sizing: border-box; }
html, body, #app { min-height: 100%; margin: 0; }
body, button, input, select, textarea {
  font-family: 'Comic Sans MS', 'Comic Sans', cursive;
}
body { color: var(--text); background: var(--page); }
button, input, select, textarea { color: inherit; }
button:focus-visible, a:focus-visible, input:focus-visible, select:focus-visible, textarea:focus-visible {
  outline: 3px solid var(--focus);
  outline-offset: 3px;
}

.site-header {
  display: flex;
  min-height: 64px;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  padding: 10px max(20px, calc((100vw - 1120px) / 2));
  border-bottom: 1px solid var(--border);
  background: var(--surface);
}

.theme-control {
  position: relative;
  display: flex;
  flex: 0 0 auto;
  align-items: center;
  gap: 10px;
}

.brand-home-link { display: flex; align-items: center; gap: 9px; color: var(--accent); font-size: 16px; font-weight: 700; text-decoration: none; }
.theme-current { color: var(--muted); font-size: 12px; }

.theme-button {
  display: grid;
  width: 38px;
  height: 38px;
  place-items: center;
  border: 1px solid var(--border);
  border-radius: 50%;
  color: var(--accent-ink);
  background: var(--accent);
  cursor: pointer;
}

.theme-button:hover { background: var(--accent-hover); }
.theme-button svg { width: 20px; height: 20px; fill: none; stroke: currentColor; stroke-linecap: round; stroke-linejoin: round; stroke-width: 1.8; }
.theme-button .contrast-icon path { fill: currentColor; stroke: currentColor; }
.theme-tooltip {
  position: absolute;
  z-index: 2;
  top: calc(100% + 8px);
  right: 0;
  width: max-content;
  max-width: 220px;
  padding: 7px 10px;
  border: 1px solid var(--border);
  border-radius: 6px;
  color: var(--text);
  background: var(--surface);
  box-shadow: var(--shadow);
  font-size: 12px;
  pointer-events: none;
  visibility: hidden;
}
.theme-control:hover .theme-tooltip,
.theme-button:focus-visible + .theme-tooltip { visibility: visible; }

@media (max-width: 620px) {
  .site-header { align-items: flex-start; flex-direction: column; gap: 10px; padding: 12px 16px; }
  .theme-control { align-self: flex-end; }
}
</style>

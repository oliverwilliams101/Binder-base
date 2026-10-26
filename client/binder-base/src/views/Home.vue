<script setup>
import { computed, onBeforeUnmount, onMounted, ref } from 'vue';
import BrandEmblem from '../components/BrandEmblem.vue';
import { useAuth } from '../services/auth';

const { isAuthenticated } = useAuth();

const welcomePhrase = 'Welcome to BinderBase.';
const welcomeFirstLine = Array.from(welcomePhrase.slice(0, 10));
const welcomeSecondLine = Array.from(welcomePhrase.slice(11));
const typedCharacterCount = ref(0);
const animationDuration = 5000;
const typeDelay = 150;
const eraseDelay = 50;
const completePause = animationDuration - welcomePhrase.length * (typeDelay + eraseDelay);
const restartPause = 500;
let typewriterTimer;

onMounted(() => {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    typedCharacterCount.value = welcomePhrase.length;
    return;
  }

  let characterIndex = 0;
  let deleting = false;

  const tick = () => {
    typedCharacterCount.value = characterIndex;

    if (deleting) {
      if (characterIndex > 0) {
        characterIndex -= 1;
        typewriterTimer = window.setTimeout(tick, eraseDelay);
      } else {
        deleting = false;
        typewriterTimer = window.setTimeout(tick, restartPause);
      }
      return;
    }

    if (characterIndex < welcomePhrase.length) {
      characterIndex += 1;
      typewriterTimer = window.setTimeout(tick, typeDelay);
    } else {
      deleting = true;
      typewriterTimer = window.setTimeout(tick, completePause);
    }
  };

  tick();
});

onBeforeUnmount(() => window.clearTimeout(typewriterTimer));

const destinations = computed(() => {
  const sections = [
    {
      number: '01',
      title: 'My Binders',
      description: 'Open the My Binders section.',
      to: '/binders',
      label: 'Go to My Binders'
    },
    {
      number: '02',
      title: 'Explore Cards',
      description: 'Open the Explore Cards section.',
      to: '/cards',
      label: 'Go to Explore Cards'
    }
  ];

  if (isAuthenticated.value) {
    sections.unshift({
      number: '',
      title: 'Dashboard',
      description: 'Open your Dashboard.',
      to: '/dashboard',
      label: 'Go to Dashboard'
    });
  }

  return sections.map((section, index) => ({
    ...section,
    number: String(index + 1).padStart(2, '0')
  }));
});
</script>

<template>
  <main class="home-shell">
    <section class="welcome" aria-labelledby="welcome-title">
      <div class="welcome-copy">
        <p class="eyebrow"><span class="status-dot" aria-hidden="true"></span> YOUR BINDERBASE HOME</p>
        <h1 id="welcome-title" aria-label="Welcome to BinderBase.">
          <span class="welcome-title-visible" aria-hidden="true">
            <span class="welcome-title-line">
              <span
                v-for="(character, index) in welcomeFirstLine"
                :key="`first-${index}`"
                :class="{ 'welcome-character-hidden': typedCharacterCount <= index }"
              >{{ character }}</span>
            </span>
            <span class="welcome-title-line welcome-title-accent">
              <span
                v-for="(character, index) in welcomeSecondLine"
                :key="`second-${index}`"
                :class="{ 'welcome-character-hidden': typedCharacterCount <= index + 11 }"
              >{{ character }}</span>
            </span>
          </span>
        </h1>
        <p v-if="!isAuthenticated" class="intro">
          Sign in or create an account. You can also use the links below to open a section.
        </p>
        <p v-else class="intro">Open your dashboard, binders, or explore cards.</p>
        <div class="welcome-actions">
          <RouterLink v-if="!isAuthenticated" class="button button-primary" to="/login">
            Sign in
          </RouterLink>
          <RouterLink v-if="!isAuthenticated" class="button button-secondary" to="/register">Create account</RouterLink>
          <RouterLink v-else class="button button-primary" to="/dashboard">Open Dashboard</RouterLink>
        </div>
      </div>

      <BrandEmblem class="welcome-mark" large />
    </section>

    <section class="destinations" aria-labelledby="destinations-title">
      <div class="section-heading">
        <div>
          <p class="eyebrow">SITE SECTIONS</p>
          <h2 id="destinations-title">Navigate BinderBase</h2>
        </div>
        <span class="section-note">Choose a section to open</span>
      </div>

      <div class="destination-grid">
        <RouterLink
          v-for="destination in destinations"
          :key="destination.to"
          class="destination-card"
          :to="destination.to"
          :aria-label="destination.label"
        >
          <span class="destination-number">{{ destination.number }}</span>
          <span class="destination-title">{{ destination.title }}</span>
          <span class="destination-description">{{ destination.description }}</span>
        </RouterLink>
      </div>
    </section>

    <footer class="home-footer">
      <span class="footer-brand">BinderBase</span>
      <span>Account access and sections</span>
    </footer>
  </main>
</template>

<style scoped>
.home-shell {
  min-height: calc(100vh - 64px);
  padding: clamp(28px, 5vw, 72px) max(24px, calc((100vw - 1120px) / 2));
  color: var(--text);
  background:
    radial-gradient(ellipse at 84% 13%, var(--accent-soft), transparent 32%),
    var(--page);
}

.welcome {
  position: relative;
  display: flex;
  min-height: 330px;
  align-items: center;
  justify-content: space-between;
  overflow: hidden;
  padding: clamp(30px, 6vw, 70px);
  border: 1px solid var(--border);
  border-radius: 18px;
  background: var(--surface);
  box-shadow: var(--shadow);
}

.welcome-copy { position: relative; z-index: 1; max-width: 510px; }
.eyebrow { margin: 0; color: var(--muted); font-size: 11px; font-weight: 700; letter-spacing: .15em; }
.welcome .eyebrow { display: flex; align-items: center; gap: 9px; }
.status-dot { width: 7px; height: 7px; border-radius: 50%; background: var(--accent); box-shadow: 0 0 0 4px var(--accent-soft); }
h1 { min-height: 1.98em; margin: 22px 0 13px; font-size: clamp(48px, 7.4vw, 78px); line-height: .99; letter-spacing: -.065em; font-weight: 650; }
.welcome-title-visible { display: block; }
.welcome-title-line { display: block; min-height: .99em; }
.welcome-character-hidden { visibility: hidden; }
.welcome-title-accent { color: var(--accent); font-style: normal; font-weight: 700; }
.intro { max-width: 430px; margin: 0; color: var(--muted); font-size: 15px; line-height: 1.7; }
.welcome-actions { display: flex; flex-wrap: wrap; gap: 11px; margin-top: 27px; }
.button { display: inline-flex; min-height: 44px; align-items: center; justify-content: center; gap: 18px; padding: 0 18px; border: 1px solid transparent; border-radius: 7px; color: inherit; font-size: 13px; font-weight: 650; text-decoration: none; }
.button-primary { color: var(--accent-ink); background: var(--accent); }
.button-primary:hover { background: var(--accent-hover); }
.button-secondary { border-color: var(--border); background: var(--surface); }
.button-secondary:hover { border-color: var(--accent); }

.welcome-mark { display: block; flex: 0 0 auto; margin: 0 5% 0 24px; }

.destinations { padding: 47px 2px 0; }
.section-heading { display: flex; align-items: end; justify-content: space-between; gap: 16px; margin-bottom: 19px; }
h2 { margin: 8px 0 0; font-size: 24px; letter-spacing: -.035em; font-weight: 700; }
.section-note { padding-bottom: 3px; color: var(--muted); font-size: 12px; }
.destination-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 13px; }
.destination-card { position: relative; display: flex; min-height: 145px; flex-direction: column; padding: 20px; border: 1px solid var(--border); border-radius: 11px; color: inherit; background: var(--surface); text-decoration: none; }
.destination-card:hover { border-color: var(--accent); box-shadow: var(--shadow); }
.destination-number { color: var(--muted); font-size: 10px; font-weight: 700; letter-spacing: .1em; }
.destination-title { margin-top: auto; font-size: 16px; font-weight: 700; letter-spacing: -.02em; }
.destination-description { margin-top: 5px; color: var(--muted); font-size: 12px; line-height: 1.5; }
.home-footer { display: flex; justify-content: space-between; margin-top: 34px; padding-top: 17px; border-top: 1px solid var(--border); color: var(--muted); font-size: 11px; }
.footer-brand { color: var(--accent); font-weight: 700; }

@media (max-width: 700px) {
  .home-shell { padding-right: 18px; padding-left: 18px; }
  .welcome { min-height: auto; padding: 34px 27px; }
  .welcome-mark { margin-right: -25px; margin-left: 0; }
  .destination-grid { grid-template-columns: 1fr; }
  .destination-card { min-height: 118px; }
}

@media (max-width: 480px) {
  .welcome { align-items: flex-start; }
  .welcome-mark { position: absolute; top: -18px; right: -48px; }
  .welcome-copy { max-width: 100%; }
  .section-heading { align-items: flex-start; flex-direction: column; gap: 8px; }
}
</style>

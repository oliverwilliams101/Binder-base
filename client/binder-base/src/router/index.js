import { createRouter, createWebHistory } from 'vue-router';
import { useAuth } from '../services/auth';

const { user, initializeAuth } = useAuth();

const routes = [
  {
    path: '/',
    component: () => import('../views/Home.vue'),
    meta: { showNavbar: true }
  },
  {
    path: '/login',
    component: () => import('../views/Login.vue'),
    meta: { showNavbar: false, guestOnly: true }
  },
  {
    path: '/register',
    component: () => import('../views/Register.vue'),
    meta: { showNavbar: false, guestOnly: true }
  },
  {
    path: '/dashboard',
    component: () => import('../views/Dashboard.vue'),
    meta: { showNavbar: true, requiresAuth: true }
  },
  {
    path: '/binders',
    component: () => import('../views/Binders.vue'),
    meta: { showNavbar: true }
  },
  {
    path: '/binder/:userId/:binderId/:pageNum',
    component: () => import('../views/Binder.vue'),
    meta: { showNavbar: true }
  },
  {
    path: '/binder',
    component: () => import('../views/Binder.vue'),
    meta: { showNavbar: true }
  },
  {
    path: '/binder-price-graph',
    component: () => import('../views/BinderPriceGraph.vue'),
    meta: { showNavbar: true }
  },
  {
    path: '/cards',
    component: () => import('../views/ExploreCards.vue'),
    meta: { showNavbar: true }
  },
  {
    path: '/profile',
    component: () => import('../views/Profile.vue'),
    meta: { showNavbar: true }
  },
  {
    path: '/cardDetails/:cardId',
    component: () => import('../views/CardDetails.vue'),
    meta: { showNavbar: true }
  },
  {
    path: '/cardDetails',
    component: () => import('../views/CardDetails.vue'),
    meta: { showNavbar: true }
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach(async (to) => {
  await initializeAuth();

  if (to.meta.requiresAuth && !user.value) {
    return { path: '/login', query: { redirect: to.fullPath } };
  }
  if (to.meta.guestOnly && user.value) {
    return { path: '/dashboard' };
  }
});

export default router;

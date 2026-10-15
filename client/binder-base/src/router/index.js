import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    component: () => import('../views/Home.vue'),
    meta: { showNavbar: true }
  },
  {
    path: '/login',
    component: () => import('../views/Login.vue'),
    meta: { showNavbar: false }
  },
  {
    path: '/register',
    component: () => import('../views/Register.vue'),
    meta: { showNavbar: false }
  },
  {
    path: '/dashboard',
    component: () => import('../views/Dashboard.vue'),
    meta: { showNavbar: true }
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
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
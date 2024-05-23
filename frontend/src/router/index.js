import { createRouter, createWebHistory } from 'vue-router';
import DataFetch from '@/components/DataFetch.vue';

const routes = [
  {
    path: '/',
    name: 'DataFetch',
    component: DataFetch,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

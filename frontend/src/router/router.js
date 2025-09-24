import { createWebHistory, createRouter } from "vue-router";

import LandingView from "@/modules/LandingPage/views/LandingView.vue";
import ProductSearchView from "@/modules/ProductSearch/views/ProductSearchView.vue";

const routes = [
  { path: "/", component: LandingView },
  { path: "/buscar", component: ProductSearchView },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

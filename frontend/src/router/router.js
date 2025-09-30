import { createWebHistory, createRouter } from "vue-router";

import LandingView from "@/modules/LandingPage/views/LandingView.vue";
import ProductSearchView from "@/modules/ProductSearch/views/ProductSearchView.vue";
import LoginView from "@/modules/Auth/views/LoginView.vue";
import RegisterView from "@/modules/Auth/views/RegisterView.vue";

const routes = [
  {
    path: "/",
    component: LandingView,
    meta: { transition: "fade-zoom" },
  },
  {
    path: "/buscar",
    component: ProductSearchView,
    meta: { transition: "fade-zoom" },
  },
  {
    path: "/ingresar",
    component: LoginView,
    meta: { transition: "fade-zoom" },
  },
  {
    path: "/registrarse",
    component: RegisterView,
    meta: { transition: "fade-zoom" },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    return { top: 0 };
  },
});

export default router;

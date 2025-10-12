import { createWebHistory, createRouter } from "vue-router";

import LandingView from "@/modules/LandingPage/views/LandingView.vue";
import TermsConditionsView from "@/modules/LandingPage/views/TermsConditionsView.vue";
import PrivatePolicyView from "@/modules/LandingPage/views/PrivatePolicyView.vue";
import ProductSearchView from "@/modules/ProductSearch/views/ProductSearchView.vue";
import LoginView from "@/modules/Auth/views/LoginView.vue";
import RegisterView from "@/modules/Auth/views/RegisterView.vue";
import DashboardView from "@/modules/Admin/views/DashboardView.vue";
import MainViewSeller from "@/modules/Seller/views/MainView.vue";
import MainViewStaff from "@/modules/PurchasingStaff/views/MainView.vue";
import QuoteView from "@/modules/Quote/views/QuoteView.vue";
import PurchaseOrderView from "@/modules/PurchaseOrder/views/PurchaseOrderView.vue";
import Unauthorized from "@/shared/components/Unauthorized.vue";

const routes = [
  {
    path: "/",
    component: LandingView,
    meta: { transition: "fade-zoom" },
  },
  {
    path: "/politica",
    component: PrivatePolicyView,
    meta: { transition: "fade-zoom" },
  },
  {
    path: "/terminos-condiciones",
    component: TermsConditionsView,
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
  {
    path: "/cotizacion",
    component: QuoteView,
    meta: { transition: "fade-zoom" },
  },
  {
    path: "/orden-compra",
    component: PurchaseOrderView,
    meta: { transition: "fade-zoom" },
  },
  {
    path: "/admin",
    component: DashboardView,
    meta: { transition: "fade-zoom", requiresAuth: true, roles: ["ADMIN"] },
  },
  {
    path: "/vendedor",
    component: MainViewSeller,
    meta: { transition: "fade-zoom", requiresAuth: true, roles: ["SELLER"] },
  },
  {
    path: "/compras",
    component: MainViewStaff,
    meta: { transition: "fade-zoom", requiresAuth: true, roles: ["SHOPPER"] },
  },
  {
    path: "/unauthorized",
    component: Unauthorized,
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

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem("token");
  const rol = localStorage.getItem("rol");

  // Si requiere autenticación y no hay token
  if (to.meta.requiresAuth && !token) {
    return next("/ingresar");
  }

  // Si la ruta tiene roles definidos y el usuario no cumple
  if (to.meta.roles && !to.meta.roles.includes(rol)) {
    return next("/unauthorized");
  }

  next();
});

export default router;

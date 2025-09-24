import { createWebHistory, createRouter } from "vue-router";

import LandingView from "@/modules/LandingPage/views/LandingView.vue";

const routes = [{ path: "/", component: LandingView }];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

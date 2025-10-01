import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import { createPinia } from 'pinia'
import router from "./router/router.js";
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";

const pinia = createPinia()
const app = createApp(App);

app.use(Toast);
app.use(pinia)
app.use(router);
app.mount("#app");

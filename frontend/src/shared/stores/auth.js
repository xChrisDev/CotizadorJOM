import { defineStore } from "pinia";
import { ref } from "vue";

export const useAuthStore = defineStore("auth", () => {
  const token = ref("");
  const rol = ref("");

  function login(newToken, newRol) {
    token.value = newToken;
    rol.value = newRol;
    localStorage.setItem("token", newToken);
    localStorage.setItem("rol", newRol);
  }

  function logout() {
    token.value = "";
    rol.value = "";
    localStorage.removeItem("token");
    localStorage.removeItem("rol");
  }

  return { token, rol, login, logout };
});

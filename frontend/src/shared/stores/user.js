import { defineStore } from "pinia";
import { ref } from "vue";
import { getProfileUser } from "@/modules/Auth/services/authService";

export const useUserStore = defineStore("user", () => {
  const user = ref(null);

  async function fetchUser() {
    try {
      const data = await getProfileUser();
      user.value = data.user ?? null;
    } catch (err) {
      user.value = null;
      console.error("Error al cargar perfil:", err);
    }
  }

  return { user, fetchUser };
});

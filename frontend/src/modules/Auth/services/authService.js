import apiClient from "@/shared/services/baseURL";

export const loginUser = async (userData) => {
  try {
    const response = await apiClient.post("/auth/login", userData);

    return { success: true, data: response.data };
  } catch (error) {
    if (error.response && error.response.data) {
      return { success: false, errors: error.response.data };
    } else {
      return { success: false, errors: { general: ["Error de conexión."] } };
    }
  }
};

export const registerUser = async (userData) => {
  try {
    const response = await apiClient.post("/auth/register", userData);
    return { success: true, data: response.data };
  } catch (error) {
    if (error.response && error.response.data) {
      return { success: false, errors: error.response.data };
    } else {
      return { success: false, errors: { general: ["Error de conexión."] } };
    }
  }
};

export const getProfileUser = async () => {
  const response = await apiClient.post("/auth/me", {});
  return response.data;
};

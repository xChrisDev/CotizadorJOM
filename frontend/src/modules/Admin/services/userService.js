import apiClient from "@/shared/services/baseURL";

export const fetchUsers = async (role, params = {}) => {
  try {
    const response = await apiClient.get(`/users/get_by_role/${role}/`, {
      params,
    });

    return response.data;
  } catch (error) {
    console.error("Error fetching users:", error);
    throw error;
  }
};

export const fetchPendingUsers = async (params = {}) => {
  try {
    const response = await apiClient.get("/users/pending/", { params });

    return response.data;
  } catch (error) {
    console.error("Error fetching users:", error);
    throw error;
  }
};

export const fetchUserById = async (userId) => {
  try {
    const response = await apiClient.get(`/users/${userId}/`);
    return response.data;
  } catch (error) {
    console.error("Error fetching user by id", error);
    throw error;
  }
};

export const patchUser = async (userId, data) => {
  try {
    const response = await apiClient.patch(`/users/${userId}/`, data);
  } catch (error) {
    console.error("Error updating user:", error.response.data);
    throw error;
  }
};

import apiClient from "@/shared/services/baseURL";

export const fetchUsers = async (role, params = {}) => {
  try {
    const response = await apiClient.get(`/users/get_by_role/${role}/`, { params });
    console.log(response);
    
    return response.data;
  } catch (error) {
    console.error("Error fetching users:", error);
    throw error;
  }
};

export const fetchPendingUsers = async (params = {}) => {
  try {
    const response = await apiClient.get("/users/pending/", { params });
    console.log(response);
    
    return response.data;
  } catch (error) {
    console.error("Error fetching users:", error);
    throw error;
  }
};
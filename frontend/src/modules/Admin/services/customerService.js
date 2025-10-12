import apiClient from "@/shared/services/baseURL";

export const fetchCustomers = async (params = {}) => {
  try {
    const response = await apiClient.get("/customers/", { params });
    return response.data;
  } catch (error) {
    console.error("Error fetching customers:", error);
    throw error;
  }
};

export const fetchCustomersPending = async (params = {}) => {
  try {
    const response = await apiClient.get("/customers/pending/", { params });
    return response.data;
  } catch (error) {
    console.error("Error fetching customers:", error);
    throw error;
  }
};
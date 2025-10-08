import apiClient from "@/shared/services/baseURL";

export const fetchPurchasingStaff = async (params = {}) => {
  try {
    const response = await apiClient.get("/purchasing-staff/", { params });
    return response.data;
  } catch (error) {
    console.error("Error fetching staff:", error);
    throw error;
  }
};

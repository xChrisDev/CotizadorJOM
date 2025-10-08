import apiClient from "@/shared/services/baseURL";

export const fetchSellers = async (params = {}) => {
  try {
    const response = await apiClient.get("/sellers/", { params });
    return response.data;
  } catch (error) {
    console.error("Error fetching sellers:", error);
    throw error;
  }
};

export const fetchSellerByID = async (id) => {
  try {
    const response = await apiClient.get("/sellers/" + id);
    return response.data;
  } catch (error) {
    console.error("Error fetching sellers:", error);
    throw error;
  }
};

export const putSeller = async (id, data) => {
  try {
    const response = await apiClient.put(`/sellers/${id}`, data);
    return response.data;
  } catch (error) {
    console.error("Error updating sellers:", error);
    throw error;
  }
};

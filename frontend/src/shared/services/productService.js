import apiClient from "@/shared/services/baseURL";

export const fetchArticles = async (params = {}) => {
  try {
    const response = await apiClient.get("/articles/", { params });
    return response.data;
  } catch (error) {
    console.error("Error fetching products:", error);
    throw error;
  }
};

export const fetchCategories = async (params = {}) => {
  try {
    const response = await apiClient.get("/categories/", { params });
    return response.data;
  } catch (error) {
    console.error("Error fetching categories:", error);
    throw error;
  }
};

export const fetchBrands = async (params = {}) => {
  try {
    const response = await apiClient.get("/brands/", { params });
    return response.data;
  } catch (error) {
    console.error("Error fetching brands:", error);
    throw error;
  }
};

export const fetchFamilies = async (params = {}) => {
  try {
    const response = await apiClient.get("/families/", { params });
    return response.data;
  } catch (error) {
    console.error("Error fetching families:", error);
    throw error;
  }
};
import apiClient from "@/shared/services/baseURL";

export const fetchQuotes = async (params = {}) => {
  try {
    const response = await apiClient.get("/quotes/", {
      params,
    });

    return response.data;
  } catch (error) {
    console.error("Error fetching quotes:", error);
    throw error;
  }
};

export const fetchQuotesByCustomerAndStatus = async () => {
  try {
    const response = await apiClient.get("/quotes/customer/all");
    return response.data;
  } catch (error) {
    console.error("Error fetching quotes:", error);
    throw error;
  }
};

export const fetchQuotesBySeller = async (params = {}, idSeller) => {
  try {
    const response = await apiClient.get(`/quotes/seller/${idSeller}`, {
      params,
    });

    return response.data;
  } catch (error) {
    console.error("Error fetching quotes:", error);
    throw error;
  }
};

export const postQuote = async (data) => {
  try {
    const response = await apiClient.post("/quotes/", data);
    return response.data;
  } catch (error) {
    console.error("Error creating quote:", error.response.data);
    throw error;
  }
};

export const downloadQuote = async (quoteId) => {
  try {
    const response = await apiClient.get(`/quotes/${quoteId}/download/`, {
      responseType: "blob",
    });

    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement("a");
    link.href = url;
    link.setAttribute("download", `JOM_cotizacion_${quoteId}.pdf`);
    document.body.appendChild(link);
    link.click();

    link.remove();
    window.URL.revokeObjectURL(url);

    return true;
  } catch (error) {
    console.error(
      "Error downloading quote:",
      error.response?.data || error.message
    );
    throw error;
  }
};

export const printQuote = async (quoteId) => {
  try {
    const response = await apiClient.get(`/quotes/${quoteId}/pdf/`, {
      responseType: "blob",
    });

    const file = new Blob([response.data], { type: "application/pdf" });
    const fileURL = URL.createObjectURL(file);

    const printWindow = window.open(fileURL);
    if (printWindow) {
      printWindow.focus();
      printWindow.onload = () => {
        printWindow.print();
      };
    } else {
      console.error("Error opening printing window.");
    }
  } catch (error) {
    console.error("Error printing:", error.response?.data || error.message);
    throw error;
  }
};

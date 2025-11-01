export const getStatusClasses = (status) => {
  const s = status.toLowerCase();
  switch (s) {
    case "active":
      return "bg-green-200 text-green-800 border-1 border-green-400/60";
    case "rejected":
      return "bg-red-100 text-red-800 border-1 border-red-400/30";
    case "pending":
      return "bg-yellow-100 text-yellow-800 border-1 border-yellow-400/30";
    case "banned":
      return "bg-gray-100 text-gray-800 border-1 border-gray-400/30";
    default:
      return "bg-gray-100 text-gray-800 border-1 border-gray-400/30";
  }
};

export const getStatusText = (status) => {
  const s = status.toLowerCase();
  switch (s) {
    case "active":
      return "Activo";
    case "rejected":
      return "Rechazado";
    case "pending":
      return "Pendiente";
    case "banned":
      return "Suspendido";
    default:
      return "Desconocido";
  }
};

export const getQuoteStatus = (status) => {
  const s = status.toLowerCase();

  switch (s) {
    case "draft":
      return {
        text: "Borrador",
        class: "bg-gray-100 text-gray-800 border border-gray-400/30",
      };
    case "accepted":
      return {
        text: "Aceptado",
        class: "bg-green-200 text-green-800 border border-green-400/60",
      };
    case "expired":
      return {
        text: "Expirado",
        class: "bg-red-100 text-red-800 border border-red-400/30",
      };
    case "sent":
      return {
        text: "Enviado",
        class: "bg-indigo-100 text-indigo-800 border border-indigo-400/30",
      };
    case "delivered":
      return {
        text: "Entregado",
        class: "bg-blue-100 text-blue-800 border border-blue-400/30",
      };
  }
};

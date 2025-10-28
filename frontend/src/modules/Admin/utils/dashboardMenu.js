import {
  LayoutDashboard,
  Calculator,
  Bell,
  Shield,
  ChevronDown,
  Users,
  Briefcase,
  Truck,
  Archive,
  Package,
  FileText,
  FolderKanban,
  FilePieChart,
  ShoppingCart,
} from "lucide-vue-next";

export const menuItems = [
  {
    title: "Administracion",
    url: "/admin",
    icon: Shield,
    items: [
      {
        title: "Clientes",
        icon: Users,
        url: "/admin/clientes",
      },
      {
        title: "Vendedores",
        icon: Briefcase,
        url: "/admin/vendedores",
      },
      {
        title: "Personal de compras",
        icon: Truck,
        url: "/admin/staff",
      },
    ],
  },
  {
    title: "Gestión del cotizador",
    url: "#",
    icon: Archive,
    items: [
      {
        title: "Articulos",
        icon: Package,
        url: "/admin/articulos",
      },
      {
        title: "Cotizaciones",
        icon: FileText,
        url: "/admin/cotizaciones",
      },
    ],
  },
  {
    title: "Documentos",
    url: "#",
    icon: FolderKanban,
    items: [
      {
        title: "Reportes",
        icon: FilePieChart,
        url: "#",
      },
      {
        title: "Ordenes de compra",
        icon: ShoppingCart,
        url: "#",
      },
    ],
  },
];

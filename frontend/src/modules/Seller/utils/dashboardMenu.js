import {
  LayoutDashboard,
  Calculator,
  Bell,
  Shield,
  ChevronDown,
  FileUser,
  UserPlus,
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
    title: "Registro",
    url: "/vendedor",
    icon: FileUser,
    items: [
      {
        title: "Clientes",
        icon: UserPlus,
        url: "/vendedor/clientes",
      },
      {
        title: "Solicitudes",
        icon: Bell,
        url: "/vendedor/solicitudes",
      }
    ],
  },
  {
    title: "Cotizador",
    url: "#",
    icon: Archive,
    items: [
      {
        title: "Articulos",
        icon: Package,
        url: "/vendedor/articulos",
      },
      {
        title: "Cotizaciones",
        icon: FileText,
        url: "/vendedor/cotizaciones",
      },
      {
        title: "Ordenes de compra",
        icon: ShoppingCart,
        url: "#",
      },
    ],
  }
];

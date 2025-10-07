import {
  LayoutDashboard,
  Users,
  Settings,
  UserCheck,
  UserX,
  UserCog,
  TrendingUp,
  FileText,
  ShoppingCart,
  FileOutput,
  UserRoundPlus,
} from "lucide-vue-next";

export const menuItems = [
  {
    title: "Dashboard",
    url: "/admin",
    icon: LayoutDashboard,
  },
  {
    title: "Solicitudes",
    url: "/admin/solicitudes",
    icon: UserRoundPlus,
  },
  {
    title: "Clientes",
    url: "/admin/clientes",
    icon: Users,
  },
  {
    title: "Vendedores",
    url: "/admin/vendedores",
    icon: Users,
  },
  {
    title: "Personal de Compras",
    url: "/admin/compras",
    icon: Users,
  },
  {
    title: "Reportes",
    url: "/admin/reportes",
    icon: FileText,
  },
  {
    title: "Cotizaciones",
    url: "/admin/cotizaciones",
    icon: FileOutput,
  },
  {
    title: "Ordenes de compra",
    url: "/admin/ordenes-compra",
    icon: ShoppingCart,
  },
];

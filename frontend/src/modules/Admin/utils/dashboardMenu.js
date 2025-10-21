import {
  LayoutDashboard,
  Users,
  FileText,
  ShoppingCart,
  FileOutput,
  UserRoundPlus,
} from "lucide-vue-next";

export const menuItems = [
  {
    title: "Dashboard",
    option: "dashboard",
    icon: LayoutDashboard,
  },
  {
    title: "Cotizar",
    option: "cotizar",
    icon: FileOutput,
  },
  {
    title: "Solicitudes",
    option: "solicitudes",
    icon: UserRoundPlus,
  },
  {
    title: "Clientes",
    option: "clientes",
    icon: Users,
  },
  {
    title: "Vendedores",
    option: "vendedores",
    icon: Users,
  },
  {
    title: "Personal de Compras",
    option: "compras",
    icon: Users,
  },
  {
    title: "Reportes",
    option: "reportes",
    icon: FileText,
  },
  {
    title: "Cotizaciones",
    option: "cotizaciones",
    icon: FileOutput,
  },
  {
    title: "Ordenes de compra",
    option: "ordenes",
    icon: ShoppingCart,
  },
];

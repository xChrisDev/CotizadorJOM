import {
  LayoutDashboard,
  Users,
  FileText,
  ShoppingCart,
  FileOutput,
  UserRoundPlus,
  PackagePlus
} from "lucide-vue-next";

export const menuItems = [
  {
    title: "Dashboard",
    option: "dashboard",
    icon: LayoutDashboard,
    url: "/dashboard"
  },
  {
    title: "Cotizar",
    option: "cotizar",
    icon: FileOutput,
    url: "/cotizar"
  },
  {
    title: "Solicitudes",
    option: "solicitudes",
    icon: UserRoundPlus,
    url: "/solicitudes"
  },
  {
    title: "Clientes",
    option: "clientes",
    icon: Users,
    url: "/clientes"
  },
  {
    title: "Vendedores",
    option: "vendedores",
    icon: Users,
    url: "/vendedores"
  },
  {
    title: "Personal de Compras",
    option: "compras",
    icon: Users,
    url: "/staff"
  },
  {
    title: "Reportes",
    option: "reportes",
    icon: FileText,
    url: "/reportes"
  },
  {
    title: "Cotizaciones",
    option: "cotizaciones",
    icon: FileOutput,
    url: "/cotizaciones"
  },
  {
    title: "Ordenes de compra",
    option: "ordenes",
    icon: ShoppingCart,
    url: "/ordenes"
  },
  {
    title: "Articulos",
    option: "articulos",
    icon: PackagePlus,
    url: "/articulos"
  },
];

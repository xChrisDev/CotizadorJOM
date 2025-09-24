<script setup>
import { Card, CardHeader, CardContent } from "@/shared/components/ui/card";
import { Badge } from "@/shared/components/ui/badge";
import { Calculator, Search, FileText, ShoppingCart } from "lucide-vue-next";

const services = [
  {
    icon: Calculator,
    title: "Cotización Inteligente",
    description: "Sistema avanzado de cotización disponible 24/7 que permite a clientes y vendedores generar cotizaciones inmediatas, reduciendo tiempos de espera.",
    badge: "Popular"
  },
  {
    icon: Search,
    title: "Búsqueda Guiada de Refacciones",
    description: "Filtro por categoría, modelo y familia del vehículo, acompañado de ayudas visuales para identificar piezas complejas con facilidad.",
    badge: "Nuevo"
  },
  {
    icon: FileText,
    title: "Documentos Automáticos",
    description: "Generación inmediata de cotizaciones y órdenes de compra en PDF con opción de descarga o envío directo por correo y WhatsApp.",
    badge: "Automatico"
  },
  {
    icon: ShoppingCart,
    title: "Carrito y Conversión a Orden",
    description: "Convierte fácilmente las cotizaciones en órdenes de compra, reservando inventario y garantizando la disponibilidad de los productos.",
    badge: "Eficiente"
  }
];
</script>

<template>
  <section class="bg-gradient-to-b from-gray-50/50 to-white dark:from-gray-900/50 dark:to-background">
    <div id="services" class="w-[90%] md:w-[70%] lg:w-[75%] lg:max-w-screen-xl mx-auto py-20 md:py-32 ">
      <div class="text-center mb-16">
        <h2 class="text-4xl md:text-5xl font-bold mb-6">
          Servicios que
          <span class="text-transparent bg-gradient-to-r from-[#4ed636] to-[#048044] bg-clip-text">
            transforman
          </span>
          tu experiencia
        </h2>

        <p class="text-xl text-muted-foreground max-w-3xl mx-auto">
          Descubre cómo nuestros servicios especializados pueden optimizar tu proceso de cotización
          y ahorrarte tiempo y esfuerzo en cada compra.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-8">
        <Card v-for="service in services" :key="service.title"
          class="group hover:shadow-2xl transition-all duration-500 hover:-translate-y-2 border-2 hover:border-[#4ed636]/20 bg-gradient-to-br from-white to-gray-50/50 dark:from-gray-900 dark:to-gray-800/50">
          <CardHeader class="pb-4">
            <div class="flex items-start justify-between mb-4">
              <div
                class="p-3 rounded-xl bg-gradient-to-r from-[#4ed636]/10 to-[#09cb6d]/10 group-hover:from-[#4ed636]/20 group-hover:to-[#09cb6d]/20 transition-all duration-300">
                <component :is="service.icon"
                  class="w-8 h-8 text-[#4ed636] group-hover:scale-110 transition-transform duration-300" />
              </div>
              <Badge class="bg-[#4ed636]/10 text-[#048044] border-[#4ed636]/20 font-semibold">
                {{ service.badge }}
              </Badge>
            </div>
            <h3 class="text-xl font-bold text-foreground group-hover:text-[#048044] transition-colors duration-300">
              {{ service.title }}
            </h3>
          </CardHeader>
          <CardContent>
            <p class="text-muted-foreground leading-relaxed">
              {{ service.description }}
            </p>
          </CardContent>
        </Card>
      </div>
    </div>
  </section>
</template>
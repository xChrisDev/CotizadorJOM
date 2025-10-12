<script setup>
import { ref } from 'vue'; // 1. Importar ref
import { Card, CardHeader, CardContent } from "@/shared/components/ui/card";
import { Badge } from "@/shared/components/ui/badge";
// 2. Importar los componentes del Modal/Dialog
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
} from '@/shared/components/ui/dialog'
import { Calculator, Search, FileText, ShoppingCart } from "lucide-vue-next";

// 3. Actualizar el arreglo de servicios
const services = [
  {
    icon: Calculator,
    title: "Cotización Inteligente",
    description: "Sistema avanzado de cotización disponible 24/7 que permite a clientes y vendedores generar cotizaciones inmediatas.",
    badge: "Popular",
    imageUrl: "src/shared/assets/hero-image.jpg",
    detailedDescription: "Nuestro sistema de cotización inteligente utiliza algoritmos avanzados para ofrecer precios precisos en tiempo real. Está disponible 24/7, permitiendo que tanto clientes como el equipo de ventas puedan generar cotizaciones completas sin demoras, optimizando el flujo de trabajo y acelerando el ciclo de ventas." // Descripción detallada
  },
  {
    icon: Search,
    title: "Búsqueda Guiada de Refacciones",
    description: "Filtro por categoría, modelo y familia del vehículo, acompañado de ayudas visuales para identificar piezas complejas.",
    badge: "Nuevo",
    imageUrl: "src/shared/assets/hero-image.jpg",
    detailedDescription: "Navega por nuestro extenso catálogo de refacciones con una búsqueda guiada e intuitiva. Filtra fácilmente por categoría, modelo y familia del vehículo. Además, te apoyamos con diagramas y ayudas visuales para que puedas identificar con total seguridad hasta las piezas más complejas."
  },
  {
    icon: FileText,
    title: "Documentos Automáticos",
    description: "Generación inmediata de cotizaciones y órdenes de compra en PDF con opción de descarga o envío directo.",
    badge: "Automatico",
    imageUrl: "src/shared/assets/hero-image.jpg",
    detailedDescription: "Olvídate del papeleo manual. Con un solo clic, el sistema genera documentos profesionales en formato PDF, como cotizaciones y órdenes de compra. Estos documentos pueden ser descargados al instante o enviados directamente a tus clientes por correo electrónico o WhatsApp, agilizando la comunicación."
  },
  {
    icon: ShoppingCart,
    title: "Carrito y Conversión a Orden",
    description: "Convierte fácilmente las cotizaciones en órdenes de compra, reservando inventario y garantizando la disponibilidad.",
    badge: "Eficiente",
    imageUrl: "src/shared/assets/hero-image.jpg",
    detailedDescription: "Nuestro carrito de compras no solo acumula productos, sino que te permite convertir una cotización completa en una orden de compra formal con un solo clic. Al hacerlo, el sistema reserva automáticamente el inventario, garantizando que los productos estarán disponibles para tu cliente cuando los necesite."
  }
];

// 4. Variable para guardar el servicio seleccionado
const selectedService = ref(null);

// 5. Función para abrir el modal
const openModal = (service) => {
  selectedService.value = service;
};

// Función para cerrar el modal (manejando el evento del componente Dialog)
const handleModalClose = (isOpen) => {
  if (!isOpen) {
    selectedService.value = null;
  }
};
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
          class="group hover:shadow-2xl transition-all duration-500 hover:-translate-y-2 border-2 hover:border-[#4ed636]/20 bg-gradient-to-br from-white to-gray-50/50 dark:from-gray-900 dark:to-gray-800/50 cursor-pointer"
          @click="openModal(service)">
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

    <Dialog :open="!!selectedService" @update:open="handleModalClose">
      <DialogContent v-if="selectedService" class="max-w-2xl p-0">
        <img :src="selectedService.imageUrl" :alt="'Imagen de ' + selectedService.title"
          class="w-full h-64 object-cover rounded-t-lg" />

        <DialogHeader class="p-6">
          <DialogTitle
            class="text-3xl font-bold text-transparent bg-gradient-to-r from-[#4ed636] to-[#048044] bg-clip-text mb-2">
            {{ selectedService.title }}
          </DialogTitle>
          <DialogDescription class="text-lg text-muted-foreground leading-relaxed">
            {{ selectedService.detailedDescription }}
          </DialogDescription>
        </DialogHeader>
      </DialogContent>
    </Dialog>
  </section>
</template>
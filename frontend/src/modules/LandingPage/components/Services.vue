<script setup>
import { Card, CardHeader, CardContent } from "@/shared/components/ui/card";
import { Badge } from "@/shared/components/ui/badge";
import { Calculator, Clock, Shield, Zap, Users, TrendingUp } from "lucide-vue-next";

const services = [
  {
    icon: Calculator,
    title: "Cotización Inteligente",
    description: "Sistema avanzado de cotización que encuentra las mejores opciones de refacciones al precio más competitivo del mercado.",
    badge: "Popular"
  },
  {
    icon: Clock,
    title: "Respuesta Rápida",
    description: "Obtén cotizaciones en tiempo real. Nuestro sistema procesa miles de opciones en segundos para darte la mejor propuesta.",
    badge: "Rápido"
  },
  {
    icon: Shield,
    title: "Garantía Asegurada",
    description: "Todas nuestras refacciones cuentan con garantía completa. Tu inversión está protegida con nosotros.",
    badge: "Confiable"
  },
  {
    icon: Zap,
    title: "Automatización Total",
    description: "Proceso completamente automatizado desde la búsqueda hasta la entrega. Sin complicaciones, sin demoras.",
    badge: "Eficiente"
  },
  {
    icon: Users,
    title: "Soporte Especializado",
    description: "Equipo de expertos disponible para asesorarte en cada paso. Atención personalizada cuando la necesites.",
    badge: "24/7"
  },
  {
    icon: TrendingUp,
    title: "Mejores Precios",
    description: "Comparamos precios en tiempo real con múltiples proveedores para garantizarte siempre la mejor oferta disponible.",
    badge: "Ahorro"
  }
];
</script>

<template>
  <section id="services" class="w-[90%] md:w-[70%] lg:w-[75%] lg:max-w-screen-xl mx-auto py-20 md:py-32">
    <div class="text-center mb-16">
      <Badge variant="outline" class="text-sm py-2 mb-6">
        <span class="mr-1 text-primary">
          <Badge class="bg-[#3fc029] font-bold">Servicios</Badge>
        </span>
        <span class="font-bold">Lo que ofrecemos</span>
      </Badge>
      
      <h2 class="text-4xl md:text-5xl font-bold mb-6">
        Servicios que
        <span class="text-transparent bg-gradient-to-r from-[#4ed636] to-[#048044] bg-clip-text">
          transforman
        </span>
        tu experiencia
      </h2>
      
      <p class="text-xl text-muted-foreground max-w-3xl mx-auto">
        Descubre cómo nuestros servicios especializados pueden optimizar tu proceso de cotización 
        y ahorrarte tiempo y dinero en cada compra.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      <Card 
        v-for="service in services" 
        :key="service.title"
        class="group hover:shadow-2xl transition-all duration-500 hover:-translate-y-2 border-2 hover:border-[#4ed636]/20 bg-gradient-to-br from-white to-gray-50/50 dark:from-gray-900 dark:to-gray-800/50"
      >
        <CardHeader class="pb-4">
          <div class="flex items-start justify-between mb-4">
            <div class="p-3 rounded-xl bg-gradient-to-r from-[#4ed636]/10 to-[#09cb6d]/10 group-hover:from-[#4ed636]/20 group-hover:to-[#09cb6d]/20 transition-all duration-300">
              <component :is="service.icon" class="w-8 h-8 text-[#4ed636] group-hover:scale-110 transition-transform duration-300" />
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
  </section>
</template>
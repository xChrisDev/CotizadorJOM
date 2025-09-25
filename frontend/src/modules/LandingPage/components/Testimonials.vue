<script setup>
import { Badge } from "@/shared/components/ui/badge";
import { Card, CardContent } from "@/shared/components/ui/card";
import { Star, Quote } from "lucide-vue-next";

const testimonials = [
  {
    name: "Carlos Mendoza",
    role: "Propietario de Taller Mecánico",
    company: "AutoServicio Mendoza",
    content: "JOM ha revolucionado completamente mi negocio. Antes tardaba horas buscando refacciones y comparando precios. Ahora en minutos tengo las mejores opciones disponibles. Mis clientes están más satisfechos y mi productividad se ha triplicado.",
    rating: 5,
    avatar: new URL("@/shared/assets/user-default.png", import.meta.url).href
  },
  {
    name: "María González",
    role: "Gerente de Compras",
    company: "Distribuidora AutoParts",
    content: "La precisión y rapidez del sistema de cotización de JOM es impresionante. Hemos reducido nuestros costos de operación en un 30% y mejorado significativamente nuestros tiempos de respuesta a clientes. Una herramienta indispensable.",
    rating: 5,
    avatar: new URL("@/shared/assets/user-default.png", import.meta.url).href
  },
  {
    name: "Roberto Silva",
    role: "Mecánico Independiente",
    company: "Taller Silva",
    content: "Como mecánico independiente, necesitaba una solución que me diera acceso a precios competitivos sin las complicaciones de negociar con múltiples proveedores. JOM me ha dado exactamente eso y más. Excelente servicio.",
    rating: 5,
    avatar: new URL("@/shared/assets/user-default.png", import.meta.url).href
  },
  {
    name: "Ana Rodríguez",
    role: "Directora de Operaciones",
    company: "FlotaMax Transportes",
    content: "Gestionar el mantenimiento de nuestra flota de 200+ vehículos era un desafío enorme. Con JOM, hemos optimizado todo el proceso de adquisición de refacciones. El ahorro en tiempo y dinero ha sido extraordinario.",
    rating: 5,
    avatar: new URL("@/shared/assets/user-default.png", import.meta.url).href
  },
  {
    name: "Luis Herrera",
    role: "Propietario",
    company: "AutoRepuestos Herrera",
    content: "La transparencia en los precios y la facilidad de uso de la plataforma JOM nos ha permitido expandir nuestro negocio. Nuestros clientes confían en nosotros porque siempre les ofrecemos las mejores opciones del mercado.",
    rating: 5,
    avatar: new URL("@/shared/assets/user-default.png", import.meta.url).href
  },
  {
    name: "Patricia Morales",
    role: "Jefa de Taller",
    company: "Servicio Integral Morales",
    content: "JOM no solo nos ayuda a encontrar las mejores refacciones, sino que también nos ha permitido brindar un mejor servicio a nuestros clientes. La confianza que genera tener precios justos y productos de calidad es invaluable.",
    rating: 5,
    avatar: new URL("@/shared/assets/user-default.png", import.meta.url).href
  }
];
</script>

<template>
  <section class="py-20 md:py-32 bg-gradient-to-b from-gray-50/50 to-white dark:from-gray-900/50 dark:to-background">
    <div class="w-[90%] md:w-[70%] lg:w-[75%] lg:max-w-screen-xl mx-auto">
      <div class="text-center mb-16">
        <h2 class="text-4xl md:text-5xl font-bold mb-6">
          <span class="text-transparent bg-gradient-to-r from-[#4ed636] to-[#048044] bg-clip-text">
            Testimonios
          </span>
          reales
        </h2>

        <p class="text-xl text-muted-foreground max-w-3xl mx-auto">
          Descubre cómo JOM ha transformado la experiencia de cotización para cientos de
          talleres, mecánicos y distribuidores en todo el país.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <Card v-for="(testimonial, index) in testimonials" :key="index"
          class="group hover:shadow-2xl transition-all duration-500 hover:-translate-y-2 border-2 hover:border-[#4ed636]/20 bg-gradient-to-br from-white to-gray-50/30 dark:from-gray-900 dark:to-gray-800/30 relative overflow-hidden">
          <!-- Icono de comillas decorativo -->
          <div class="absolute top-4 right-4 opacity-10 group-hover:opacity-20 transition-opacity duration-300">
            <Quote class="w-12 h-12 text-[#4ed636]" />
          </div>

          <CardContent class="p-6">
            <!-- Estrellas de rating -->
            <div class="flex items-center gap-1 mb-4">
              <div v-for="star in testimonial.rating" :key="star" class="text-yellow-400">
                <Star class="w-4 h-4 fill-current" />
              </div>
            </div>

            <!-- Contenido del testimonio -->
            <blockquote class="text-muted-foreground mb-6 leading-relaxed italic">
              "{{ testimonial.content }}"
            </blockquote>

            <!-- Información del cliente -->
            <div class="flex items-center gap-4">
              <div class="relative">
                <img :src="testimonial.avatar" :alt="testimonial.name"
                  class="w-12 h-12 rounded-full object-cover border-2 border-[#4ed636]/20 group-hover:border-[#4ed636]/40 transition-all duration-300" />
                <div
                  class="absolute -bottom-1 -right-1 w-4 h-4 bg-[#4ed636] rounded-full border-2 border-white dark:border-gray-900">
                </div>
              </div>
              <div>
                <div class="font-semibold text-foreground group-hover:text-[#048044] transition-colors duration-300">
                  {{ testimonial.name }}
                </div>
                <div class="text-sm text-muted-foreground">
                  {{ testimonial.role }}
                </div>
                <div class="text-xs text-[#4ed636] font-medium">
                  {{ testimonial.company }}
                </div>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <!-- Estadísticas de testimonios -->
      <div class="mt-16 grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
        <div class="group">
          <div class="text-4xl font-bold text-[#4ed636] mb-2 group-hover:scale-110 transition-transform duration-300">
            500+
          </div>
          <div class="text-muted-foreground font-medium">
            Clientes satisfechos
          </div>
        </div>
        <div class="group">
          <div class="text-4xl font-bold text-[#4ed636] mb-2 group-hover:scale-110 transition-transform duration-300">
            4.9/5
          </div>
          <div class="text-muted-foreground font-medium">
            Calificación promedio
          </div>
        </div>
        <div class="group">
          <div class="text-4xl font-bold text-[#4ed636] mb-2 group-hover:scale-110 transition-transform duration-300">
            95%
          </div>
          <div class="text-muted-foreground font-medium">
            Recomiendan JOM
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
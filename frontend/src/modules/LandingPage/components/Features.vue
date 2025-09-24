<script setup>
import { Badge } from "@/shared/components/ui/badge";
import { Card, CardContent } from "@/shared/components/ui/card";
import { 
  Search, 
  BarChart3, 
  Shield, 
  Smartphone, 
  Globe, 
  Headphones,
  CheckCircle,
  ArrowRight
} from "lucide-vue-next";

const features = [
  {
    icon: Search,
    title: "Búsqueda Inteligente",
    description: "Encuentra cualquier refacción con nuestro motor de búsqueda avanzado que comprende marcas, modelos y especificaciones técnicas.",
    benefits: ["Búsqueda por imagen", "Reconocimiento de códigos", "Sugerencias automáticas"]
  },
  {
    icon: BarChart3,
    title: "Análisis de Precios",
    description: "Compara precios en tiempo real de múltiples proveedores y obtén insights detallados sobre tendencias del mercado.",
    benefits: ["Comparación automática", "Alertas de precio", "Historial de cotizaciones"]
  },
  {
    icon: Shield,
    title: "Garantía Total",
    description: "Todas las refacciones incluyen garantía completa y certificación de calidad respaldada por nuestros proveedores verificados.",
    benefits: ["Garantía extendida", "Proveedores certificados", "Soporte post-venta"]
  },
  {
    icon: Smartphone,
    title: "App Móvil",
    description: "Accede a todas las funcionalidades desde tu smartphone. Cotiza, compara y compra desde cualquier lugar.",
    benefits: ["Disponible 24/7", "Sincronización en tiempo real", "Notificaciones push"]
  },
  {
    icon: Globe,
    title: "Cobertura Nacional",
    description: "Red de distribución en todo el país con entregas rápidas y seguimiento en tiempo real de tus pedidos.",
    benefits: ["Entrega express", "Seguimiento GPS", "Cobertura completa"]
  },
  {
    icon: Headphones,
    title: "Soporte Experto",
    description: "Equipo de especialistas disponible para asesorarte en la selección de refacciones y resolver cualquier duda técnica.",
    benefits: ["Chat en vivo", "Asesoría técnica", "Soporte multicanal"]
  }
];
</script>

<template>
  <section class="py-20 md:py-32 bg-gradient-to-b from-white to-gray-50/50 dark:from-background to-gray-900/50">
    <div class="w-[90%] md:w-[70%] lg:w-[75%] lg:max-w-screen-xl mx-auto">
      <div class="text-center mb-16">
        <Badge variant="outline" class="text-sm py-2 mb-6">
          <span class="mr-1 text-primary">
            <Badge class="bg-[#3fc029] font-bold">Características</Badge>
          </span>
          <span class="font-bold">Funcionalidades avanzadas</span>
        </Badge>
        
        <h2 class="text-4xl md:text-5xl font-bold mb-6">
          Tecnología que
          <span class="text-transparent bg-gradient-to-r from-[#4ed636] to-[#048044] bg-clip-text">
            impulsa
          </span>
          tu negocio
        </h2>
        
        <p class="text-xl text-muted-foreground max-w-3xl mx-auto">
          Descubre las características que hacen de JOM la plataforma más completa 
          y eficiente para la cotización de refacciones automotrices.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <Card 
          v-for="(feature, index) in features" 
          :key="index"
          class="group hover:shadow-2xl transition-all duration-500 hover:-translate-y-2 border-2 hover:border-[#4ed636]/20 bg-gradient-to-br from-white to-gray-50/30 dark:from-gray-900 dark:to-gray-800/30 relative overflow-hidden"
        >
          <!-- Efecto de brillo en hover -->
          <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/5 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000"></div>
          
          <CardContent class="p-8 relative">
            <!-- Icono -->
            <div class="mb-6">
              <div class="w-16 h-16 bg-gradient-to-r from-[#4ed636]/10 to-[#09cb6d]/10 rounded-2xl flex items-center justify-center group-hover:from-[#4ed636]/20 group-hover:to-[#09cb6d]/20 transition-all duration-300">
                <component :is="feature.icon" class="w-8 h-8 text-[#4ed636] group-hover:scale-110 transition-transform duration-300" />
              </div>
            </div>

            <!-- Título y descripción -->
            <h3 class="text-xl font-bold text-foreground mb-4 group-hover:text-[#048044] transition-colors duration-300">
              {{ feature.title }}
            </h3>
            
            <p class="text-muted-foreground mb-6 leading-relaxed">
              {{ feature.description }}
            </p>

            <!-- Lista de beneficios -->
            <ul class="space-y-2">
              <li 
                v-for="benefit in feature.benefits" 
                :key="benefit"
                class="flex items-center gap-3 text-sm text-muted-foreground"
              >
                <CheckCircle class="w-4 h-4 text-[#4ed636] flex-shrink-0" />
                <span>{{ benefit }}</span>
              </li>
            </ul>

            <!-- Enlace de acción -->
            <div class="mt-6 pt-4 border-t border-border/50">
              <button class="flex items-center gap-2 text-sm text-[#4ed636] hover:text-[#048044] font-medium group/link transition-colors duration-200">
                Saber más
                <ArrowRight class="w-4 h-4 group-hover/link:translate-x-1 transition-transform duration-200" />
              </button>
            </div>
          </CardContent>
        </Card>
      </div>

      <!-- CTA Section -->
      <div class="mt-20 text-center">
        <Card class="bg-gradient-to-r from-[#4ed636]/5 to-[#09cb6d]/5 border-[#4ed636]/20 max-w-4xl mx-auto">
          <CardContent class="p-12">
            <h3 class="text-3xl font-bold text-foreground mb-4">
              ¿Listo para experimentar todas estas características?
            </h3>
            <p class="text-lg text-muted-foreground mb-8 max-w-2xl mx-auto">
              Únete a cientos de talleres y distribuidores que ya están optimizando 
              su proceso de cotización con JOM.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
              <button class="px-8 py-4 bg-gradient-to-r from-[#4ed636] to-[#09cb6d] text-white font-semibold rounded-lg hover:opacity-90 transition-opacity duration-200 group">
                Comenzar prueba gratuita
                <ArrowRight class="w-5 h-5 ml-2 inline group-hover:translate-x-1 transition-transform" />
              </button>
              <button class="px-8 py-4 border-2 border-[#4ed636]/30 text-[#4ed636] font-semibold rounded-lg hover:bg-[#4ed636]/10 transition-colors duration-200">
                Ver demo en vivo
              </button>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  </section>
</template>
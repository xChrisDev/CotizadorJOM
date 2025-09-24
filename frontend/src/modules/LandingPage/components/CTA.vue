<script setup>
import { Button } from "@/shared/components/ui/button";
import { Card, CardContent } from "@/shared/components/ui/card";
import { ArrowRight, Sparkles, Zap } from "lucide-vue-next";
</script>

<template>
  <section class="py-20 md:py-32 relative overflow-hidden">
    <!-- Fondo con gradiente -->
    <div class="absolute inset-0 bg-gradient-to-br from-[#4ed636]/10 via-[#09cb6d]/5 to-[#048044]/10"></div>
    
    <!-- Elementos decorativos -->
    <div class="absolute top-20 left-10 w-20 h-20 bg-[#4ed636]/20 rounded-full blur-xl animate-pulse"></div>
    <div class="absolute bottom-20 right-10 w-32 h-32 bg-[#09cb6d]/20 rounded-full blur-xl animate-pulse delay-1000"></div>
    
    <div class="w-[90%] md:w-[70%] lg:w-[75%] lg:max-w-screen-xl mx-auto relative">
      <Card class="bg-gradient-to-r from-white/80 to-gray-50/80 dark:from-gray-900/80 dark:to-gray-800/80 backdrop-blur-xl border-2 border-[#4ed636]/20 shadow-2xl">
        <CardContent class="p-12 md:p-16 text-center">
          <!-- Icono decorativo -->
          <div class="flex justify-center mb-8">
            <div class="relative">
              <div class="w-20 h-20 bg-gradient-to-r from-[#4ed636] to-[#09cb6d] rounded-2xl flex items-center justify-center shadow-2xl">
                <Sparkles class="w-10 h-10 text-white" />
              </div>
              <div class="absolute -top-2 -right-2 w-6 h-6 bg-yellow-400 rounded-full flex items-center justify-center">
                <Zap class="w-3 h-3 text-yellow-900" />
              </div>
            </div>
          </div>

          <!-- Título principal -->
          <h2 class="text-4xl md:text-6xl font-bold mb-6">
            Transforma tu negocio
            <span class="text-transparent bg-gradient-to-r from-[#4ed636] to-[#048044] bg-clip-text block mt-2">
              hoy mismo
            </span>
          </h2>

          <!-- Descripción -->
          <p class="text-xl md:text-2xl text-muted-foreground mb-8 max-w-4xl mx-auto leading-relaxed">
            Únete a la revolución digital de las refacciones automotrices. 
            <strong class="text-foreground">Miles de talleres</strong> ya confían en JOM 
            para optimizar sus cotizaciones y <strong class="text-foreground">aumentar sus ganancias</strong>.
          </p>

          <!-- Estadísticas rápidas -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12 max-w-3xl mx-auto">
            <div class="group">
              <div class="text-3xl md:text-4xl font-bold text-[#4ed636] mb-2 group-hover:scale-110 transition-transform duration-300">
                30%
              </div>
              <div class="text-muted-foreground font-medium">
                Ahorro promedio en costos
              </div>
            </div>
            <div class="group">
              <div class="text-3xl md:text-4xl font-bold text-[#4ed636] mb-2 group-hover:scale-110 transition-transform duration-300">
                5min
              </div>
              <div class="text-muted-foreground font-medium">
                Tiempo promedio de cotización
              </div>
            </div>
            <div class="group">
              <div class="text-3xl md:text-4xl font-bold text-[#4ed636] mb-2 group-hover:scale-110 transition-transform duration-300">
                24/7
              </div>
              <div class="text-muted-foreground font-medium">
                Disponibilidad del sistema
              </div>
            </div>
          </div>

          <!-- Botones de acción -->
          <div class="flex flex-col sm:flex-row gap-6 justify-center items-center mb-8">
            <Button 
              size="lg" 
              class="bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90 font-bold text-lg px-12 py-4 group shadow-2xl hover:shadow-3xl transition-all duration-300"
            >
              Comenzar ahora GRATIS
              <ArrowRight class="w-6 h-6 ml-3 group-hover:translate-x-2 transition-transform duration-300" />
            </Button>
            
            <Button 
              variant="outline" 
              size="lg" 
              class="border-2 border-[#4ed636]/30 text-[#4ed636] hover:bg-[#4ed636]/10 font-semibold text-lg px-12 py-4 group"
            >
              Ver demo en vivo
              <span class="ml-3 text-2xl group-hover:scale-125 transition-transform duration-300">🎥</span>
            </Button>
          </div>

          <!-- Garantía y confianza -->
          <div class="flex flex-col sm:flex-row items-center justify-center gap-6 text-sm text-muted-foreground">
            <div class="flex items-center gap-2">
              <div class="w-5 h-5 bg-green-500 rounded-full flex items-center justify-center">
                <span class="text-white text-xs">✓</span>
              </div>
              <span>Prueba gratuita de 30 días</span>
            </div>
            <div class="hidden sm:block w-px h-4 bg-border"></div>
            <div class="flex items-center gap-2">
              <div class="w-5 h-5 bg-green-500 rounded-full flex items-center justify-center">
                <span class="text-white text-xs">✓</span>
              </div>
              <span>Sin compromiso de permanencia</span>
            </div>
            <div class="hidden sm:block w-px h-4 bg-border"></div>
            <div class="flex items-center gap-2">
              <div class="w-5 h-5 bg-green-500 rounded-full flex items-center justify-center">
                <span class="text-white text-xs">✓</span>
              </div>
              <span>Soporte incluido</span>
            </div>
          </div>

          <!-- Urgencia -->
          <div class="mt-8 p-4 bg-gradient-to-r from-yellow-50 to-orange-50 dark:from-yellow-900/20 dark:to-orange-900/20 rounded-xl border border-yellow-200 dark:border-yellow-800">
            <p class="text-sm font-medium text-yellow-800 dark:text-yellow-200">
              🔥 <strong>Oferta limitada:</strong> Los primeros 100 usuarios obtienen 
              <strong>3 meses adicionales GRATIS</strong> en cualquier plan anual.
            </p>
          </div>
        </CardContent>
      </Card>
    </div>
  </section>
</template>
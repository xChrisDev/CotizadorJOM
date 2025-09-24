<script setup>
import { Badge } from "@/shared/components/ui/badge";
import { Button } from "@/shared/components/ui/button";
import { Card, CardContent } from "@/shared/components/ui/card";
import { ArrowRight, Award, Target, Heart, Lightbulb } from "lucide-vue-next";

const values = [
  {
    icon: Award,
    title: "Excelencia",
    description: "Comprometidos con la calidad superior en cada servicio que ofrecemos."
  },
  {
    icon: Target,
    title: "Precisión",
    description: "Cotizaciones exactas y detalladas para tomar las mejores decisiones."
  },
  {
    icon: Heart,
    title: "Confianza",
    description: "Construimos relaciones duraderas basadas en transparencia y honestidad."
  },
  {
    icon: Lightbulb,
    title: "Innovación",
    description: "Tecnología de vanguardia para revolucionar el mercado de refacciones."
  }
];
</script>

<template>
  <section id="about-us" class="w-[90%] md:w-[70%] lg:w-[75%] lg:max-w-screen-xl mx-auto py-20 md:py-32">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
      <!-- Contenido de texto -->
      <div class="space-y-8">
        <div>
          <Badge variant="outline" class="text-sm py-2 mb-6">
            <span class="mr-1 text-primary">
              <Badge class="bg-[#3fc029] font-bold">Nosotros</Badge>
            </span>
            <span class="font-bold">Nuestra historia</span>
          </Badge>
          
          <h2 class="text-4xl md:text-5xl font-bold mb-6">
            Transformando el
            <span class="text-transparent bg-gradient-to-r from-[#4ed636] to-[#048044] bg-clip-text">
              futuro
            </span>
            de las refacciones
          </h2>
          
          <div class="space-y-4 text-lg text-muted-foreground">
            <p>
              En <strong class="text-foreground">JOM</strong>, somos pioneros en revolucionar la industria de refacciones 
              automotrices a través de tecnología innovadora y un servicio excepcional.
            </p>
            <p>
              Fundada con la visión de simplificar y optimizar el proceso de cotización, 
              hemos desarrollado una plataforma que conecta a talleres, mecánicos y distribuidores 
              con las mejores opciones del mercado.
            </p>
            <p>
              Nuestro compromiso es brindar transparencia, eficiencia y los mejores precios, 
              transformando cada transacción en una experiencia satisfactoria y confiable.
            </p>
          </div>
        </div>

        <div class="flex flex-col sm:flex-row gap-4">
          <Button 
            size="lg" 
            class="bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90 font-semibold group"
          >
            Conoce más sobre nosotros
            <ArrowRight class="w-5 h-5 ml-2 group-hover:translate-x-1 transition-transform" />
          </Button>
          <Button variant="outline" size="lg" class="font-semibold">
            Ver nuestros logros
          </Button>
        </div>
      </div>

      <!-- Imagen y estadísticas -->
      <div class="relative">
        <div class="relative group">
          <div class="absolute -top-6 -right-6 w-full h-full bg-gradient-to-r from-[#4ed636]/20 to-[#09cb6d]/20 rounded-2xl blur-xl group-hover:blur-2xl transition-all duration-500"></div>
          <img 
            src="https://images.pexels.com/photos/3807277/pexels-photo-3807277.jpeg?auto=compress&cs=tinysrgb&w=800" 
            alt="Equipo JOM trabajando" 
            class="relative w-full h-96 object-cover rounded-2xl border shadow-2xl group-hover:shadow-3xl transition-all duration-500"
          />
        </div>

        <!-- Estadísticas flotantes -->
        <div class="absolute -bottom-8 -left-8 bg-white dark:bg-gray-900 p-6 rounded-2xl shadow-2xl border">
          <div class="text-3xl font-bold text-[#4ed636]">10,000+</div>
          <div class="text-sm text-muted-foreground font-medium">Cotizaciones realizadas</div>
        </div>

        <div class="absolute -top-8 -right-8 bg-white dark:bg-gray-900 p-6 rounded-2xl shadow-2xl border">
          <div class="text-3xl font-bold text-[#4ed636]">98%</div>
          <div class="text-sm text-muted-foreground font-medium">Satisfacción del cliente</div>
        </div>
      </div>
    </div>

    <!-- Valores -->
    <div class="mt-24">
      <div class="text-center mb-12">
        <h3 class="text-3xl font-bold mb-4">Nuestros Valores</h3>
        <p class="text-lg text-muted-foreground max-w-2xl mx-auto">
          Los principios que guían cada decisión y nos mantienen comprometidos con la excelencia.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <Card 
          v-for="value in values" 
          :key="value.title"
          class="text-center group hover:shadow-xl transition-all duration-300 hover:-translate-y-1 border-2 hover:border-[#4ed636]/20"
        >
          <CardContent class="pt-8 pb-6">
            <div class="mx-auto w-16 h-16 bg-gradient-to-r from-[#4ed636]/10 to-[#09cb6d]/10 rounded-2xl flex items-center justify-center mb-4 group-hover:from-[#4ed636]/20 group-hover:to-[#09cb6d]/20 transition-all duration-300">
              <component :is="value.icon" class="w-8 h-8 text-[#4ed636] group-hover:scale-110 transition-transform duration-300" />
            </div>
            <h4 class="text-xl font-bold mb-3 group-hover:text-[#048044] transition-colors duration-300">
              {{ value.title }}
            </h4>
            <p class="text-muted-foreground text-sm leading-relaxed">
              {{ value.description }}
            </p>
          </CardContent>
        </Card>
      </div>
    </div>
  </section>
</template>
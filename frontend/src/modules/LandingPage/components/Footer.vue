<script setup>
import { Button } from "@/shared/components/ui/button";
import { Separator } from "@/shared/components/ui/separator";
import {
  Facebook,
  Twitter,
  Instagram,
  Linkedin,
  Youtube,
  Mail,
  Phone,
  MapPin,
  ArrowRight
} from "lucide-vue-next";

const quickLinks = [
  { name: "Inicio", href: "#" },
  { name: "Servicios", href: "#services" },
  { name: "Nosotros", href: "#about-us" },
  { name: "Contacto", href: "#contact" }
];

const legal = [
  { name: "Términos y Condiciones", href: "#" },
  { name: "Política de Privacidad", href: "#" },
  { name: "Aviso Legal", href: "#" }
];

const socialLinks = [
  { name: "Facebook", icon: Facebook, href: "https://www.facebook.com/p/JOM-61555701680633/", color: "hover:text-blue-600" },
  { name: "Twitter", icon: Twitter, href: "#", color: "hover:text-blue-400" },
  { name: "Instagram", icon: Instagram, href: "https://www.instagram.com/jom__refaccionaria/", color: "hover:text-pink-600" },
  { name: "LinkedIn", icon: Linkedin, href: "#", color: "hover:text-blue-700" },
  { name: "YouTube", icon: Youtube, href: "#", color: "hover:text-red-600" }
];

const currentYear = new Date().getFullYear();
</script>

<template>
  <footer class="bg-gradient-to-b from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-950 border-t">
    <!-- Sección principal del footer -->
    <div class="w-[90%] md:w-[70%] lg:w-[75%] lg:max-w-screen-xl mx-auto pt-16">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-12">

        <!-- Información de la empresa -->
        <div class="lg:col-span-1 space-y-6">
          <div class="flex items-center gap-3">
            <img src="@/shared/assets/JOM.png" alt="JOM" class="h-16 w-16" />
            <span class="text-2xl font-bold text-foreground">JOM</span>
          </div>

          <p class="text-muted-foreground leading-relaxed">
            Revolucionando la industria de refacciones automotrices con tecnología
            innovadora y el mejor servicio al cliente.
          </p>

          <!-- Información de contacto rápida -->
          <div class="space-y-3">
            <div class="flex items-center gap-3 text-sm text-muted-foreground">
              <MapPin class="w-4 h-4 text-[#4ed636]" />
              <span>Calle Fray Servando T. de M. Ote. 211,<br> Barrio Alto,
                99070 Fresnillo, Zac.</span>
            </div>
            <div class="flex items-center gap-3 text-sm text-muted-foreground">
              <Phone class="w-4 h-4 text-[#4ed636]" />
              <span>+52 449 264 0046</span>
            </div>
            <div class="flex items-center gap-3 text-sm text-muted-foreground">
              <Mail class="w-4 h-4 text-[#4ed636]" />
              <span>contacto@jom.com</span>
            </div>
          </div>

          <!-- Redes sociales -->
          <div class="flex items-center gap-3">
            <a v-for="social in socialLinks" :key="social.name" :href="social.href" target="_blank"
              class="p-2 rounded-lg bg-white dark:bg-gray-800 border hover:border-[#4ed636]/30 transition-all duration-300 hover:-translate-y-1 hover:shadow-lg group"
              :class="social.color">
              <component :is="social.icon"
                class="w-5 h-5 text-muted-foreground group-hover:scale-110 transition-all duration-300" />
            </a>
          </div>
        </div>

        <!-- Enlaces rápidos y Legal -->
        <div class="flex flex-col gap-10 space-y-2">
          <div>
            <h3 class="text-lg font-semibold text-foreground">Enlaces Rápidos</h3>
            <ul class="space-y-3 mt-4 grid grid-cols-2">
              <li v-for="link in quickLinks" :key="link.name">
                <a :href="link.href"
                  class="text-base text-muted-foreground hover:text-[#4ed636] transition-colors duration-200">
                  {{ link.name }}
                </a>
              </li>
            </ul>
          </div>
          <div>
            <h3 class="text-lg font-semibold text-foreground">Legal</h3>
            <ul class="space-y-3 mt-4">
              <li v-for="item in legal" :key="item.name">
                <a :href="item.href"
                  class="text-base text-muted-foreground hover:text-[#4ed636] transition-colors duration-200">
                  {{ item.name }}
                </a>
              </li>
            </ul>
          </div>
        </div>

        <!-- Newsletter  -->
        <div class="space-y-6">
          <h3 class="text-lg font-semibold text-foreground">Mantente Informado</h3>
          <p class="text-sm text-muted-foreground">
            Suscríbete para recibir las últimas noticias y ofertas especiales.
          </p>

          <!-- Newsletter form -->
          <div class="space-y-3">
            <div class="flex gap-2">
              <input type="email" placeholder="tu@email.com"
                class="flex-1 px-3 py-2 text-sm rounded-lg border border-input bg-background text-foreground placeholder:text-muted-foreground focus:border-[#4ed636] focus:ring-2 focus:ring-[#4ed636]/20 transition-all duration-200" />
              <Button size="sm" class="bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90">
                <Mail class="w-4 h-4" />
              </Button>
            </div>
            <p class="text-xs text-muted-foreground">
              No spam. Puedes cancelar en cualquier momento.
            </p>
          </div>
        </div>
      </div>
    </div>

    <Separator class="opacity-20" />

    <!-- Copyright y enlaces adicionales -->
    <div class="w-[90%] md:w-[70%] lg:w-[75%] lg:max-w-screen-xl mx-auto py-8">
      <div class="flex flex-col md:flex-row justify-between items-center gap-4">
        <div class="text-sm text-muted-foreground text-center md:text-left">
          © {{ currentYear }} JOM. Todos los derechos reservados.
        </div>

        <div class="lg:flex hidden items-center gap-6 text-sm text-muted-foreground">
          <span class="flex items-center gap-2">
            Hecho con
            <span class="text-red-500">❤️</span>
            en Fresnillo, Zacatecas
          </span>
          <span class="hidden md:block">|</span>
          <span class="text-[#4ed636] font-medium">
            Versión 0.1
          </span>
        </div>
      </div>
    </div>
  </footer>
</template>
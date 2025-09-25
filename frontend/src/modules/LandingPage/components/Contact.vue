<script setup>
import { ref } from 'vue';
import { Badge } from "@/shared/components/ui/badge";
import { Button } from "@/shared/components/ui/button";
import { Card, CardHeader, CardContent } from "@/shared/components/ui/card";
import { MapPin, Phone, Mail, Clock, Send, MessageCircle } from "lucide-vue-next";
import Map from './Map.vue';

// Formulario reactivo
const form = ref({
  name: '',
  email: '',
  phone: '',
  company: '',
  message: ''
});

const isSubmitting = ref(false);

const handleSubmit = async () => {
  isSubmitting.value = true;

  console.log('Formulario enviado:', form.value);

  // Reset form
  form.value = {
    name: '',
    email: '',
    phone: '',
    company: '',
    message: ''
  };

  isSubmitting.value = false;
  alert('¡Mensaje enviado correctamente! Te contactaremos pronto.');
};

const contactInfo = [
  {
    icon: MapPin,
    title: "Ubicación",
    content: "Calle Fray Servando T. de M. Ote. 211, Barrio Alto,\n 99070 Fresnillo, Zac.",
    action: "Ver en mapa"
  },
  {
    icon: Phone,
    title: "Teléfono",
    content: "+52 449 264 0046\n+52 449 264 0046",
    action: "Llamar ahora"
  },
  {
    icon: Mail,
    title: "Email",
    content: "contacto@jom.com\nventas@jom.com",
    action: "Enviar email"
  },
  {
    icon: Clock,
    title: "Horarios",
    content: "Lunes a Viernes:\n 9:00 - 19:00\nSábados:\n 9:00 - 15:00",
    action: "Ver disponibilidad"
  }
];
</script>

<template>
  <section id="contact" class="py-56 lg:p-32">
    <div class="w-[90%] md:w-[70%] lg:w-[75%] lg:max-w-screen-xl mx-auto">
      <div class="text-center mb-16">
        <h2 class="text-4xl md:text-5xl font-bold mb-6">
          ¿Listo para
          <span class="text-transparent bg-gradient-to-r from-[#4ed636] to-[#048044] bg-clip-text">
            comenzar?
          </span>
        </h2>

        <p class="text-xl text-muted-foreground max-w-3xl mx-auto">
          Estamos aquí para ayudarte. Contáctanos y descubre cómo JOM puede
          transformar tu proceso de cotización de refacciones.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-16">
        <!-- Información de contacto -->
        <div class="space-y-8">
          <div>
            <h3 class="text-2xl font-bold mb-6">Información de Contacto</h3>
            <p class="text-muted-foreground mb-8 leading-relaxed">
              Nuestro equipo de expertos está disponible para resolver todas tus dudas
              y ayudarte a implementar la mejor solución para tu negocio.
            </p>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <Card v-for="info in contactInfo" :key="info.title"
              class="group hover:shadow-xl transition-all duration-300 hover:-translate-y-1 border-2 hover:border-[#4ed636]/20 cursor-pointer">
              <CardContent class="p-6">
                <div class="flex items-start gap-4">
                  <div
                    class="p-3 rounded-xl bg-gradient-to-r from-[#4ed636]/10 to-[#09cb6d]/10 group-hover:from-[#4ed636]/20 group-hover:to-[#09cb6d]/20 transition-all duration-300">
                    <component :is="info.icon"
                      class="w-6 h-6 text-[#4ed636] group-hover:scale-110 transition-transform duration-300" />
                  </div>
                  <div class="flex-1">
                    <h4
                      class="font-semibold text-foreground mb-2 group-hover:text-[#048044] transition-colors duration-300">
                      {{ info.title }}
                    </h4>
                    <p class="text-sm text-muted-foreground whitespace-pre-line mb-3">
                      {{ info.content }}
                    </p>
                    <button
                      class="text-xs text-[#4ed636] font-medium hover:text-[#048044] transition-colors duration-200">
                      {{ info.action }} →
                    </button>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>

        <!-- Formulario de contacto -->
        <Card class="shadow-2xl border-2 hover:border-[#4ed636]/20 transition-all duration-300">
          <CardHeader>
            <h3 class="text-2xl font-bold text-center">Envíanos un mensaje</h3>
            <p class="text-muted-foreground text-center">
              Completa el formulario y te contactaremos en menos de 24 horas
            </p>
          </CardHeader>
          <CardContent>
            <form @submit.prevent="handleSubmit" class="space-y-6">
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div class="space-y-2">
                  <label class="text-sm font-medium text-foreground">
                    Nombre completo *
                  </label>
                  <input v-model="form.name" type="text" required
                    class="w-full px-4 py-3 rounded-lg border border-input bg-background text-foreground placeholder:text-muted-foreground focus:border-[#4ed636] focus:ring-2 focus:ring-[#4ed636]/20 transition-all duration-200"
                    placeholder="Tu nombre" />
                </div>
                <div class="space-y-2">
                  <label class="text-sm font-medium text-foreground">
                    Teléfono
                  </label>
                  <input v-model="form.phone" type="tel"
                    class="w-full px-4 py-3 rounded-lg border border-input bg-background text-foreground placeholder:text-muted-foreground focus:border-[#4ed636] focus:ring-2 focus:ring-[#4ed636]/20 transition-all duration-200"
                    placeholder="+52 (55) 1234-5678" />
                </div>
              </div>

              <div class="space-y-2">
                <label class="text-sm font-medium text-foreground">
                  Mensaje *
                </label>
                <textarea v-model="form.message" required rows="8"
                  class="w-full px-4 py-3 rounded-lg border border-input bg-background text-foreground placeholder:text-muted-foreground focus:border-[#4ed636] focus:ring-2 focus:ring-[#4ed636]/20 transition-all duration-200 resize-none"
                  placeholder="Cuéntanos cómo podemos ayudarte..."></textarea>
              </div>

              <Button type="submit" :disabled="isSubmitting"
                class="w-full bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90 font-semibold py-3 group">
                <template v-if="isSubmitting">
                  <div class="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin mr-2"></div>
                  Enviando...
                </template>
                <template v-else>
                  Enviar mensaje
                  <Send class="w-5 h-5 ml-2 group-hover:translate-x-1 transition-transform" />
                </template>
              </Button>

              <p class="text-xs text-muted-foreground text-center">
                Al enviar este formulario, aceptas nuestros términos de privacidad y
                el procesamiento de tus datos personales.
              </p>
            </form>
          </CardContent>
        </Card>
      </div>
    </div>
  </section>
  <Map />
</template>
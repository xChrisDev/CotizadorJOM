<script setup>
import { Card, CardContent, CardHeader, CardTitle } from '@/shared/components/ui/card'
import { Button } from '@/shared/components/ui/button'
import { Mail, MessageCircle, FileDown, Printer, LogOut } from 'lucide-vue-next'
import { useRouter } from 'vue-router'

const emit = defineEmits(['send-email', 'send-whatsapp', 'download-pdf', 'print-pdf'])
const router = useRouter()

defineProps({
  showConvertButton: {
    type: Boolean,
    default: true
  }
})

const goBack = () => {
  router.push('/admin')
}
</script>

<template>
  <Card
    class="shadow-lg rounded-2xl border w-full border-gray-100 bg-white/80 dark:bg-slate-900/80 backdrop-blur-sm transition-all">
    <div class="px-6">
      <h1 class="text-2xl md:text-4xl font-bold">Cotización Generada</h1>
      <p class="text-muted-foreground mt-1">
        Seleccione las opciones que desea realizar
      </p>
    </div>
    <CardContent class="flex flex-col lg:flex-row gap-3 justify-between">
      <div class="flex flex-col lg:flex-row gap-3">
        <Button variant="default" class="bg-blue-500 hover:bg-blue-600 text-white shadow-sm transition-all"
          @click.prevent="emit('send-email')">
          <Mail class="w-5 h-5" />
          Enviar por correo
        </Button>

        <Button variant="default" class="bg-green-500 hover:bg-green-600 text-white shadow-sm transition-all"
          @click.prevent="emit('send-whatsapp')">
          <MessageCircle class="w-5 h-5" />
          Enviar por WhatsApp
        </Button>
        <Button variant="default" class="bg-red-500 hover:bg-red-600 text-white shadow-sm transition-all"
          @click.prevent="emit('download-pdf')">
          <FileDown class="w-5 h-5" />
          Descargar PDF
        </Button>

        <Button variant="default" class="bg-slate-600 hover:bg-slate-700 text-white shadow-sm transition-all"
          @click.prevent="emit('print-pdf')">
          <Printer class="w-5 h-5" />
          Imprimir PDF
        </Button>
      </div>

      <Button variant="outline"
        class="border-gray-300 dark:border-gray-700 hover:bg-gray-100 dark:hover:bg-gray-800 transition-all"
        @click="goBack">
        <LogOut class="w-5 h-5 text-gray-700 dark:text-gray-300" />
        Volver al cotizador
      </Button>
    </CardContent>
  </Card>
</template>

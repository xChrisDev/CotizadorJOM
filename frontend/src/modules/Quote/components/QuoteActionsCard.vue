<script setup>
import { Card, CardContent, CardHeader, CardTitle } from '@/shared/components/ui/card';
import { Button } from '@/shared/components/ui/button';
import { Separator } from '@/shared/components/ui/separator';
import { Mail, MessageCircle, FileDown, ShoppingCart } from 'lucide-vue-next';

const emit = defineEmits(['send-email', 'send-whatsapp', 'download-pdf', 'convert-to-order']);

defineProps({
  showConvertButton: {
    type: Boolean,
    default: true
  }
});
</script>

<template>
  <Card>
    <CardHeader>
      <CardTitle>{{ showConvertButton ? 'Acciones de cotización' : 'Acciones de orden de compra' }}</CardTitle>
    </CardHeader>
    <CardContent class="space-y-3">
      <Button variant="outline" class="w-full justify-start" @click="emit('send-email')">
        <Mail class="w-4 h-4 mr-2" />
        {{ showConvertButton ? 'Enviar por Correo' : 'Imprimir Orden' }}
      </Button>
      <Button variant="outline" class="w-full justify-start" @click="emit('send-whatsapp')">
        <MessageCircle class="w-4 h-4 mr-2" />
        Enviar por WhatsApp
      </Button>
      <Button variant="outline" class="w-full justify-start" @click="emit('download-pdf')">
        <FileDown class="w-4 h-4 mr-2" />
        Descargar PDF
      </Button>
      <template v-if="showConvertButton">
        <Separator />
        <Button class="w-full bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90"
          @click="emit('convert-to-order')">
          <ShoppingCart class="w-4 h-4 mr-2" />
          Convertir en orden de compra
        </Button>
      </template>
    </CardContent>
  </Card>
</template>
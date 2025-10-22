<script setup>
import { ref, watch } from 'vue'
import { Card, CardContent, CardHeader, CardTitle } from '@/shared/components/ui/card'
import { UserCircle, Mail, Phone } from 'lucide-vue-next'

const props = defineProps({
  client: {
    type: Object,
    required: true,
    default: () => ({})
  },
  isLoading: {
    type: Boolean,
    default: false
  }
})
</script>

<template>
  <Card>
    <CardHeader>
      <CardTitle class="text-lg flex items-center gap-2">
        <UserCircle class="w-5 h-5" /> Detalles del Cliente
      </CardTitle>
    </CardHeader>

    <CardContent>
      <div v-if="isLoading" class="flex flex-col items-center justify-center h-full text-center text-muted-foreground">
        <div class="w-12 h-12 border-4 border-gray-300 border-t-green-500 rounded-full animate-spin mb-2"></div>
        <p class="text-sm font-semibold">Cargando cliente...</p>
      </div>

      <div v-else-if="client.id" class="space-y-4">
        <div class="flex flex-col">
          <div class="flex items-center gap-1">
            <UserCircle class="w-4 h-4 text-muted-foreground" />
            <p class="text-sm text-muted-foreground">Nombre:</p>
          </div>
          <p class="font-semibold">{{ client.first_name }} {{ client.last_name }}</p>
        </div>

        <div class="flex flex-col">
          <div class="flex items-center gap-1">
            <Mail class="w-4 h-4 text-muted-foreground" />
            <p class="text-sm text-muted-foreground">Email:</p>
          </div>
          <p class="font-semibold break-all">{{ client.email }}</p>
        </div>

        <div class="flex flex-col">
          <div class="flex items-center gap-1">
            <Phone class="w-4 h-4 text-muted-foreground" />
            <p class="text-sm text-muted-foreground">Teléfono:</p>
          </div>
          <p class="font-semibold">{{ client.phone_number }}</p>
        </div>
      </div>

      <div v-else class="flex flex-col items-center justify-center h-full text-center text-muted-foreground">
        <UserCircle class="w-12 h-12 mb-2" />
        <h3 class="text-base font-semibold">No seleccionado</h3>
        <p class="text-sm">¡Selecciona un cliente para continuar!</p>
      </div>
    </CardContent>
  </Card>
</template>

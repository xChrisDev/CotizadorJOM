<script setup>
import { Card, CardContent, CardHeader, CardTitle } from '@/shared/components/ui/card';

defineProps({
  client: {
    type: Object,
    required: true
  }
});
</script>

<template>
  <Card>
    <CardHeader>
      <CardTitle>Detalles del Cliente</CardTitle>
    </CardHeader>
    <CardContent class="space-y-3">
      <div>
        <p class="text-sm text-muted-foreground">Nombre:</p>
        <p class="font-semibold">{{ client.name }}</p>
      </div>
      <div>
        <p class="text-sm text-muted-foreground">Email:</p>
        <p class="font-medium text-sm break-all">{{ client.email }}</p>
      </div>
      <div>
        <p class="text-sm text-muted-foreground">Teléfono:</p>
        <p class="font-medium">{{ client.phone }}</p>
      </div>
    </CardContent>
  </Card>
</template>
<script setup>
import { Card, CardContent, CardHeader, CardTitle } from '@/shared/components/ui/card';
import { Separator } from '@/shared/components/ui/separator';
import { Badge } from '@/shared/components/ui/badge';

defineProps({
  orderNumber: {
    type: String,
    required: true
  },
  date: {
    type: String,
    required: true
  },
  status: {
    type: String,
    required: true
  },
  total: {
    type: Number,
    required: true
  }
});
</script>

<template>
  <Card>
    <CardHeader>
      <CardTitle>Resumen de la Orden</CardTitle>
    </CardHeader>
    <CardContent class="space-y-4">
      <div>
        <p class="text-sm text-muted-foreground">Número de Orden:</p>
        <p class="font-semibold font-mono">{{ orderNumber }}</p>
      </div>
      <div>
        <p class="text-sm text-muted-foreground">Fecha:</p>
        <p class="font-semibold">{{ date }}</p>
      </div>
      <div>
        <p class="text-sm text-muted-foreground">Estado:</p>
        <Badge variant="secondary" class="bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-100">
          {{ status }}
        </Badge>
      </div>

      <Separator />

      <div class="space-y-2">
        <div class="flex justify-between text-lg pt-2">
          <span class="font-bold">Total:</span>
          <span class="font-bold text-xl">${{ total.toFixed(2) }}</span>
        </div>
      </div>
    </CardContent>
  </Card>
</template>
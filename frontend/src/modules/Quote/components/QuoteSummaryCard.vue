<script setup>
import { Card, CardContent, CardHeader, CardTitle } from '@/shared/components/ui/card';
import { Separator } from '@/shared/components/ui/separator';
import { Badge } from '@/shared/components/ui/badge';
import { Calendar, Clock, CheckCircle } from 'lucide-vue-next';

const props = defineProps({
  dueDate: { type: String, required: true },
  date: { type: String, required: true },
  status: { type: String, required: true },
  total: { type: Number, required: true }
});

const IVA_RATE = 0.16

</script>

<template>
  <Card>
    <CardHeader>
      <CardTitle class="text-lg flex items-center gap-2">
        <Calendar class="w-5 h-5" /> Resumen
      </CardTitle>
    </CardHeader>

    <CardContent class="space-y-4">
      <div class="flex items-center gap-2">
        <Calendar class="w-4 h-4 text-muted-foreground" />
        <p class="text-sm text-muted-foreground">Fecha de generación:</p>
        <p class="font-semibold">{{ date }}</p>
      </div>

      <div class="flex items-center gap-2">
        <Clock class="w-4 h-4 text-muted-foreground" />
        <p class="text-sm text-muted-foreground">Fecha de vencimiento:</p>
        <p class="font-semibold">{{ dueDate }}</p>
      </div>

      <div class="flex items-center gap-2">
        <CheckCircle class="w-4 h-4 text-muted-foreground" />
        <p class="text-sm text-muted-foreground">Estado:</p>
        <Badge :class="{
          'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-100': status === 'Pagado',
          'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-100': status === 'Pendiente',
          'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-100': status === 'Vencido'
        }">
          {{ status }}
        </Badge>
      </div>

      <Separator />

      <div class="space-y-1">
        <div class="flex justify-between text-sm">
          <span>Subtotal:</span>
          <span>${{ (total / (1 + IVA_RATE)).toFixed(2) }}</span>
        </div>
        <div class="flex justify-between text-sm">
          <span>IVA (16%):</span>
          <span>${{ (total - (total / (1 + IVA_RATE))).toFixed(2) }}</span>
        </div>
        <div class="flex justify-between text-lg font-bold pt-1">
          <span>Total:</span>
          <span>${{ total.toFixed(2) }}</span>
        </div>
      </div>
    </CardContent>
  </Card>
</template>

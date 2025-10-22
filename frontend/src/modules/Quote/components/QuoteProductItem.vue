<script setup>
import { Badge } from '@/shared/components/ui/badge';
import placeholderImage from '@/shared/assets/default-image.jpg';

defineProps({
  product: {
    type: Object,
    required: true
  },
  price: {
    type: Number,
    required: true
  }
});
</script>

<template>
  <div class="flex flex-col sm:flex-row gap-4 p-4 border rounded-lg hover:bg-accent/5 transition-colors">
    <img :src="product.imageUrl || placeholderImage" :alt="product.name"
      class="w-full sm:w-24 h-32 sm:h-24 object-cover rounded-md" />
    <div class="flex-grow space-y-2">
      <div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-2">
        <div>
          <Badge variant="outline" class="mb-2">{{ product.brand.name }}</Badge>
          <h4 class="font-semibold">{{ product.article_name }}</h4>
          <p class="text-sm text-muted-foreground"><span class="font-semibold">SKU:</span> {{ product.item_code }}</p>
        </div>
        <div class="text-right">
          <p class="font-bold text-lg">${{ (price * product.quantity).toFixed(2) }}</p>
        </div>
      </div>
      <div class="flex items-center justify-between text-sm pt-2 border-t">
        <span class="text-muted-foreground">Cantidad: <span class="font-medium text-foreground">{{
          product.quantity }}</span></span>
        <span class="text-muted-foreground">Precio unitario: <span class="font-medium text-foreground">${{
          price.toFixed(2) }}</span></span>
      </div>
    </div>
  </div>
</template>
<script setup>
import { Card, CardContent, CardFooter, CardHeader } from '@/shared/components/ui/card';
import { Button } from '@/shared/components/ui/button';
import { Input } from '@/shared/components/ui/input';
import { Star, Plus, Minus, PackagePlusIcon, XCircle } from 'lucide-vue-next';
import Badge from '@/shared/components/ui/badge/Badge.vue';
import placeholderImage from '@/shared/assets/default-image.jpg';
import { ref, computed } from 'vue';
import { useCartStore } from '../stores/cart.js';

const cartStore = useCartStore();
const props = defineProps({
  product: {
    type: Object,
    required: true,
    default: () => ({
      id: 'default-id',
      name: 'Nombre del Producto',
      brand: 'Marca',
      rating: 4,
      reviews: 0,
      price: 0.00,
      oldPrice: null,
      imageUrl: null,
      stock: 1
    })
  }
});

const productAmount = ref(1);

const isOutOfStock = computed(() => props.product.stock === 0);

function increment() {
  if (props.product.stock && productAmount.value >= props.product.stock) return;
  productAmount.value++;
}

function decrement() {
  if (productAmount.value > 1) {
    productAmount.value--;
  }
}

function handleAddToCart() {
  cartStore.addToCart(props.product, productAmount.value);
//   alert(`${productAmount.value} x ${props.product.name} fue(ron) agregado(s) al carrito.`);
  productAmount.value = 1; // Reseteamos la cantidad
}
</script>

<template>
  <Card class="overflow-hidden flex flex-col">
    <CardHeader class="p-4">
      <img :src="product.imageUrl || placeholderImage" :alt="product.name" class="w-full rounded-lg h-48 object-cover" />
    </CardHeader>
    <CardContent class="p-4 space-y-2 flex-grow min-h-[216px]">
      <Badge variant="outline">{{ product.brand }}</Badge>
      <h4 class="font-semibold h-12 line-clamp-2">{{ product.name }}</h4>
      <div class="flex items-center gap-1">
        <Star v-for="i in 5" :key="i" class="w-4 h-4"
          :class="i <= product.rating ? 'text-yellow-400 fill-yellow-400' : 'text-gray-300'" />
        <span class="text-xs text-muted-foreground ml-1">({{ product.reviews }})</span>
      </div>
      <div class="flex items-baseline gap-2">
        <p class="text-2xl font-bold">${{ product.price.toFixed(2) }}</p>
        <del v-if="product.oldPrice" class="text-muted-foreground">${{ product.oldPrice.toFixed(2) }}</del>
      </div>
    </CardContent>
    <CardFooter class="p-4 flex-col items-stretch gap-2">
      <div class="w-full flex">
        <Button variant="outline" size="icon" class="h-9 w-9" @click="decrement" :disabled="isOutOfStock">
          <Minus class="w-4 h-4" />
        </Button>
        <Input type="number" min="1" :max="product.stock" v-model.number="productAmount" class="h-9 text-center mx-1" :disabled="isOutOfStock" />
        <Button variant="outline" size="icon" class="h-9 w-9" @click="increment" :disabled="isOutOfStock">
          <Plus class="w-4 h-4" />
        </Button>
      </div>
      <Button 
        size="lg"
        @click="handleAddToCart"
        :disabled="isOutOfStock"
        class="bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90 disabled:opacity-50 disabled:bg-gray-500"
      >
        <XCircle v-if="isOutOfStock" class="size-5 mr-2" />
        <PackagePlusIcon v-else class="size-5 mr-2" />
        <span>{{ isOutOfStock ? 'Agotado' : 'Agregar al carrito' }}</span>
      </Button>
    </CardFooter>
  </Card>
</template>
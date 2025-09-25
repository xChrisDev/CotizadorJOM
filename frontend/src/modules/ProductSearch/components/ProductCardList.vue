<script setup>
import { Card } from '@/shared/components/ui/card';
import { Badge } from '@/shared/components/ui/badge';
import { Button } from '@/shared/components/ui/button';
import { Input } from '@/shared/components/ui/input';
import { Star, Plus, Minus, PackagePlusIcon } from 'lucide-vue-next';
import placeholderImage from '@/shared/assets/default-image.jpg';
import { ref } from 'vue';
import { useCartStore } from '../stores/cart.js';

const cartStore = useCartStore();

const props = defineProps({
    product: {
        type: Object,
        required: true
    }
});
const productAmount = ref(1);
function increment() {
    productAmount.value++;
}

function decrement() {
    if (productAmount.value > 1) {
        productAmount.value--;
    }
}
</script>

<template>
    <Card class="flex flex-col md:flex-row items-center p-4 gap-4 w-full">

        <img :src="placeholderImage" :alt="product.name" class="w-full md:w-24 h-36 md:h-24 object-cover rounded-md" />


        <div class="flex flex-col justify-between flex-grow h-full w-full md:w-auto">
            <div>
                <div class="flex gap-2 items-center">
                    <Badge variant="outline">{{ product.brand }}</Badge>
                    <h4 class="text-md font-semibold mt-2">{{ product.name }}</h4>
                </div>
                <div class="flex items-center gap-1 mt-2">
                    <Star v-for="i in 5" :key="i" class="w-3 h-3"
                        :class="i <= product.rating ? 'text-yellow-400 fill-yellow-400' : 'text-gray-300'" />
                    <span class="text-xs text-muted-foreground ml-1">({{ product.reviews }} reseñas)</span>
                </div>
            </div>
            <div class="flex items-baseline gap-2 mt-4">
                <p class="text-lg font-bold">${{ product.price.toFixed(2) }}</p>
                <del v-if="product.oldPrice" class="text-muted-foreground">${{ product.oldPrice.toFixed(2) }}</del>
            </div>
        </div>

        <div class="flex-shrink-0 w-full md:w-48 flex flex-col items-stretch justify-center gap-2 mt-4 md:mt-0">
            <div class="w-full flex">
                <Button variant="outline" size="icon" class="h-9 w-9" @click="decrement">
                    <Minus class="w-4 h-4" />
                </Button>
                <Input type="text" readonly min="1" v-model="productAmount" class="h-9 text-center mx-1" />
                <Button variant="outline" size="icon" class="h-9 w-9" @click="increment">
                    <Plus class="w-4 h-4" />
                </Button>
            </div>
            <Button @click="cartStore.addToCart(product, productAmount);"
                class="w-full bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90 disabled:opacity-50 disabled:bg-gray-500">
                <PackagePlusIcon class="size-5 mr-2" />
                <span>Agregar</span>
            </Button>
        </div>
    </Card>
</template>
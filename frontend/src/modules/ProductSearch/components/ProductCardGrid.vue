<script setup>
import { Card, CardContent, CardFooter, CardHeader } from '@/shared/components/ui/card';
import { Button } from '@/shared/components/ui/button';
import { Input } from '@/shared/components/ui/input';
import { Star, Plus, Minus, PackagePlusIcon, XCircle } from 'lucide-vue-next';
import Badge from '@/shared/components/ui/badge/Badge.vue';
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
    <Card class="overflow-hidden">
        <CardHeader class="px-4">
            <img :src="placeholderImage" :alt="product.name" class="w-full rounded-lg h-48 object-cover" />
        </CardHeader>
        <CardContent class="space-y-2">
            <Badge variant="outline">{{ product.brand }}</Badge>
            <h4 class="font-semibold h-12">{{ product.name }}</h4>
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
        <CardFooter class="px-4 flex-col items-stretch gap-2">
            <div class="w-full flex justify-center items-center gap-2">
                <div class="w-1/2 flex">
                    <Button variant="outline" size="icon" class="h-9 w-9" @click="decrement">
                        <Minus class="w-4 h-4" />
                    </Button>
                    <Input type="text" readonly min="1" v-model="productAmount" class="h-9 text-center mx-1" />
                    <Button variant="outline" size="icon" class="h-9 w-9" @click="increment">
                        <Plus class="w-4 h-4" />
                    </Button>
                </div>
                <Button size="lg" @click="cartStore.addToCart(product, productAmount);"
                    class="bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90 disabled:opacity-50 disabled:bg-gray-500">
                    <PackagePlusIcon class="size-5 mr-2" />
                    <span>Agregar</span>
                </Button>
            </div>
        </CardFooter>
    </Card>
</template>
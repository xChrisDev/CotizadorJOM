<script setup>
import { Button } from '@/shared/components/ui/button';
import { Plus, Minus, Trash2 } from 'lucide-vue-next';
import placeholderImage from '@/shared/assets/default-image.jpg';

import { useCartStore } from '../stores/cart.js';

const cartStore = useCartStore();

defineProps({
    item: {
        type: Object,
        required: true,
    }
});
</script>

<template>
    <div class="flex items-center gap-4 p-2">
        <img :src="item.imageUrl || placeholderImage" :alt="item.name" class="h-16 w-16 rounded-md object-cover" />
        <div class="flex-grow">
            <p class="font-semibold line-clamp-1">{{ item.name }}</p>
            <p class="text-sm text-muted-foreground">${{ item.price.toFixed(2) }}</p>
        </div>
        <div class="flex items-center gap-2">
            <Button variant="outline" size="icon" class="h-8 w-8"
                @click="cartStore.updateQuantity(item.id, item.quantity - 1)">
                <Minus class="h-8 w-8" />
            </Button>
            <span class="w-6 text-center font-medium">{{ item.quantity }}</span>
            <Button variant="outline" size="icon" class="h-8 w-8"
                @click="cartStore.updateQuantity(item.id, item.quantity + 1)">
                <Plus class="h-8 w-8" />
            </Button>
        </div>
        <Button variant="destructive" size="icon" class="h-8 w-8 text-white hover:opacity-80"
            @click="cartStore.removeFromCart(item.id)">
            <Trash2 class="h-8 w-8" />
        </Button>
    </div>
</template>
<script setup>
import { Button } from '@/shared/components/ui/button'
import { Plus, Minus, Trash2 } from 'lucide-vue-next'
import placeholderImage from '@/shared/assets/default-image.jpg'
import { useCartStore } from '../stores/cart.js'

const cartStore = useCartStore()

defineProps({
    item: {
        type: Object,
        required: true
    }
})
</script>

<template>
    <div class="flex items-center gap-4 p-3 rounded-xl border bg-white dark:bg-[#27272a] shadow-sm">
        <img :src="item.imageUrl || placeholderImage" :alt="item.article_name"
            class="h-16 w-16 rounded-lg object-cover border" />

        <div class="flex flex-col flex-1 justify-between">
            <p class="font-semibold  leading-tight line-clamp-2">
                {{ item.article_name }}
            </p>

            <div class="flex items-center justify-between mt-2">
                <div class="flex items-center gap-2">
                    <Button variant="outline" size="icon" class="h-8 w-8 border dark:border-white"
                        :disabled="item.quantity <= 1" @click="cartStore.updateQuantity(item.id, item.quantity - 1)">
                        <Minus class="h-4 w-4" />
                    </Button>

                    <input type="number" v-model.number="item.quantity"
                        @change="cartStore.updateQuantity(item.id, item.quantity)" min="1"
                        class="w-12 text-center font-medium border rounded-md h-8 text-sm dark:border-white focus:outline-none focus:ring-2 focus:ring-green-400" />

                    <Button variant="outline" size="icon" class="h-8 w-8 border dark:border-white"
                        @click="cartStore.updateQuantity(item.id, item.quantity + 1)">
                        <Plus class="h-4 w-4" />
                    </Button>
                </div>

                <div class="flex items-center gap-3">
                    <Button variant="destructive" size="icon" class="h-8 w-8 text-white dark:bg-red-600 hover:opacity-90"
                        @click="cartStore.removeFromCart(item.id)">
                        <Trash2 class="h-4 w-4" />
                    </Button>
                </div>
            </div>
        </div>
    </div>
</template>

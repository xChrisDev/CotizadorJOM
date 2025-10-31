<script setup>
import { ref, watch } from 'vue';
import { Card, CardContent, CardFooter, CardHeader } from '@/shared/components/ui/card';
import { Button } from '@/shared/components/ui/button';
import { Input } from '@/shared/components/ui/input';
import { Plus, Minus, PackagePlusIcon } from 'lucide-vue-next';
import Badge from '@/shared/components/ui/badge/Badge.vue';
import placeholderImage from '@/shared/assets/default-image.jpg';
import { useCartStore } from '../stores/cart.js';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/shared/components/ui/table';

const cartStore = useCartStore();

const props = defineProps({
    product: {
        type: Object,
        required: true
    }
});

const productAmount = ref(1);

watch(productAmount, (newVal) => {
    if (!newVal || newVal < 1) productAmount.value = 1;
});

function increment() { productAmount.value++; }
function decrement() { if (productAmount.value > 1) productAmount.value--; }
</script>

<template>
    <Card class="overflow-visible shadow-lg flex flex-col">
        <CardHeader class="relative px-4">
            <img :src="product.image_url || placeholderImage" :alt="product.article_name"
                class="w-full h-48 object-cover rounded-lg" />
            <Badge variant="solid" class="absolute -top-2 left-2 bg-white text-black shadow-md">
                {{ product.brand.name }}
            </Badge>
        </CardHeader>

        <CardContent class="space-y-2 px-4">
            <h4 class="text-lg font-bold line-clamp-2">{{ product.article_name }}</h4>

            <p class="text-sm text-gray-500">
                <span class="font-medium">Categoría:</span> {{ product.category.name }}
            </p>
            <p class="text-sm text-gray-500">
                <span class="font-medium">Familia:</span> {{ product.family.name }}
            </p>

            <div class="border dark:border-[#38383d] border-green-400 rounded-lg overflow-hidden custom-scrollbar">
                <Table>
                    <TableHeader>
                        <TableRow class="dark:bg-[#27272a] bg-green-100/60 hover:bg-green-100/60 text-xs font-semibold">
                            <TableHead class="text-center dark:text-white">Lista</TableHead>
                            <TableHead class="text-center dark:text-white">Descuento</TableHead>
                            <TableHead class="text-center dark:text-white">Mayoreo</TableHead>
                            <TableHead class="text-center dark:text-white">Mínimo</TableHead>
                            <TableHead class="text-center dark:text-white">Crédito</TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        <TableRow class="text-sm">
                            <TableCell v-for="price in product.prices" :key="price.id" class="text-center font-medium">
                                ${{ parseFloat(price.price).toFixed(2) }}
                            </TableCell>
                        </TableRow>
                    </TableBody>
                </Table>
            </div>
        </CardContent>

        <CardFooter class="px-4 pb-4 flex flex-col gap-3">
            <div class="card w-full grid grid-cols-1 lg:grid-cols-2 gap-2">
                <div class="col-span-1 flex items-center gap-1">
                    <Button variant="outline" size="icon" class="h-9 w-9" @click="decrement">
                        <Minus class="w-4 h-4" />
                    </Button>
                    <Input type="number" v-model.number="productAmount" min="1"
                        class="h-9 lg:w-18 w-full text-center rounded-md mx-1" />
                    <Button variant="outline" size="icon" class="h-9 w-9" @click="increment">
                        <Plus class="w-4 h-4" />
                    </Button>
                </div>

                <Button size="lg" @click="cartStore.addToCart(product, productAmount)"
                    class="col-span-1 flex items-center justify-center gap-2 bg-gradient-to-r from-[#4ed636] to-[#09cb6d]">
                    <PackagePlusIcon class="w-5 h-5" />
                    <span>Agregar</span>
                </Button>
            </div>
        </CardFooter>
    </Card>
</template>

<script setup>
import { ref, computed } from 'vue';
import { Card } from '@/shared/components/ui/card';
import { Badge } from '@/shared/components/ui/badge';
import { Button } from '@/shared/components/ui/button';
import { Input } from '@/shared/components/ui/input';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/shared/components/ui/table';
import { Plus, Minus, PackagePlusIcon } from 'lucide-vue-next';
import placeholderImage from '@/shared/assets/default-image.jpg';
import { useCartStore } from '../stores/cart.js';

const cartStore = useCartStore();

const props = defineProps({
    product: {
        type: Object,
        required: true
    }
});

const productAmount = ref(1);
const selectedPrice = ref('Lista');

function increment() {
    productAmount.value++;
}

function decrement() {
    if (productAmount.value > 1) productAmount.value--;
}

const currentPrice = computed(() => {
    const priceObj = props.product.prices.find(p => p.price_type_name === selectedPrice.value);
    return priceObj ? parseFloat(priceObj.price) : 0;
});
</script>

<template>
    <Card class="flex flex-col md:flex-row items-center p-4 gap-4 w-full">

        <div class="relative">
            <img :src="product.image_url || placeholderImage" :alt="product.article_name"
                class="w-full md:w-24 h-36 md:h-24 object-cover rounded-md" />
            <Badge variant="solid" class="absolute -top-2 -left-2 bg-white text-black shadow-md">
                {{ product.brand.name }}
            </Badge>
        </div>

        <div class="flex flex-col justify-between flex-grow h-full w-full md:w-auto">
            <div>
                <div class="flex gap-2 items-center">
                    <h4 class="text-md font-semibold mt-2">{{ product.article_name }}</h4>
                    <p class="text-sm text-muted-foreground mt-1">
                        <strong>Categoría:</strong> {{ product.category.name }} |
                        <strong>Familia:</strong> {{ product.family.name }}
                    </p>
                </div>

                <div class="flex gap-4 mt-2">
                    <div class="w-full border dark:border-[#38383d] border-green-400 rounded-lg overflow-hidden">
                        <Table>
                            <TableHeader>
                                <TableRow
                                    class="dark:bg-[#27272a] bg-green-100/60 hover:bg-green-100/60 text-xs font-semibold">
                                    <TableHead class="text-center dark:text-white">Lista</TableHead>
                                    <TableHead class="text-center dark:text-white">Descuento</TableHead>
                                    <TableHead class="text-center dark:text-white">Mayoreo</TableHead>
                                    <TableHead class="text-center dark:text-white">Mínimo</TableHead>
                                    <TableHead class="text-center dark:text-white">Crédito</TableHead>
                                </TableRow>
                            </TableHeader>
                            <TableBody>
                                <TableRow class="text-sm">
                                    <TableCell v-for="price in product.prices" :key="price.id"
                                        class="text-center font-medium">
                                        ${{ parseFloat(price.price).toFixed(2) }}
                                    </TableCell>
                                </TableRow>
                            </TableBody>
                        </Table>
                    </div>
                    <div class="flex-shrink-0 w-full md:w-48 flex flex-col items-stretch justify-center gap-2">
                        <div class="w-full flex">
                            <Button variant="outline" size="icon" class="h-9 w-9" @click="decrement">
                                <Minus class="w-4 h-4" />
                            </Button>
                            <Input type="text" readonly min="1" v-model="productAmount" class="h-9 text-center mx-1" />
                            <Button variant="outline" size="icon" class="h-9 w-9" @click="increment">
                                <Plus class="w-4 h-4" />
                            </Button>
                        </div>

                        <Button @click="cartStore.addToCart(product, productAmount, currentPrice.value)"
                            class="w-full bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90 disabled:opacity-50 disabled:bg-gray-500">
                            <PackagePlusIcon class="size-5 mr-2" />
                            <span>Agregar</span>
                        </Button>
                    </div>
                </div>

            </div>
        </div>
    </Card>
</template>

<script setup>
import { ref } from 'vue';
import { Button } from '@/shared/components/ui/button';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/shared/components/ui/select';
import { Grip, List } from 'lucide-vue-next';
import ProductCardGrid from './ProductCardGrid.vue';
import ProductCardList from './ProductCardList.vue';

defineProps({
    products: {
        type: Array,
        required: true
    }
});

const viewMode = ref('grid');
</script>

<template>
    <div>
        <div class="flex justify-between items-center mb-4">
            <p class="text-sm text-muted-foreground"><span class="font-bold text-foreground">{{ products.length }}
                    productos</span> encontrados</p>
            <div class="flex items-center gap-2">
                <Button @click="viewMode = 'grid'" :variant="viewMode === 'grid' ? 'secondary' : 'ghost'" size="icon"
                    class="hidden md:flex">
                    <Grip class="w-5 h-5" />
                </Button>
                <Button @click="viewMode = 'list'" :variant="viewMode === 'list' ? 'secondary' : 'ghost'" size="icon"
                    class="hidden md:flex">
                    <List class="w-5 h-5" />
                </Button>
                <Select default-value="relevancia">
                    <SelectTrigger class="w-[180px]">
                        <SelectValue placeholder="Ordenar por" />
                    </SelectTrigger>
                    <SelectContent>
                        <SelectItem value="relevancia">Más relevantes</SelectItem>
                        <SelectItem value="precio-asc">Precio: Menor a Mayor</SelectItem>
                        <SelectItem value="precio-desc">Precio: Mayor a Menor</SelectItem>
                    </SelectContent>
                </Select>
            </div>
        </div>

        <div v-if="viewMode === 'grid'" class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-6">
            <ProductCardGrid v-for="product in products" :key="`card-${product.id}`" :product="product" />
        </div>
        <div v-else class="flex flex-col gap-4">
            <ProductCardList v-for="product in products" :key="`item-${product.id}`" :product="product" />
        </div>
    </div>
</template>
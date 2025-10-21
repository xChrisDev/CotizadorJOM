<script setup>
import { ref, computed, onMounted } from 'vue';
import { Button } from '@/shared/components/ui/button';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/shared/components/ui/select';
import { Grip, List, Filter } from 'lucide-vue-next';
import ProductCardGrid from './ProductCardGrid.vue';
import ProductCardList from './ProductCardList.vue';
import { fetchFamilies, fetchBrands, fetchCategories } from '@/shared/services/productService.js';

const props = defineProps({
    products: {
        type: Array,
        required: true
    }
});

const viewMode = ref('grid');

const familia = ref('');
const categoria = ref('');
const marca = ref('');

const families = ref([]);
const categories = ref([]);
const brands = ref([]);

const loadFilters = async () => {
    try {
        const data_fam = await fetchFamilies({
            page_size: 100,
        });

        const data_cat = await fetchCategories({
            page_size: 100,
        });

        const data_br = await fetchBrands({
            page_size: 100,
        });
        families.value = data_fam.results ?? [];
        categories.value = data_cat.results ?? [];
        brands.value = data_br.results ?? [];
    } catch (error) {
        console.error("Error al cargar filtros:", error);
    }
};

onMounted(loadFilters)

</script>

<template>
    <div>
        <div class="flex flex-col md:flex-row justify-between md:items-center gap-4 py-4">
            <div class="flex flex-col lg:flex-row flex-wrap gap-3 items-center">
                <div class="flex items-center gap-2 text-muted-foreground">
                    <Filter class="w-4 h-4" />
                    <span class="font-medium text-sm">Filtros</span>
                </div>

                <Select v-model="familia">
                    <SelectTrigger class="w-full lg:w-[100px]">
                        <SelectValue placeholder="Familia" />
                    </SelectTrigger>
                    <SelectContent>
                        <SelectItem value="all">Todas</SelectItem>
                        <SelectItem v-for="f in families" :key="f.id" :value="f.name">{{ f.name }}</SelectItem>
                    </SelectContent>
                </Select>

                <Select v-model="categoria">
                    <SelectTrigger class="w-full lg:w-[120px]">
                        <SelectValue placeholder="Categoría" />
                    </SelectTrigger>
                    <SelectContent>
                        <SelectItem value="all">Todas</SelectItem>
                        <SelectItem v-for="c in categories" :key="c.id" :value="c.name">{{ c.name }}</SelectItem>
                    </SelectContent>
                </Select>

                <Select v-model="marca">
                    <SelectTrigger class="w-full lg:w-[100px]">
                        <SelectValue placeholder="Marca" />
                    </SelectTrigger>
                    <SelectContent>
                        <SelectItem value="all">Todas</SelectItem>
                        <SelectItem v-for="m in brands" :key="m.id" :value="m.name">{{ m.name }}</SelectItem>
                    </SelectContent>
                </Select>
            </div>

            <div class="flex items-center gap-2">
                <Button @click="viewMode = 'grid'" :variant="viewMode === 'grid' ? 'secondary' : 'ghost'" size="icon"
                    class="hidden md:flex">
                    <Grip class="w-6 h-6" />
                </Button>
                <Button @click="viewMode = 'list'" :variant="viewMode === 'list' ? 'secondary' : 'ghost'" size="icon"
                    class="hidden md:flex">
                    <List class="w-6 h-6" />
                </Button>
            </div>
        </div>

        <div v-if="products.length > 0">
            <div v-if="viewMode === 'grid'" class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-6">
                <ProductCardGrid v-for="product in products" :key="`card-${product.id}`" :product="product" />
            </div>

            <div v-else class="flex flex-col gap-4">
                <ProductCardList v-for="product in products" :key="`item-${product.id}`" :product="product" />
            </div>
        </div>

        <div v-else class="text-center text-muted-foreground py-10">
            No se encontraron productos con los filtros seleccionados.
        </div>
    </div>
</template>

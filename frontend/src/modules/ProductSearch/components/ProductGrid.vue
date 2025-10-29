<script setup>
import { ref, computed, onMounted, watch } from 'vue';
import { Button } from '@/shared/components/ui/button';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/shared/components/ui/select';
import { Grip, List, Filter, FileEdit } from 'lucide-vue-next';
import ProductCardGrid from './ProductCardGrid.vue';
import ProductCardList from './ProductCardList.vue';
import { fetchFamilies, fetchBrands, fetchCategories } from '@/shared/services/productService.js';
import SearchBar from './SearchBar.vue';
import { fetchArticles } from '@/shared/services/productService.js'
import { Pagination, PaginationContent, PaginationEllipsis, PaginationItem, PaginationNext, PaginationPrevious } from '@/shared/components/ui/pagination';
import { useDebounce } from '@/shared/utils/useDebounce.js';

const products = ref([])
const isLoading = ref(true);
const search = ref("");
const ordering = ref("article_name");
const page = ref(1);
const totalItems = ref(0);
const itemsPerPage = 9;
const viewMode = ref('grid');
const familia = ref('');
const categoria = ref('');
const marca = ref('');
const families = ref([]);
const categories = ref([]);
const brands = ref([]);
let debounceTimeout = null;

const loadProducts = async () => {
    isLoading.value = true;
    try {
        const data = await fetchArticles({
            search: search.value,
            ordering: ordering.value,
            page: page.value,
            page_size: itemsPerPage,
        });
        products.value = data.results ?? [];
        totalItems.value = data.count ?? 0;
    } catch (error) {
        console.error("Error al cargar productos:", error);
    } finally {
        isLoading.value = false;
    }
};

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

onMounted(loadProducts)
onMounted(loadFilters)

const debouncedSearch = useDebounce(search, 300);
const debouncedPage = useDebounce(page, 300);
const debouncedOrdering = useDebounce(ordering, 300);
watch([debouncedSearch, debouncedOrdering, debouncedPage], loadProducts);

</script>

<template>
    <div class="xl:sticky top-0 pt-2 z-[19]">
        <div class="flex flex-col justify-between md:items-center gap-4">
            <div
                class="w-full flex flex-col gap-4 sm:gap-6 xl:flex-row sm:items-center sm:justify-between bg-card/60 backdrop-blur-md rounded-xl p-4 border border-border shadow-sm">
                <SearchBar />

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
            </div>
        </div>
    </div>

    <div class="w-full flex justify-end gap-2 py-4">
        <Button @click="viewMode = 'grid'" :variant="viewMode === 'grid' ? 'secondary' : 'ghost'"
            class="hidden md:flex">
            <Grip class="w-6 h-6" />
            <span>Cuadricula</span>
        </Button>
        <Button @click="viewMode = 'list'" :variant="viewMode === 'list' ? 'secondary' : 'ghost'"
            class="hidden md:flex">
            <List class="w-6 h-6" />
            <span>Lista</span>
        </Button>
    </div>

    <div v-if="isLoading" class="flex justify-center items-center h-[calc(100vh-200px)]">
        <div class="w-12 h-12 border-4 border-gray-300 border-t-green-500 rounded-full animate-spin"></div>
    </div>

    <div v-else>
        <div v-if="products.length > 0" class="overflow-hidden">
            <div v-if="viewMode === 'grid'"
                class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-6 overflow-y-auto">
                <ProductCardGrid v-for="product in products" :key="`card-${product.id}`" :product="product" />
            </div>

            <div v-else class="flex flex-col gap-4 overflow-y-auto">
                <ProductCardList v-for="product in products" :key="`item-${product.id}`" :product="product" />
            </div>
        </div>

        <div v-else class="text-center text-muted-foreground py-10">
            No se encontraron productos con los filtros seleccionados.
        </div>
    </div>

    <div v-if="totalItems > itemsPerPage" class="bg-background border-t flex justify-center pt-4 mt-4">
        <Pagination v-model:page="page" :items-per-page="itemsPerPage" :total="totalItems">
            <PaginationContent v-slot="{ items }">
                <PaginationPrevious />
                <template v-for="(item, index) in items" :key="index">
                    <PaginationItem v-if="item.type === 'page'" :value="item.value" :is-active="item.value === page">
                        {{ item.value }}
                    </PaginationItem>
                </template>
                <PaginationEllipsis :index="4" />
                <PaginationNext />
            </PaginationContent>
        </Pagination>
    </div>

</template>

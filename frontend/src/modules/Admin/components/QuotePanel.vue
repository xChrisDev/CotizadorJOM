<script setup>
import ProductFilters from '@/modules/ProductSearch/components/ProductFilters.vue';
import ProductGrid from '@/modules/ProductSearch/components/ProductGrid.vue';
import SearchBar from '@/modules/ProductSearch/components/SearchBar.vue';
import { fetchArticles } from '@/shared/services/productService.js'
import { onMounted, ref, watch } from 'vue';

const products = ref([])
const isLoading = ref(true);
const search = ref("");
const ordering = ref("article_name");
const page = ref(1);
const totalItems = ref(0);
const itemsPerPage = 10;

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

watch(search, () => {
  page.value = 1;
  loadProducts();
});

onMounted(loadProducts)

</script>

<template>
    <div>
        <SearchBar v-model="search" :products="products" />

        <div class="">

            <main class="lg:col-span-3">
                <ProductGrid :products="products" />
            </main>
        </div>
    </div>
</template>

<script setup>
import ProductFilters from '@/modules/ProductSearch/components/ProductFilters.vue';
import ProductGrid from '@/modules/ProductSearch/components/ProductGrid.vue';
import SearchBar from '@/modules/ProductSearch/components/SearchBar.vue';
import ShoppingCartButton from '@/modules/ProductSearch/components/ShoppingCartButton.vue';


</script>

<template>
    <main class="lg:col-span-3">
        <ProductGrid />
        <ShoppingCartButton />
    </main>
</template>

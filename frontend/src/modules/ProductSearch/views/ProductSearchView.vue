<script setup>
import { ref } from 'vue';
import ProductFilters from '../components/ProductFilters.vue';
import ProductGrid from '../components/ProductGrid.vue';
import Navbar from '../components/Navbar.vue';
import SearchBar from '../components/SearchBar.vue';
import Footer from '@/modules/LandingPage/components/Footer.vue';

const products = ref([
    { id: 1, brand: 'Bosch', name: 'Kit de Frenos Delanteros Bosch Premium', price: 2499.00, oldPrice: 2899.00, rating: 4, reviews: 47, image: '@/shared/assets/default-image.jpg' },
    { id: 2, brand: 'Mann-Filter', name: 'Filtro de Aceite Mann-Filter HU...', price: 189.00, rating: 5, reviews: 123, image: '@/shared/assets/default-image.jpg' },
    { id: 3, brand: 'NGK', name: 'Bujías NGK Iridium IX Set de 4 piezas', price: 890.00, rating: 5, reviews: 99, image: '@/shared/assets/default-image.jpg' },
    { id: 4, brand: 'Monroe', name: 'Amortiguador Monroe Gas-Matic...', price: 1299.00, oldPrice: 1499.00, rating: 4, reviews: 54, image: '@/shared/assets/default-image.jpg' },
    { id: 5, brand: 'Brembo', name: 'Pastillas de Freno Brembo Premium', price: 1890.00, rating: 5, reviews: 67, image: '@/shared/assets/default-image.jpg' },
    { id: 6, brand: 'Castrol', name: 'Aceite Motor Castrol GTX 5W-30 4L', price: 459.00, rating: 4, reviews: 166, image: '@/shared/assets/default-image.jpg' },
]);

</script>

<template>
    <div>
        <div class="w-[90%] lg:max-w-screen-xl mx-auto py-8">
            <Navbar />
            <SearchBar />

            <div class="grid grid-cols-1 lg:grid-cols-4 gap-8">
                <aside class="lg:col-span-1">
                    <ProductFilters />
                </aside>

                <main class="lg:col-span-3">
                    <ProductGrid :products="products" />
                    <!-- <ProductPagination /> -->
                </main>
            </div>

        </div>
        <Footer />
    </div>
</template>
<script setup>
import {
    Card,
    CardContent,
    CardFooter,
    CardHeader,
    CardTitle
} from '@/shared/components/ui/card';
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow
} from '@/shared/components/ui/table';
import Button from '@/shared/components/ui/button/Button.vue';
import { Search, ListCollapse, PackagePlus } from 'lucide-vue-next';
import { onMounted, ref, watch } from 'vue';
import { fetchArticles } from '@/shared/services/productService.js';
import { Select, SelectContent, SelectGroup, SelectItem, SelectLabel, SelectTrigger, SelectValue } from '@/shared/components/ui/select';
import {
    Pagination,
    PaginationContent,
    PaginationItem,
    PaginationPrevious,
    PaginationNext,
    PaginationEllipsis
} from "@/shared/components/ui/pagination";
import Input from '@/shared/components/ui/input/Input.vue';

const products = ref([]);
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

onMounted(loadProducts);

let timeout;
watch([search, ordering, page], () => {
    clearTimeout(timeout);
    timeout = setTimeout(() => {
        loadProducts();
    }, 300);
});

</script>
<template>
    <div class="flex gap-4 flex-col h-[calc(100vh-120px)]">
        <header
            class="flex flex-col gap-4 sm:gap-6 sm:flex-row sm:items-center sm:justify-between bg-card/60 backdrop-blur-md rounded-xl p-4 border border-border shadow-sm">
            <div>
                <h2 class="text-2xl sm:text-3xl font-semibold tracking-tight flex items-center gap-2">
                    <PackagePlus class="text-primary size-6" />
                    Productos
                </h2>
                <p class="text-sm text-muted-foreground">
                    Administra y gestiona los productos registrados en el sistema.
                </p>
            </div>

            <div class="flex flex-col sm:flex-row gap-3 sm:items-center sm:justify-end w-full sm:w-auto">
                <div class="relative w-full sm:w-72">
                    <Input v-model="search" type="text" placeholder="Buscar producto..." autocomplete="off"
                        class="pl-10 w-full focus:ring-2 focus:ring-primary/30 transition-all" />
                    <span class="absolute start-0 inset-y-0 flex items-center justify-center px-2">
                        <Search class="size-5 text-muted-foreground" />
                    </span>
                </div>

                <div class="grid grid-cols-2 items-center gap-2 justify-center lg:justify-end">
                    <Select v-model="ordering">
                        <SelectTrigger class="col-span-1 w-full">
                            <SelectValue placeholder="Ordenar por..." />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectGroup>
                                <SelectLabel>Ordenar por</SelectLabel>
                                <SelectItem value="article_name">Nombre</SelectItem>
                                <SelectItem value="item_code">Código</SelectItem>
                                <SelectItem value="category__name">Categoría</SelectItem>
                                <SelectItem value="brand__name">Marca</SelectItem>
                            </SelectGroup>
                        </SelectContent>
                    </Select>

                    <Button>Crear Producto</Button> 
                </div>
            </div>
        </header>

        <Card class="flex flex-col flex-1 overflow-hidden">
            <CardContent class="px-2 flex-1 overflow-y-auto">
                <div class="flex items-center gap-2 ps-2">
                    <ListCollapse class="size-5" />
                    Mostrando <span class="font-bold">{{ totalItems }}</span> registros
                </div>

                <div v-if="isLoading" class="flex justify-center items-center py-20">
                    <div class="w-12 h-12 border-4 border-gray-300 border-t-green-500 rounded-full animate-spin"></div>
                </div>

                <Table v-else-if="products && products.length > 0">
                    <TableHeader>
                        <TableRow>
                            <TableHead>Imagen</TableHead>
                            <TableHead>SKU</TableHead>
                            <TableHead>Nombre</TableHead>
                            <TableHead>Familia</TableHead>
                            <TableHead>Categoría</TableHead>
                            <TableHead>Marca</TableHead>
                            <TableHead>U. de Medida</TableHead>
                            <TableHead class="text-center">Acciones</TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        <TableRow v-for="product in products" :key="product.id">
                            <TableCell>
                                <img :src="product.image || '/src/shared/assets/default-image.jpg'" :alt="product.article_name" class="w-16 h-16 object-cover rounded-md">
                            </TableCell>
                            <TableCell class="font-medium">
                                {{ product.item_code }}
                            </TableCell>
                            <TableCell>
                                {{ product.article_name }}
                            </TableCell>
                            <TableCell>{{ product.family.name }}</TableCell>
                            <TableCell>{{ product.category.name }}</TableCell>
                            <TableCell>{{ product.brand.name }}</TableCell>
                            <TableCell>{{ product.unit_of_measure }}</TableCell>
                            <TableCell class="flex gap-2 justify-center">
                                <Button variant="outline">Editar</Button>
                                <Button variant="destructive">Eliminar</Button>
                            </TableCell>
                        </TableRow>
                    </TableBody>
                </Table>

                <div v-else class="text-center py-10 text-muted-foreground">
                    <p class="text-lg">No hay productos disponibles.</p>
                </div>
            </CardContent>

            <CardFooter v-if="totalItems > itemsPerPage"
                class="sticky bottom-0 bg-background border-t flex justify-center p-4">
                <Pagination v-model:page="page" :items-per-page="itemsPerPage" :total="totalItems">
                    <PaginationContent v-slot="{ items }">
                        <PaginationPrevious />
                        <template v-for="(item, index) in items" :key="index">
                            <PaginationItem v-if="item.type === 'page'" :value="item.value"
                                :is-active="item.value === page">
                                {{ item.value }}
                            </PaginationItem>
                        </template>
                        <PaginationEllipsis :index="4" />
                        <PaginationNext />
                    </PaginationContent>
                </Pagination>
            </CardFooter>
        </Card>
    </div>
</template>

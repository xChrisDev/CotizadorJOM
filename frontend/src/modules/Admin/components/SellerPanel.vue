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
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuTrigger,
} from '@/shared/components/ui/dropdown-menu'
import Button from '@/shared/components/ui/button/Button.vue';
import Badge from '@/shared/components/ui/badge/Badge.vue';
import Separator from '@/shared/components/ui/separator/Separator.vue';
import { MoreVertical, Info, Search, ListCollapse, ShoppingCart, UserRoundPlus } from 'lucide-vue-next';
import { onMounted, ref, watch } from 'vue';
import { fetchUsers } from '../services/userService.js';
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
import { getStatusClasses, getStatusText } from '../utils/styleBadge.js'
import EditUser from './modals/EditUser.vue';
import BanUser from './modals/BanUser.vue';
import ActivateUser from './modals/ActivateUser.vue';

const sellers = ref([]);
const isLoading = ref(true);
const search = ref("");
const ordering = ref("username");
const page = ref(1);
const totalItems = ref(0);
const itemsPerPage = 10;

const loadSellers = async () => {
    isLoading.value = true;
    try {
        const data = await fetchUsers('SELLER', {
            search: search.value,
            ordering: ordering.value,
            page: page.value,
            page_size: itemsPerPage,
        });
        sellers.value = data.results;
        totalItems.value = data.count;
    } catch (error) {
        console.error("Error al cargar vendedores:", error);
    } finally {
        isLoading.value = false;
    }
};

onMounted(loadSellers);
let timeout;
watch([search, ordering, page], () => {
    clearTimeout(timeout);
    timeout = setTimeout(() => {
        loadSellers();
    }, 300);
});

</script>
<template>
    <div class="flex gap-4 flex-col h-[calc(100vh-120px)]">
        <header
            class="flex flex-col gap-4 sm:gap-6 sm:flex-row sm:items-center sm:justify-between bg-card/60 backdrop-blur-md rounded-xl p-4 border border-border shadow-sm">
            <div>
                <h2 class="text-2xl sm:text-3xl font-semibold tracking-tight flex items-center gap-2">
                    <ShoppingCart class="text-primary size-6" />
                    Vendedores
                </h2>
                <p class="text-sm text-muted-foreground">
                    Administra y gestiona los vendedores registrados en el sistema.
                </p>
            </div>

            <div class="flex flex-col sm:flex-row gap-3 sm:items-center sm:justify-end w-full sm:w-auto">
                <div class="relative w-full sm:w-72">
                    <Input v-model="search" type="text" placeholder="Buscar vendedor..." autocomplete="off"
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
                                <SelectItem value="username">Usuario</SelectItem>
                                <SelectItem value="first_name">Nombre</SelectItem>
                                <SelectItem value="email">Correo</SelectItem>
                                <SelectItem value="status">Status</SelectItem>
                            </SelectGroup>
                        </SelectContent>
                    </Select>

                    <Button
                        class="col-span-1 bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90 transition-all">
                        <UserRoundPlus class="size-4 mr-1" />
                        Nuevo
                    </Button>
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

                <Table v-else-if="sellers && sellers.length > 0">
                    <TableHeader>
                        <TableRow>
                            <TableHead>Usuario</TableHead>
                            <TableHead>Nombre completo</TableHead>
                            <TableHead>Correo</TableHead>
                            <TableHead>Número telefónico</TableHead>
                            <TableHead class="text-center">Status</TableHead>
                            <TableHead class="text-center">Acciones</TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        <TableRow v-for="seller in sellers" :key="seller.id">
                            <TableCell class="font-medium">
                                {{ seller.username }}
                            </TableCell>
                            <TableCell>
                                {{ seller.first_name }} {{ seller.last_name }}
                            </TableCell>
                            <TableCell>{{ seller.email }}</TableCell>
                            <TableCell>{{ seller.phone_number }}</TableCell>
                            <TableCell class="text-center">
                                <div
                                    :class="['inline-flex w-24 justify-center rounded-full px-2.5 py-0.5 text-xs font-semibold', getStatusClasses(seller.status)]">
                                    {{ getStatusText(seller.status) }}
                                </div>
                            </TableCell>
                            <TableCell class="flex gap-2 justify-center">
                                <EditUser :id="seller.id" role="Vendedor" @update="loadSellers" />
                                <BanUser v-if="seller.status != 'BANNED'" :id="seller.id" role="Vendedor"
                                    @update="loadSellers" />
                                <ActivateUser v-if="seller.status == 'BANNED'" :id="seller.id" role="Vendedor"
                                    @update="loadSellers" />
                            </TableCell>
                        </TableRow>
                    </TableBody>
                </Table>

                <div v-else class="text-center py-10 text-muted-foreground">
                    <p class="text-lg">No hay vendedores disponibles.</p>
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

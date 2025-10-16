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
import { MoreVertical, Info, Search, UserRoundPlus, ListCollapse } from 'lucide-vue-next';
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
    <div>
        <div class="pb-4 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
            <div>
                <h2 class="text-3xl font-bold">Gestión de Vendedores</h2>
                <p class="text-muted-foreground mt-1">
                    Administra los vendedores registrados en el sistema.
                </p>
            </div>

            <Button class="bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90">
                <UserRoundPlus />
                <span class="hidden lg:block">Nuevo</span>
            </Button>
        </div>

        <div class="flex flex-col sm:flex-row items-center justify-between gap-4 pb-4">
            <div class="relative w-full max-w-md items-center">
                <Input v-model="search" type="text" placeholder="Buscar por nombre..." autocomplete="off"
                    class="pl-10" />
                <span class="absolute start-0 inset-y-0 flex items-center justify-center px-2">
                    <Search class="size-5 text-muted-foreground" />
                </span>
            </div>

            <Select v-model="ordering">
                <SelectTrigger>
                    <SelectValue placeholder="Ordenar por..." />
                </SelectTrigger>
                <SelectContent>
                    <SelectGroup>
                        <SelectLabel>Filtros</SelectLabel>
                        <SelectItem value="username">
                            Ordenar por usuario
                        </SelectItem>
                        <SelectItem value="first_name">
                            Ordenar por nombre
                        </SelectItem>
                        <SelectItem value="status">
                            Ordenar por status
                        </SelectItem>
                    </SelectGroup>
                </SelectContent>
            </Select>
        </div>

        <Card>
            <CardContent class="h-auto lg:min-h-[600px]">
                <div class="flex items-center gap-2 ps-2 pb-2">
                    <ListCollapse class="size-5" />
                    Mostrando <span class="font-bold">{{ totalItems }}</span> registros
                </div>
                <div v-if="isLoading" class="flex justify-center items-center py-20">
                    <div class="w-12 h-12 border-4 border-gray-300 border-t-green-500 rounded-full animate-spin"></div>
                </div>

                <Table v-else-if="sellers.length > 0">
                    <TableHeader>
                        <TableRow>
                            <TableHead>Usuario</TableHead>
                            <TableHead>Nombre completo</TableHead>
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

                            <TableCell class="text-center">
                                <div
                                    :class="['inline-flex w-24 justify-center rounded-full px-2.5 py-0.5 text-xs font-semibold', getStatusClasses(seller.status)]">
                                    {{ getStatusText(seller.status) }}
                                </div>
                            </TableCell>

                            <TableCell class="flex gap-2 justify-center">
                                <EditUser :id="seller.id" role="Vendedor" @update="loadSellers" />
                                <BanUser :id="seller.id" role="Vendedor" @update="loadSellers" />
                            </TableCell>
                        </TableRow>
                    </TableBody>
                </Table>

                <div v-else class="text-center py-10 text-muted-foreground">
                    <p class="text-lg">No hay vendedores disponibles.</p>
                </div>

            </CardContent>
            <CardFooter v-if="totalItems > itemsPerPage" class="flex justify-center">
                <div class="pt-6 flex justify-center">
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
                </div>
            </CardFooter>
        </Card>
    </div>
</template>
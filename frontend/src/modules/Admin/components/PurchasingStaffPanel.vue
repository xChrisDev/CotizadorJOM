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
import { Ban, PencilLine, MoreVertical, Info, Search, ListCollapse } from 'lucide-vue-next';
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

const purchasingStaff = ref([]);
const isLoading = ref(true);
const search = ref("");
const ordering = ref("username");
const page = ref(1);
const totalItems = ref(0);
const itemsPerPage = 8;

const loadPurchasingStaff = async () => {
    isLoading.value = true;
    try {
        const data = await fetchUsers('STAFF', {
            search: search.value,
            ordering: ordering.value,
            page: page.value,
            page_size: itemsPerPage,
        });
        purchasingStaff.value = data.results;
        totalItems.value = data.count;
    } catch (error) {
        console.error("Error al cargar el personal de compras:", error);
    } finally {
        isLoading.value = false;
    }
};


onMounted(loadPurchasingStaff);
watch([search, ordering, page], loadPurchasingStaff);

</script>

<template>
    <div>
        <div class="pb-4 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
            <div>
                <h2 class="text-3xl font-bold">Gestión de Personal de Compras</h2>
                <p class="text-muted-foreground mt-1">
                    Administra al personal de compras registrado en el sistema.
                </p>
            </div>

            <Button class="bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90">
                Crear Usuario
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

            <Select v-model="ordering" class="relative w-full max-w-md items-center">
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

                <Table v-else-if="purchasingStaff.length > 0">
                    <TableHeader>
                        <TableRow>
                            <TableHead>Usuario</TableHead>
                            <TableHead>Nombre completo</TableHead>
                            <TableHead class="text-center">Status</TableHead>
                            <TableHead class="text-center">Acciones</TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        <TableRow v-for="staff in purchasingStaff" :key="staff.id">
                            <TableCell class="font-medium">
                                {{ staff.username }}
                            </TableCell>
                            <TableCell>
                                {{ staff.first_name }} {{ staff.last_name }}
                            </TableCell>
                            <TableCell class="text-center">
                                <div
                                    :class="['inline-flex w-24 justify-center rounded-full px-2.5 py-0.5 text-xs font-semibold', getStatusClasses(staff.status)]">
                                    {{ getStatusText(staff.status) }}
                                </div>
                            </TableCell>

                            <TableCell class="flex gap-2 justify-center">
                                <EditUser :id="staff.id" role="Colaborador" @update="loadPurchasingStaff" />
                                <BanUser :id="staff.id" role="Colaborador" @update="loadPurchasingStaff"/>
                            </TableCell>
                        </TableRow>
                    </TableBody>
                </Table>

                <div v-else class="text-center py-10 text-muted-foreground">
                    <p class="text-lg">No hay personal de compras disponible.</p>
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
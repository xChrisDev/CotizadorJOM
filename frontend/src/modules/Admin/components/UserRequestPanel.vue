<script setup>
import {
    Card,
    CardContent,
    CardFooter,
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
import Badge from '@/shared/components/ui/badge/Badge.vue';
import { Ban, PencilLine, MoreVertical, Info, Search, Check, ListCollapse } from 'lucide-vue-next';
import { onMounted, ref, watch } from 'vue';
import { fetchPendingUsers } from '../services/userService.js';
import { Select, SelectContent, SelectGroup, SelectItem, SelectLabel, SelectTrigger, SelectValue } from '@/shared/components/ui/select';
import {
    Pagination,
    PaginationContent,
    PaginationItem,
    PaginationPrevious,
    PaginationNext,
    PaginationEllipsis
} from "@/shared/components/ui/pagination";
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogFooter,
    DialogHeader,
    DialogTitle,
} from '@/shared/components/ui/dialog';
import Input from '@/shared/components/ui/input/Input.vue';
import { getStatusClasses, getStatusText } from '../utils/styleBadge.js';

const customers = ref([]);
const isLoading = ref(true);
const search = ref("");
const ordering = ref("username");
const page = ref(1);
const totalItems = ref(0);
const itemsPerPage = 8;

const isConfirmDialogOpen = ref(false);
const selectedCustomerForApproval = ref(null);

const loadCustomers = async () => {
    isLoading.value = true;
    try {
        const data = await fetchPendingUsers({
            search: search.value,
            ordering: ordering.value,
            page: page.value,
            page_size: itemsPerPage,
        });
        customers.value = data.results;
        totalItems.value = data.count;
    } catch (error) {
        console.error("Error al cargar clientes:", error);
    } finally {
        isLoading.value = false;
    }
};

const handleApproveCustomer = (customer) => {
    selectedCustomerForApproval.value = customer;
    isConfirmDialogOpen.value = true;
};

const confirmApproval = () => {
    if (selectedCustomerForApproval.value) {
        // TODO: implement approval fetching 
    }
    closeDialog();
};

const closeDialog = () => {
    isConfirmDialogOpen.value = false;
    selectedCustomerForApproval.value = null;
};

onMounted(loadCustomers);
let timeout;
watch([search, ordering, page], () => {
    clearTimeout(timeout);
    timeout = setTimeout(() => {
        loadCustomers();
    }, 300);
});


</script>

<template>
    <div>
        <div class="pb-4 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
            <div>
                <h2 class="text-3xl font-bold">Solicitudes de registro</h2>
                <p class="text-muted-foreground mt-1">
                    Administra los clientes registrados en el sistema.
                </p>
            </div>
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
            <CardContent class="h-auto lg:min-h-[630px]">
                <div class="flex items-center gap-2 ps-2 pb-2">
                    <ListCollapse class="size-5" />
                    Mostrando <span class="font-bold">{{ totalItems }}</span> registros
                </div>
                <div v-if="isLoading" class="flex justify-center items-center py-25">
                    <div class="w-12 h-12 border-4 border-gray-300 border-t-green-500 rounded-full animate-spin"></div>
                </div>

                <Table v-else-if="customers.length > 0">
                    <TableHeader>
                        <TableRow>
                            <TableHead>Usuario</TableHead>
                            <TableHead>Nombre completo</TableHead>
                            <TableHead>Correo</TableHead>
                            <TableHead>Número telefónico</TableHead>
                            <TableHead class="text-center">Status</TableHead>
                            <TableHead class="text-center">Aprobar</TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        <TableRow v-for="customer in customers" :key="customer.id">
                            <TableCell class="font-medium">
                                {{ customer.username }}
                            </TableCell>
                            <TableCell>
                                {{ customer.first_name }} {{ customer.last_name }}
                            </TableCell>
                            <TableCell>{{ customer.email }}</TableCell>
                            <TableCell>{{ customer.phone_number }}</TableCell>

                            <TableCell class="text-center">
                                <div
                                    :class="['inline-flex w-24 justify-center rounded-full px-2.5 py-0.5 text-xs font-semibold', getStatusClasses(customer.status)]">
                                    {{ getStatusText(customer.status) }}
                                </div>
                            </TableCell>

                            <TableCell class="flex gap-2 justify-center">
                                <Button @click="handleApproveCustomer(customer)"
                                    class="bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90" size="icon">
                                    <Check />
                                </Button>
                            </TableCell>
                        </TableRow>
                    </TableBody>
                </Table>

                <div v-else class="text-center py-10 text-muted-foreground">
                    <p class="text-lg">No hay clientes disponibles.</p>
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

        <Dialog :open="isConfirmDialogOpen" @update:open="isConfirmDialogOpen = $event">
            <DialogContent>
                <DialogHeader>
                    <DialogTitle>Confirmación</DialogTitle>
                    <DialogDescription>
                        <span class="text-base font-semibold">{{ selectedCustomerForApproval?.username }}</span>
                        cambiará su estado a "Activo".
                    </DialogDescription>
                </DialogHeader>
                <DialogFooter>
                    <Button variant="outline" @click="closeDialog">Cancelar</Button>
                    <Button class="bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90"
                        @click="confirmApproval">Confirmar</Button>
                </DialogFooter>
            </DialogContent>
        </Dialog>

    </div>
</template>

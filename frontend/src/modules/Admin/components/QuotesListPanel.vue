<script setup>
import {
    Card, CardContent, CardFooter, CardHeader, CardTitle
} from '@/shared/components/ui/card';
import {
    Table, TableBody, TableCell, TableHead, TableHeader, TableRow
} from '@/shared/components/ui/table';
import {
    DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger,
} from '@/shared/components/ui/dropdown-menu'
import Button from '@/shared/components/ui/button/Button.vue';
import Badge from '@/shared/components/ui/badge/Badge.vue';
import Separator from '@/shared/components/ui/separator/Separator.vue';
import {
    Tooltip,
    TooltipContent,
    TooltipProvider,
    TooltipTrigger,
} from '@/shared/components/ui/tooltip'
import { Ban, PencilLine, MoreVertical, Info, Search, ListCollapse, UserRoundPlus, Calendar, MessageCircle, FileDown, Printer, Mail } from 'lucide-vue-next';
import { onMounted, ref, watch } from 'vue';
import { fetchQuotes } from '@/modules/Quote/services/quoteService.js';
import Skeleton from '@/shared/components/ui/skeleton/Skeleton.vue';
import {
    Select, SelectContent, SelectGroup, SelectItem, SelectLabel, SelectTrigger, SelectValue
} from '@/shared/components/ui/select';
import {
    Pagination, PaginationContent, PaginationItem,
    PaginationPrevious, PaginationNext, PaginationEllipsis
} from "@/shared/components/ui/pagination";
import Input from '@/shared/components/ui/input/Input.vue';
import { getStatusClasses, getStatusText } from '../utils/styleBadge.js'
import { downloadQuote, printQuote } from '@/modules/Quote/services/quoteService.js'
import { useToast } from 'vue-toastification';

const toast = useToast()
const quotes = ref([]);
const isLoading = ref(true);
const search = ref("");
const ordering = ref("-issue_date");
const page = ref(1);
const totalItems = ref(0);
const itemsPerPage = 10;

const status = ref("");
const issueDateStart = ref("");
const issueDateEnd = ref("");

const formatCurrency = (value) => {
    if (!value) return '$0.00';
    return new Intl.NumberFormat('es-MX', {
        style: 'currency',
        currency: 'MXN',
    }).format(value);
};

const loadQuotes = async () => {
    isLoading.value = true;

    const params = {
        search: search.value || undefined,
        status: status.value || undefined,
        ordering: ordering.value,
        page: page.value,
        page_size: itemsPerPage,
        issue_date_after: issueDateStart.value || undefined,
        issue_date_before: issueDateEnd.value || undefined,
    };

    try {
        const data = await fetchQuotes(params);
        quotes.value = data.results ?? [];
        totalItems.value = data.count ?? 0;
    } catch (error) {
        console.error("Error al cargar cotizaciones:", error);
    } finally {
        isLoading.value = false;
    }
};

const handleDownloadPDF = async (quote_id) => {
    try {
        await downloadQuote(quote_id);
        toast.success("PDF descargado exitosamente");
    } catch (error) {
        toast.error("Error al descargar PDF");
    }
}

const handlePrintPDF = async (quote_id) => {
    try {
        await printQuote(quote_id);
    } catch (error) {
        toast.error("Error al imprimir PDF");
    }
}

onMounted(loadQuotes);

let timeout;
watch([search, ordering, status, issueDateStart, issueDateEnd], () => {
    page.value = 1;
    clearTimeout(timeout);
    timeout = setTimeout(() => {
        loadQuotes();
    }, 300);
});

watch(page, () => {
    clearTimeout(timeout);
    timeout = setTimeout(() => {
        loadQuotes();
    }, 300);
});
</script>

<template>
    <div class="flex gap-4 flex-col h-[calc(100vh-120px)]">
        <header class="flex flex-col gap-6 bg-card/70 backdrop-blur-xl rounded-2xl p-6 border border-border/60 
         shadow-sm transition-all hover:shadow-md">

            <!-- 🧾 Encabezado -->
            <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2">
                <div>
                    <h2 class="text-2xl sm:text-3xl font-semibold tracking-tight flex items-center gap-2">
                        <ListCollapse class="text-primary size-6" />
                        Cotizaciones
                    </h2>
                    <p class="text-sm text-muted-foreground">
                        Administra y gestiona las cotizaciones registradas en el sistema.
                    </p>
                </div>

                <Button class="bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-95 hover:scale-[1.02]
             transition-all font-medium shadow-sm">
                    <UserRoundPlus class="size-4 mr-1" />
                    Nueva
                </Button>
            </div>

            <!-- 🎛️ Controles de filtrado -->
            <div class="flex flex-col lg:flex-row gap-4 lg:items-center lg:justify-between mt-2">

                <!-- 🔍 Búsqueda -->
                <div class="relative w-full lg:max-w-xs">
                    <Input v-model="search" type="text" placeholder="Buscar cotización..." autocomplete="off" class="pl-9 w-full focus:ring-2 focus:ring-primary/40 focus:border-primary/60 
               placeholder:text-muted-foreground/70 text-sm transition-all" />
                    <span class="absolute left-2 inset-y-0 flex items-center justify-center">
                        <Search class="size-4 text-muted-foreground/80" />
                    </span>
                </div>

                <!-- 📅 Filtros de fecha -->
                <div class="flex flex-col sm:flex-row sm:items-center gap-3">
                    <label class="flex items-center gap-2 text-sm text-muted-foreground">
                        <Calendar class="size-4" /> Fecha de emisión
                    </label>
                    <div class="flex items-center gap-2">
                        <Input v-model="issueDateStart" type="date" class="w-40 text-sm" />
                        <span class="text-muted-foreground text-xs">→</span>
                        <Input v-model="issueDateEnd" type="date" class="w-40 text-sm" />
                    </div>
                </div>

                <!-- ⚙️ Filtros y orden -->
                <div class="flex flex-col sm:flex-row gap-3 sm:items-center">

                    <Select v-model="status">
                        <SelectTrigger class="w-[160px]">
                            <SelectValue placeholder="Estado" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectGroup>
                                <SelectLabel>Estado</SelectLabel>
                                <SelectItem value="All">Todos</SelectItem>
                                <SelectItem value="pendiente">Pendiente</SelectItem>
                                <SelectItem value="aceptada">Aceptada</SelectItem>
                                <SelectItem value="cancelada">Cancelada</SelectItem>
                            </SelectGroup>
                        </SelectContent>
                    </Select>

                    <Select v-model="ordering">
                        <SelectTrigger class="w-[180px]">
                            <SelectValue placeholder="Ordenar por..." />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectGroup>
                                <SelectLabel>Ordenar por</SelectLabel>
                                <SelectItem value="-issue_date">Más recientes</SelectItem>
                                <SelectItem value="issue_date">Más antiguos</SelectItem>
                                <SelectItem value="quote_number">No. Cotización (Asc)</SelectItem>
                                <SelectItem value="-quote_number">No. Cotización (Desc)</SelectItem>
                                <SelectItem value="total">Total (Menor a Mayor)</SelectItem>
                                <SelectItem value="-total">Total (Mayor a Menor)</SelectItem>
                            </SelectGroup>
                        </SelectContent>
                    </Select>
                </div>
            </div>
        </header>


        <!-- 📋 Tabla -->
        <Card class="flex flex-col flex-1 overflow-hidden">
            <CardContent class="px-2 flex-1 overflow-y-auto">
                <div class="flex items-center gap-2 ps-2">
                    <ListCollapse class="size-5" />
                    Mostrando <span class="font-bold">{{ totalItems }}</span> registros
                </div>

                <div v-if="isLoading" class="flex justify-center items-center py-20">
                    <div class="w-12 h-12 border-4 border-gray-300 border-t-green-500 rounded-full animate-spin"></div>
                </div>

                <Table v-else-if="quotes && quotes.length > 0">
                    <TableHeader>
                        <TableRow>
                            <TableHead>No. Cotización</TableHead>
                            <TableHead>Cliente</TableHead>
                            <TableHead>Vendedor</TableHead>
                            <TableHead>Emisión</TableHead>
                            <TableHead>Vencimiento</TableHead>
                            <TableHead>Total</TableHead>
                            <TableHead class="text-center">Status</TableHead>
                            <TableHead class="text-center">Acciones</TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        <TableRow v-for="quote in quotes" :key="quote.id">
                            <TableCell class="font-medium">{{ quote.quote_number }}</TableCell>
                            <TableCell>{{ quote.customer.first_name }} {{ quote.customer.last_name }}</TableCell>
                            <TableCell>{{ quote.seller.first_name }} {{ quote.seller.last_name }}</TableCell>
                            <TableCell>{{ quote.issue_date }}</TableCell>
                            <TableCell>{{ quote.expiration_date }}</TableCell>
                            <TableCell>{{ formatCurrency(quote.total) }}</TableCell>
                            <TableCell class="text-center">
                                <div
                                    :class="['inline-flex w-24 justify-center rounded-full px-2.5 py-0.5 text-xs font-semibold', getStatusClasses(quote.status)]">
                                    {{ getStatusText(quote.status) }}
                                </div>
                            </TableCell>
                            <TableCell class="text-center">
                                <TableCell class="flex gap-2 justify-center">
                                    <TooltipProvider>
                                        <div class="flex gap-2">

                                            <Tooltip>
                                                <TooltipTrigger as-child>
                                                    <Button variant="default"
                                                        class="bg-blue-500 hover:bg-blue-600 text-white transition-all">
                                                        <Mail class="w-5 h-5" />
                                                    </Button>
                                                </TooltipTrigger>
                                                <TooltipContent>
                                                    <p>Enviar Correo</p>
                                                </TooltipContent>
                                            </Tooltip>

                                            <Tooltip>
                                                <TooltipTrigger as-child>
                                                    <Button variant="default"
                                                        class="bg-green-500 hover:bg-green-600 text-white transition-all">
                                                        <MessageCircle class="w-5 h-5" />
                                                    </Button>
                                                </TooltipTrigger>
                                                <TooltipContent>
                                                    <p>Enviar WhatsApp</p>
                                                </TooltipContent>
                                            </Tooltip>

                                            <Tooltip>
                                                <TooltipTrigger as-child>
                                                    <Button variant="default" @click="handleDownloadPDF(quote.id)"
                                                        class="bg-red-500 hover:bg-red-600 text-white transition-all">
                                                        <FileDown class="w-5 h-5" />
                                                    </Button>
                                                </TooltipTrigger>
                                                <TooltipContent>
                                                    <p>Descargar Archivo</p>
                                                </TooltipContent>
                                            </Tooltip>

                                            <Tooltip>
                                                <TooltipTrigger as-child>
                                                    <Button variant="default" @click="handlePrintPDF(quote.id)"
                                                        class="bg-slate-600 hover:bg-slate-700 text-white transition-all">
                                                        <Printer class="w-5 h-5" />
                                                    </Button>
                                                </TooltipTrigger>
                                                <TooltipContent>
                                                    <p>Imprimir</p>
                                                </TooltipContent>
                                            </Tooltip>

                                        </div>
                                    </TooltipProvider>
                                </TableCell>
                            </TableCell>
                        </TableRow>
                    </TableBody>
                </Table>

                <div v-else class="text-center py-10 text-muted-foreground">
                    <p class="text-lg">No hay cotizaciones disponibles.</p>
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

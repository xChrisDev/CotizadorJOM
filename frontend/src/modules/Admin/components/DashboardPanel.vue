<script setup>
import { ref, onMounted } from 'vue'
import { Send, CheckCircle, Clock } from 'lucide-vue-next'
import StatsCard from '@/shared/components/StatsCard.vue'
import { Card, CardContent } from '@/shared/components/ui/card'
import QuoteColumn from '@/modules/Quote/components/QuoteColumn.vue'
import { fetchQuotesByCustomerAndStatus } from '@/modules/Quote/services/quoteService.js'

const isLoading = ref(true);

const formatCurrency = (value) => {
    if (!value) return '$0.00';
    return new Intl.NumberFormat('es-MX', {
        style: 'currency',
        currency: 'MXN',
    }).format(value);
};

const kanbanColumns = ref([
    {
        id: 'DRAFT',
        title: 'Borrador',
        color: 'bg-gray-100 text-gray-800 border border-gray-400/30 dark:bg-gray-700 dark:text-gray-200 dark:border-gray-500',
        cards: []
    },
    {
        id: 'GENERATED',
        title: 'Generadas',
        color: 'bg-yellow-100 text-yellow-800 border border-yellow-400/30 dark:bg-yellow-800 dark:text-yellow-100 dark:border-yellow-600',
        cards: []
    },
    {
        id: 'SENT',
        title: 'Enviadas',
        color: 'bg-indigo-100 text-fuchsia-800 border border-fuchsia-400/30 dark:bg-fuchsia-800/90 dark:text-fuchsia-100 dark:border-fuchsia-600',
        cards: []
    },
    {
        id: 'ACCEPTED',
        title: 'Aprobadas',
        color: 'bg-green-200 text-green-800 border border-green-400/60 dark:bg-green-800 dark:text-green-200 dark:border-green-500',
        cards: []
    },
    {
        id: 'DELIVERED',
        title: 'Entregadas',
        color: 'bg-blue-200 text-blue-800 border border-blue-400/30 dark:bg-blue-900 dark:text-blue-100 dark:border-blue-600',
        cards: []
    },
    {
        id: 'EXPIRED',
        title: 'Vencidas',
        color: 'bg-red-100 text-red-800 border border-red-400/30 dark:bg-red-800/90 dark:text-red-100 dark:border-red-600',
        cards: []
    },
])

const mapDataToKanban = (apiData) => {
    if (!apiData || !apiData.results) return;

    const resultsByStatus = apiData.results;

    kanbanColumns.value = kanbanColumns.value.map(column => {
        const columnId = column.id;
        const rawQuotes = resultsByStatus[columnId] || [];

        const mappedCards = rawQuotes.map(quote => ({
            cliente: quote.customer_name,
            cotizaciones: quote.quotes_count,
            importe: formatCurrency(quote.quotes_total)
        }));

        return {
            ...column,
            cards: mappedCards
        };
    });
};

const fetchAndMapData = async () => {
    isLoading.value = true;
    try {
        const rawData = await fetchQuotesByCustomerAndStatus();

        mapDataToKanban(rawData);

    } catch (error) {
        console.error(error);
    } finally {
        isLoading.value = false;
    }
};

onMounted(() => {
    fetchAndMapData();
});
</script>

<template>
    <div>
        <div class="pb-4">
            <h2 class="text-3xl font-bold">Dashboard</h2>
            <p class="text-muted-foreground mt-2">
                Revisa el estado actual de todas las cotizaciones.
            </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-6 gap-4 custom-scrollbar">
            <QuoteColumn v-for="column in kanbanColumns" :key="column.id" :column="column" />
        </div>
    </div>
</template>
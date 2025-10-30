<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import { Card, CardContent, CardHeader, CardTitle } from '@/shared/components/ui/card'
import { Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue } from '@/shared/components/ui/select'
import { Button } from '@/shared/components/ui/button'
import { ShoppingCart, DollarSign, FileCog } from "lucide-vue-next"
import QuoteProductItem from '../components/QuoteProductItem.vue'
import QuoteSummaryCard from '../components/QuoteSummaryCard.vue'
import ClientDetailsCard from '../components/ClientDetailsCard.vue'
import ClientSearchBar from '../components/ClientSearchBar.vue'
import { useCartStore } from '@/modules/ProductSearch/stores/cart.js'
import { useDebounce } from '@/shared/utils/useDebounce.js'
import { postQuote, downloadQuote, printQuote } from '../services/quoteService.js'
import QuoteActionsCard from '../components/QuoteActionsCard.vue'
import { useToast } from "vue-toastification";
import apiClient from "@/shared/services/baseURL";

const toast = useToast();
const cartStore = useCartStore()

const price = ref('1')
const items = ref([])
const isLoadingItems = ref(false)
const quote = ref({})
const client = ref({})
const isLoadingClient = ref(false)
const isGenerating = ref(false)
const isGenerated = ref(false)
const isPreview = ref(false)
const pdfUrl = ref("")

const today = new Date()
const formattedDate = today.toISOString().split('T')[0]
const futureDate = new Date()
futureDate.setDate(today.getDate() + 30)
const formattedDueDate = futureDate.toISOString().split('T')[0]

const quoteData = ref({
    date: formattedDate,
    status: 'Pendiente',
    dueDate: formattedDueDate,
    notes: ''
})

const total = computed(() => {
    return items.value.reduce((sum, product) => {
        const selectedPrice = product.prices.find(p => p.price_type == price.value)?.price || 0;
        return sum + selectedPrice * product.quantity;
    }, 0);
})

const itemsWithSelectedPrice = computed(() => {
    return items.value.map(product => {
        const selected = product.prices.find(p => p.price_type == price.value);
        return { ...product, selectedPrice: selected ? parseFloat(selected.price) : 0 }
    })
})

const debouncedItems = useDebounce(items, 300)
const debouncedClient = useDebounce(client, 300)

watch(debouncedItems, (val) => {
    isLoadingItems.value = true
    items.value = val
    isLoadingItems.value = false
})

watch(debouncedClient, (val) => {
    if (!val || !val.id) return
    isLoadingClient.value = true
    client.value = val
    isLoadingClient.value = false
})

function handleClientSelect(selectedClient) {
    client.value = selectedClient
}

const handleGenerateQuote = async () => {
    if (!client.value.id) return
    isGenerating.value = true
    try {
        cartStore.clearCart()
        const data = await postQuote({
            customer_id: client.value.id,
            seller_id: localStorage.getItem('user_id'),
            initial_status_id: 1,
            issue_date: quoteData.value.date,
            expiration_date: quoteData.value.dueDate,
            notes: quoteData.value.notes,
            items: items.value.map(product => ({
                article_id: product.id,
                quantity: product.quantity,
                price: product.prices.find(p => p.price_type == price.value)?.price || 0
            }))
        });
        quote.value = data
        isGenerated.value = true
        const response = await apiClient.get(`/quotes/${quote.value.id}/pdf/`, { responseType: 'blob' })
        pdfUrl.value = URL.createObjectURL(new Blob([response.data], { type: 'application/pdf' }))
        isPreview.value = true
        toast.success(`Cotización ${quote.value.quote_number} generada correctamente.`)
    } catch (error) {
        console.error(error)
        toast.error("Error al generar cotización")
    } finally {
        isGenerating.value = false
    }
}

const handleSendWhatsApp = () => { }
const handleSendEmail = () => { }

const handleDownloadPDF = async () => {
    try {
        await downloadQuote(quote.value.id);
        toast.success("PDF descargado exitosamente");
    } catch (error) {
        toast.error("Error al descargar PDF");
    }
}

const handlePrintPDF = async () => {
    try {
        await printQuote(quote.value.id);
    } catch (error) {
        toast.error("Error al imprimir PDF");
    }
}

onMounted(() => {
    items.value = cartStore.items
})
</script>

<template>
    <div class="min-h-screen bg-background">
        <div class="w-[90%] md:w-[80%] lg:max-w-screen-xl mx-auto py-4 space-y-8">
            <div v-if="isPreview" class="flex flex-col items-center justify-center space-y-4">
                <QuoteActionsCard v-if="isGenerated" :show-convert-button="true" @send-email="handleSendEmail"
                    @send-whatsapp="handleSendWhatsApp" @download-pdf="handleDownloadPDF" @print-pdf="handlePrintPDF" />
                <iframe :src="pdfUrl" class="w-full h-[70vh] rounded-lg" type="application/pdf"></iframe>
            </div>

            <div v-else>
                <div>
                    <h1 class="text-3xl md:text-4xl font-bold">Generar cotización</h1>
                    <p class="text-muted-foreground mt-1">
                        Revisa los artículos, selecciona el tipo de precio y genera la cotización.
                    </p>
                </div>
                <div class="grid grid-cols-1 lg:grid-cols-[2fr_1fr] gap-6 items-start">
                    <div class="space-y-6">
                        <Card class="p-4">
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div class="flex flex-col">
                                    <label class="text-base font-medium mb-1 block">Cliente:</label>
                                    <ClientSearchBar @select:client="handleClientSelect" />
                                </div>

                                <div>
                                    <label class="text-base font-medium mb-1 block rounded-lg">Tipo de precio:</label>
                                    <Select v-model="price" class="rounded-lg">
                                        <SelectTrigger class="relative w-full border-2 rounded-lg border-[#4ed636]">
                                            <span
                                                class="absolute start-0 inset-y-0 flex items-center justify-center px-3 bg-gradient-to-r from-[#4ed636] to-[#09cb6d] rounded-s-md">
                                                <DollarSign class="size-5 dark:text-black text-white" />
                                            </span>
                                            <SelectValue class="pl-10" placeholder="Selecciona un tipo" />
                                        </SelectTrigger>
                                        <SelectContent class="border-2 border-[#4ed636]">
                                            <SelectGroup>
                                                <SelectItem value="1">Lista</SelectItem>
                                                <SelectItem value="2">Descuento</SelectItem>
                                                <SelectItem value="3">Mayoreo</SelectItem>
                                                <SelectItem value="4">Mínimo</SelectItem>
                                                <SelectItem value="5">Crédito</SelectItem>
                                            </SelectGroup>
                                        </SelectContent>
                                    </Select>
                                </div>
                            </div>
                        </Card>

                        <Card class="flex flex-col h-[65vh] px-2">
                            <CardHeader>
                                <CardTitle class="flex items-center gap-2">
                                    <ShoppingCart class="w-5 h-5" /> Artículos seleccionados
                                </CardTitle>
                            </CardHeader>

                            <CardContent class="overflow-y-auto px-2 custom-scrollbar">
                                <div v-if="isLoadingItems" class="flex justify-center py-10">
                                    <div
                                        class="w-10 h-10 border-4 border-gray-300 border-t-green-500 rounded-full animate-spin">
                                    </div>
                                </div>

                                <div v-else-if="items.length" class="space-y-4">
                                    <QuoteProductItem v-for="product in itemsWithSelectedPrice" :key="product.id"
                                        :product="product" :price="product.selectedPrice" />
                                </div>

                                <div v-else class="text-center text-muted-foreground py-10">
                                    No hay productos agregados aún.
                                </div>
                            </CardContent>
                        </Card>

                        <Card class="flex flex-col my-2">
                            <CardContent>
                                <label class="text-base font-medium block mb-1">Notas:</label>
                                <textarea v-model="quoteData.notes"
                                    placeholder="Agrega aquí notas o comentarios para la cotización"
                                    class="w-full p-2 border-2 border-[#4ed636] rounded-lg resize-none h-24 focus:outline-none focus:ring-2 focus:ring-[#4ed636] transition-all custom-scrollbar"></textarea>
                            </CardContent>
                        </Card>
                    </div>

                    <div class="space-y-6">
                        <QuoteSummaryCard :dueDate="quoteData.dueDate" :date="quoteData.date" :status="quoteData.status"
                            :total="total" />

                        <ClientDetailsCard :client="client" :is-loading="isLoadingClient" />

                        <Button v-if="!isGenerated" :disabled="!client || !client.id || isGenerating"
                            @click="handleGenerateQuote"
                            class="h-11 w-full text-lg bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90 transition-all flex justify-center items-center gap-2">
                            <FileCog class="size-6" />
                            <span v-if="!isGenerating">Generar</span>
                            <span v-else class="flex items-center gap-2">
                                <div
                                    class="w-5 h-5 border-4 border-gray-300 border-t-green-500 rounded-full animate-spin">
                                </div>
                                Generando...
                            </span>
                        </Button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

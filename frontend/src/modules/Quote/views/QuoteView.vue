<script setup>
import { ref } from 'vue';
import { Card, CardContent, CardHeader, CardTitle } from '@/shared/components/ui/card';
import { Button } from '@/shared/components/ui/button';
import { useColorMode } from "@vueuse/core";
import { Moon, Sun } from "lucide-vue-next";
import { Badge } from '@/shared/components/ui/badge';
import { ShoppingCart, ArrowLeft } from 'lucide-vue-next';
import { useRouter } from 'vue-router';
import Navbar from '@/modules/ProductSearch/components/Navbar.vue';
import Footer from '@/modules/LandingPage/components/Footer.vue';
import QuoteProductItem from '../components/QuoteProductItem.vue';
import QuoteSummaryCard from '../components/QuoteSummaryCard.vue';
import ClientDetailsCard from '../components/ClientDetailsCard.vue';
import QuoteActionsCard from '../components/QuoteActionsCard.vue';
import ThemeButton from '@/shared/components/ThemeButton.vue';

const mode = useColorMode();
const router = useRouter();

// Datos de ejemplo - en producción vendrían del store o API
const quoteData = ref({
    quoteNumber: 'COT-JOM-2024-00123',
    date: '2024-10-01',
    status: 'Pendiente',
    client: {
        name: 'Carlos Hernández',
        email: 'carlos.hernandez@example.com',
        phone: '+52 55 1234 5678'
    },
    products: [
        {
            id: 1,
            name: 'Filtro de Aire Deportivo',
            description: 'Filtro de alto rendimiento para motor',
            brand: 'K&N',
            quantity: 2,
            unitPrice: 75.00,
            imageUrl: null
        },
        {
            id: 2,
            name: 'Bujía de Iridio (Juego de 4)',
            description: 'Juego de 4 bujías de iridio para motor',
            brand: 'NGK',
            quantity: 1,
            unitPrice: 120.00,
            imageUrl: null
        },
        {
            id: 3,
            name: 'Aceite Sintético 5W-30',
            description: 'Aceite de motor sintético de alta calidad',
            brand: 'Castrol',
            quantity: 3,
            unitPrice: 55.00,
            imageUrl: null
        }
    ]
});

const total = ref(519.60);

function handleSendEmail() {
    alert('Funcionalidad de enviar por correo');
}

function handleSendWhatsApp() {
    alert('Funcionalidad de enviar por WhatsApp');
}

function handleDownloadPDF() {
    alert('Funcionalidad de descargar PDF');
}

function handleConvertToOrder() {
    router.push('/orden-compra');
}

function handleGoBack() {
    router.push('/buscar');
}
</script>

<template>
    <div class="min-h-screen bg-background">
        <div class="w-[90%] md:w-[70%] lg:w-[75%] lg:max-w-screen-xl mx-auto mb-6">
            <!-- <Navbar /> -->

            <div class="mt-12 mb-8">
                <div class="flex justify-between items-center mb-6">
                    <Button variant="" @click="handleGoBack" class="h-14">
                        <ArrowLeft class="w-4 h-4 mr-2" />
                        Regresar
                    </Button>
                    <Button @click="mode = mode === 'dark' ? 'light' : 'dark'" size="lg" variant="outline"
                        class="h-14 w-14 justify-center">
                        <div v-if="mode == 'light'" class="flex gap-2">
                            <Moon class="size-5" />
                        </div>

                        <div v-else="mode == 'dark'" class="flex gap-2">
                            <Sun class="size-5" />
                        </div>

                        <span class="sr-only">Toggle theme</span>
                    </Button>
                </div>

                <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
                    <div>
                        <h1 class="text-3xl md:text-4xl font-bold">Detalles de la Cotización</h1>
                        <p class="text-muted-foreground mt-2">
                            Revisa los detalles de tu cotización y elige cómo proceder.
                        </p>
                    </div>
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <!-- Sección principal -->
                <div class="lg:col-span-2 space-y-6">
                    <!-- Productos -->
                    <Card>
                        <CardHeader>
                            <CardTitle class="flex items-center gap-2">
                                <ShoppingCart class="w-5 h-5" />
                                Productos seleccionados
                            </CardTitle>
                        </CardHeader>
                        <CardContent>
                            <div class="space-y-4">
                                <QuoteProductItem v-for="product in quoteData.products" :key="product.id"
                                    :product="product" />
                            </div>
                        </CardContent>
                    </Card>

                    <ClientDetailsCard :client="quoteData.client" />
                </div>

                <!-- Sidebar -->
                <div class="space-y-6">
                    <!-- Resumen -->
                    <QuoteSummaryCard :order-number="quoteData.quoteNumber" :date="quoteData.date"
                        :status="quoteData.status" :subtotal="subtotal" :tax="tax" :shipping="shipping"
                        :total="total" />

                    <!-- Acciones -->
                    <QuoteActionsCard :show-convert-button="true" @send-email="handleSendEmail"
                        @send-whatsapp="handleSendWhatsApp" @download-pdf="handleDownloadPDF"
                        @convert-to-order="handleConvertToOrder" />
                </div>
            </div>
        </div>

        <!-- <Footer /> -->
    </div>
</template>
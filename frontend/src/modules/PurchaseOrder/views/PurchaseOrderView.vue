<script setup>
import { ref } from 'vue';
import { Card, CardContent, CardHeader, CardTitle } from '@/shared/components/ui/card';
import { Button } from '@/shared/components/ui/button';
import { Badge } from '@/shared/components/ui/badge';
import { Package, ArrowLeft, CheckCircle } from 'lucide-vue-next';
import { useRouter } from 'vue-router';
import Navbar from '@/modules/ProductSearch/components/Navbar.vue';
import Footer from '@/modules/LandingPage/components/Footer.vue';
import QuoteProductItem from '@/modules/Quote/components/QuoteProductItem.vue';
import QuoteSummaryCard from '@/modules/Quote/components/QuoteSummaryCard.vue';
import ClientDetailsCard from '@/modules/Quote/components/ClientDetailsCard.vue';
import QuoteActionsCard from '@/modules/Quote/components/QuoteActionsCard.vue';


const router = useRouter();

// Datos de ejemplo
const orderData = ref({
  orderNumber: 'PO-JOM-2024-00123',
  date: '2024-07-26',
  status: 'Completada',
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
  ],
  shipping: {
    address: 'Av. de los Insurgentes Sur 1500',
    city: 'Ciudad de México',
    postalCode: '03920',
    country: 'México',
    method: 'Envío Estándar'
  },
  payment: {
    method: 'Tarjeta de Crédito (VISA **** 1234)',
    transactionId: 'TXN-JOM-87654321'
  }
});

const subtotal = ref(435.00);
const tax = ref(69.60);
const shipping = ref(15.00);
const total = ref(519.60);

function handleSendEmail() {
  alert('Funcionalidad de imprimir orden');
}

function handleSendWhatsApp() {
  alert('Funcionalidad de enviar por WhatsApp');
}

function handleDownloadPDF() {
  alert('Funcionalidad de descargar PDF');
}

function handleGoBack() {
  router.push('/buscar');
}
</script>

<template>
  <div class="min-h-screen bg-background">
    <div class="w-[90%] md:w-[70%] lg:w-[75%] lg:max-w-screen-xl mx-auto py-8">
      <Navbar />

      <div class="mt-24 mb-8">
        <Button variant="ghost" @click="handleGoBack" class="mb-4 hover:bg-accent">
          <ArrowLeft class="w-4 h-4 mr-2" />
          Regresar
        </Button>

        <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
          <div>
            <h1 class="text-3xl md:text-4xl font-bold">Detalles de la Orden de Compra</h1>
            <p class="text-muted-foreground mt-2">
              Revisa toda la información de tu orden de compra.
            </p>
          </div>
          <Badge variant="secondary" class="bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-100 w-fit">
            <CheckCircle class="w-4 h-4 mr-2" />
            {{ orderData.status }}
          </Badge>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- Sección principal -->
        <div class="lg:col-span-2 space-y-6">
          <!-- Productos -->
          <Card>
            <CardHeader>
              <CardTitle class="flex items-center gap-2">
                <Package class="w-5 h-5" />
                Productos del Pedido
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div class="space-y-4">
                <QuoteProductItem v-for="product in orderData.products" :key="product.id" :product="product" />
              </div>
            </CardContent>
          </Card>

        </div>

        <!-- Sidebar -->
        <div class="space-y-6">
          <!-- Resumen -->
          <QuoteSummaryCard :order-number="orderData.orderNumber" :date="orderData.date" :status="orderData.status"
            :subtotal="subtotal" :tax="tax" :shipping="shipping" :total="total" />

          <!-- Detalles del Cliente -->
          <ClientDetailsCard :client="orderData.client" />

          <!-- Acciones -->
          <QuoteActionsCard :show-convert-button="false" @send-email="handleSendEmail"
            @send-whatsapp="handleSendWhatsApp" @download-pdf="handleDownloadPDF" />
        </div>
      </div>
    </div>

    <Footer />
  </div>
</template>
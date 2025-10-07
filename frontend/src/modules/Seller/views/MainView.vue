<script setup>
import { ref } from 'vue'
import DashboardSidebar from '@/shared/components/DashboardSidebar.vue'
import StatsCard from '@/shared/components/StatsCard.vue'
import {
  LayoutDashboard,
  FileText,
  ShoppingCart,
  Clock,
  CheckCircle,
  XCircle,
  AlertCircle,
  UserRoundPlus
} from 'lucide-vue-next'

const menuItems = [
  {
    title: 'Cotizador',
    url: '/vendedor',
    icon: LayoutDashboard
  },
  {
    title: 'Cotizaciones',
    url: '/vendedor/cotizaciones',
    icon: FileText
  },
  {
    title: 'Pedidos',
    url: '/vendedor/pedidos',
    icon: ShoppingCart
  },
  {
    title: 'Solicitudes',
    url: '/vendedor/solicitudes',
    icon: UserRoundPlus
  }
]
</script>

<template>
  <div>
    <DashboardSidebar :menu-items="menuItems" user-role="SELLER" user-name="José Martin"
      user-email="jose.martin@jom.com">
      <template #header>
        <h1 class="text-lg font-semibold">Vendedor</h1>
      </template>

      <div class="space-y-6">
        <div>
          <h2 class="text-3xl font-bold">Cotizador</h2>
          <p class="text-muted-foreground mt-2">
            Gestiona tus cotizaciones y pedidos desde aquí
          </p>
        </div>


        <div class="mt-8">
          <div class="bg-card rounded-lg border p-8 md:p-12 text-center flex flex-col items-center justify-center">
            <FileText class="w-16 h-16 mx-auto mb-4 text-muted-foreground" />
            <h2 class="text-2xl font-bold mb-2">Cotizador</h2>
          </div>
        </div>
      </div>
    </DashboardSidebar>
  </div>
</template>
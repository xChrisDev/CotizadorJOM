<script setup>
import { ref } from 'vue'
import DashboardSidebar from '@/shared/components/DashboardSidebar.vue'
import StatsCard from '@/shared/components/StatsCard.vue'
import { menuItems } from '../utils/dashboardMenu.js'
import { TrendingUp, UserCheck, UserCog, UserX } from 'lucide-vue-next'

const stats = ref([
  {
    title: 'Usuarios Activos',
    value: '48',
    icon: UserCheck,
    description: 'Usuarios verificados',
    variant: 'success'
  },
  {
    title: 'Pendientes de Verificación',
    value: '7',
    icon: UserCog,
    description: 'Requieren aprobación',
    variant: 'warning'
  },
  {
    title: 'Usuarios Inactivos',
    value: '12',
    icon: UserX,
    description: 'Sin actividad reciente',
    variant: 'danger'
  },
  {
    title: 'Total de Usuarios',
    value: '67',
    icon: TrendingUp,
    description: 'Crecimiento: +12%',
    variant: 'info'
  }
])
</script>

<template>
  <div>
    <DashboardSidebar :menu-items="menuItems" user-role="ADMIN" user-name="Administrador" user-email="admin@jom.com">
      <template #header>
        <h1 class="text-lg font-semibold">Administrador</h1>
      </template>

      <div class="space-y-6">
        <div>
          <h2 class="text-3xl font-bold">Gestión de Usuarios</h2>
          <p class="text-muted-foreground mt-2">
            Administra usuarios, revisa metricas y gestiona el sistema
          </p>
        </div>

        <div class="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
          <StatsCard v-for="stat in stats" :key="stat.title" :title="stat.title" :value="stat.value" :icon="stat.icon"
            :description="stat.description" :variant="stat.variant" />
        </div>

        <div class="mt-8">
          <div
            class="bg-card rounded-lg border p-8 md:p-12 text-center min-h-[400px] flex flex-col items-center justify-center">
            <Settings class="w-16 h-16 mx-auto mb-4 text-muted-foreground" />
            <h2 class="text-2xl font-bold mb-2">Gestión Administrativa</h2>
          </div>
        </div>
      </div>
    </DashboardSidebar>
  </div>
</template>
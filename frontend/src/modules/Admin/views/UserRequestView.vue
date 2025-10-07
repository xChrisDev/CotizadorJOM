<script setup>
import { ref } from 'vue'
import DashboardSidebar from '@/shared/components/DashboardSidebar.vue'
import StatsCard from '@/shared/components/StatsCard.vue'
import { menuItems } from '../utils/dashboardMenu.js'
import {
    LayoutDashboard,
    Users,
    Settings,
    UserCheck,
    UserX,
    UserCog,
    TrendingUp,
    FileText,
    ShoppingCart,
    FileOutput,
    UserRoundPlus
} from 'lucide-vue-next'
import UserRequestTable from '@/shared/components/UserRequestTable.vue'

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
        <DashboardSidebar :menu-items="menuItems" user-role="ADMIN" user-name="Administrador"
            user-email="admin@jom.com">
            <template #header>
                <h1 class="text-lg font-semibold">Administrador</h1>
            </template>

            <div class="space-y-6">
                <div>
                    <h2 class="text-3xl font-bold">Gestión de solicitudes</h2>
                    <p class="text-muted-foreground mt-2">
                        Gestiona las solicitudes entrantes de los usuarios.
                    </p>
                </div>

                <div class="mt-8">
                    <UserRequestTable />
                </div>
            </div>
        </DashboardSidebar>
    </div>
</template>
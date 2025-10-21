<script setup>
import { ref } from 'vue'
import DashboardSidebar from '@/shared/components/DashboardSidebar.vue'
import { menuItems } from '../utils/dashboardMenu.js'
import DashboardPanel from '../components/DashboardPanel.vue'
import UserRequestPanel from '../components/UserRequestPanel.vue'
import CustomerPanel from '../components/CustomerPanel.vue'
import SellerPanel from '../components/SellerPanel.vue'
import PurchasingStaffPanel from '../components/PurchasingStaffPanel.vue'
import QuotePanel from '../components/QuotePanel.vue'

const currentView = ref(localStorage.getItem('sidebarActive') || 'dashboard')

const handleViewChange = (newView) => {
  currentView.value = newView
  localStorage.setItem('sidebarActive', newView)
}

</script>

<template>
  <div>
    <DashboardSidebar @update:view="handleViewChange" :menu-items="menuItems" user-role="ADMIN"
      user-name="Administrador" user-email="admin@jom.com">

      <DashboardPanel v-if="currentView === 'dashboard'" />
      <UserRequestPanel v-if="currentView === 'solicitudes'" />
      <CustomerPanel v-if="currentView === 'clientes'" />
      <SellerPanel v-if="currentView === 'vendedores'" />
      <PurchasingStaffPanel v-if="currentView === 'compras'" />
      <QuotePanel v-if="currentView === 'cotizar'"/>
    </DashboardSidebar>
  </div>
</template>
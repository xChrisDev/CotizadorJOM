<script setup>
import { onMounted, ref } from 'vue'
import DashboardSidebar from '@/shared/components/DashboardSidebar.vue'
import { menuItems } from '../utils/dashboardMenu.js'
import DashboardPanel from '../components/DashboardPanel.vue'
import UserRequestPanel from '../components/UserRequestPanel.vue'
import CustomerPanel from '../components/CustomerPanel.vue'
import SellerPanel from '../components/SellerPanel.vue'
import PurchasingStaffPanel from '../components/PurchasingStaffPanel.vue'
import QuotePanel from '../components/QuotePanel.vue'
import { getProfileUser } from '@/modules/Auth/services/authService.js'
import QuotesListPanel from '../components/QuotesListPanel.vue'
import ArticlesPanel from '../components/ArticlesPanel.vue'

const currentView = ref(localStorage.getItem('sidebarActive') || 'dashboard')
const handleViewChange = (newView) => {
  currentView.value = newView
  localStorage.setItem('sidebarActive', newView)
}

const user = ref({})

async function fetchMe() {
  try {
    user.value = await getProfileUser()
    localStorage.setItem('user_id', user.value.id)
  } catch (error) {
    console.error(error)
  }
}

onMounted(fetchMe)

</script>

<template>
  <div>
    <DashboardSidebar v-if="user && user.role" @update:view="handleViewChange" :menu-items="menuItems"
      :user-role="user.role" :user-name="user.username" :user-email="user.email">

      <DashboardPanel v-if="currentView === 'dashboard'" />
      <UserRequestPanel v-if="currentView === 'solicitudes'" />
      <CustomerPanel v-if="currentView === 'clientes'" />
      <SellerPanel v-if="currentView === 'vendedores'" />
      <PurchasingStaffPanel v-if="currentView === 'compras'" />
      <QuotePanel v-if="currentView === 'cotizar'" />
      <QuotesListPanel v-if="currentView === 'cotizaciones'" />
      <ArticlesPanel v-if="currentView === 'articulos'" />
    </DashboardSidebar>
  </div>
</template>
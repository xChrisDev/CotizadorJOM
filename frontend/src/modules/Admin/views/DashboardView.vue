<script setup>
import { onMounted, ref } from 'vue'
import { menuItems } from '../utils/dashboardMenu.js'
import { getProfileUser } from '@/modules/Auth/services/authService.js'
import { RouterView } from 'vue-router'
import DashboardSidebar from '@/shared/components/DashboardSidebar.vue'

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
      <RouterView />
    </DashboardSidebar>
  </div>
</template>
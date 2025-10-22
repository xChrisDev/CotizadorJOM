<script setup>
import { nextTick, ref } from 'vue'
import { useRouter } from 'vue-router'
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from '@/shared/components/ui/sidebar'
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuSeparator, DropdownMenuTrigger } from '@/shared/components/ui/dropdown-menu'
import { Avatar, AvatarFallback } from '@/shared/components/ui/avatar'
import { Separator } from '@/shared/components/ui/separator'
import { Button } from '@/shared/components/ui/button'
import ThemeButton from '@/shared/components/ThemeButton.vue'
import { ChevronsUpDown, LogOut, User } from 'lucide-vue-next'
import { useAuthStore } from '@/shared/stores/auth.js'
import ShoppingCartButton from '@/modules/ProductSearch/components/ShoppingCartButton.vue'

const props = defineProps({
  menuItems: { type: Array, required: true },
  userRole: { type: String, required: true },
  userName: { type: String, default: 'Usuario' },
  userEmail: { type: String, default: 'usuario@jom.com' }
})

const router = useRouter()
const authStore = useAuthStore()
const emit = defineEmits(["update:view"])
const sidebarTriggerRef = ref(null)
const activeOption = ref(localStorage.getItem('sidebarActive') || '')

const handleClick = (option, toggleSidebar) => {
  activeOption.value = option
  localStorage.setItem('sidebarActive', option)
  emit("update:view", option)

  if (window.innerWidth < 768) {
    nextTick(() => {
      sidebarTriggerRef.value?.$el?.click?.()
    })
  }
}

const getUserRoleLabel = () => {
  const roles = { 'ADMIN': 'Administrador', 'SELLER': 'Vendedor', 'STAFF': 'Compras' }
  return roles[props.userRole] || 'Usuario'
}

const getUserInitials = () => {
  return props.userName.split(' ').map(n => n[0]).join('').toUpperCase().slice(0, 2)
}

const handleLogout = () => {
  authStore.logout()
  router.push('/ingresar')
  localStorage.removeItem('sidebarActive')
  localStorage.removeItem('user_id')
}
</script>

<template>
  <SidebarProvider v-slot="{ toggleSidebar }">
    <Sidebar collapsible="icon">
      <SidebarHeader>
        <div class="flex gap-2 py-2">
          <div
            class="flex aspect-square size-8 items-center justify-center rounded-lg bg-gradient-to-r from-[#4ed636] to-[#09cb6d] text-white">
            <img src="@/shared/assets/JOM.png" alt="JOM" class="h-4" />
          </div>
          <div class="grid flex-1 text-left text-sm leading-tight">
            <span class="truncate font-semibold">JOM</span>
            <span class="truncate text-xs text-muted-foreground">{{ getUserRoleLabel() }}</span>
          </div>
        </div>
      </SidebarHeader>

      <SidebarContent>
        <!-- Menú Principal -->
        <SidebarGroup>
          <SidebarGroupLabel>Menú Principal</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              <SidebarMenuItem v-for="item in menuItems.filter(i => ['dashboard', 'cotizar'].includes(i.option))"
                :key="item.title">
                <SidebarMenuButton as-child :tooltip="item.title" class="py-4">
                  <Button @click="() => handleClick(item.option, toggleSidebar)" variant="ghost"
                    class="flex justify-start gap-2"
                    :class="{ 'bg-sidebar-accent border-[1px] dark:border-gray-700': activeOption === item.option }">
                    <component :is="item.icon" class="w-4 h-4" />
                    <span>{{ item.title }}</span>
                  </Button>
                </SidebarMenuButton>
              </SidebarMenuItem>
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>

        <!-- Gestión de Usuarios -->
        <SidebarGroup>
          <SidebarGroupLabel>Usuarios</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              <SidebarMenuItem
                v-for="item in menuItems.filter(i => ['clientes', 'vendedores', 'compras'].includes(i.option))"
                :key="item.title">
                <SidebarMenuButton as-child :tooltip="item.title" class="py-4">
                  <Button @click="() => handleClick(item.option, toggleSidebar)" variant="ghost"
                    class="flex justify-start gap-2"
                    :class="{ 'bg-sidebar-accent border-[1px] dark:border-gray-700': activeOption === item.option }">
                    <component :is="item.icon" class="w-4 h-4" />
                    <span>{{ item.title }}</span>
                  </Button>
                </SidebarMenuButton>
              </SidebarMenuItem>
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>

        <!-- Solicitudes -->
        <SidebarGroup>
          <SidebarGroupLabel>Solicitudes</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              <SidebarMenuItem v-for="item in menuItems.filter(i => ['solicitudes'].includes(i.option))"
                :key="item.title">
                <SidebarMenuButton as-child :tooltip="item.title" class="py-4">
                  <Button @click="() => handleClick(item.option, toggleSidebar)" variant="ghost"
                    class="flex justify-start gap-2"
                    :class="{ 'bg-sidebar-accent border-[1px] dark:border-gray-700': activeOption === item.option }">
                    <component :is="item.icon" class="w-4 h-4" />
                    <span>{{ item.title }}</span>
                  </Button>
                </SidebarMenuButton>
              </SidebarMenuItem>
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>

        <!-- Reportes / Documentos -->
        <SidebarGroup>
          <SidebarGroupLabel>Reportes / Documentos</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              <SidebarMenuItem
                v-for="item in menuItems.filter(i => ['reportes', 'cotizaciones', 'ordenes'].includes(i.option))"
                :key="item.title">
                <SidebarMenuButton as-child :tooltip="item.title" class="py-4">
                  <Button @click="() => handleClick(item.option, toggleSidebar)" variant="ghost"
                    class="flex justify-start gap-2"
                    :class="{ 'bg-sidebar-accent border-[1px] dark:border-gray-700': activeOption === item.option }">
                    <component :is="item.icon" class="w-4 h-4" />
                    <span>{{ item.title }}</span>
                  </Button>
                </SidebarMenuButton>
              </SidebarMenuItem>
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>


      <SidebarFooter>
        <SidebarMenu>
          <SidebarMenuItem>
            <DropdownMenu>
              <DropdownMenuTrigger as-child>
                <SidebarMenuButton size="lg"
                  class="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground">
                  <Avatar class="h-8 w-8 rounded-lg">
                    <AvatarFallback class="rounded-lg bg-gradient-to-r from-[#4ed636] to-[#09cb6d] text-white">
                      {{ getUserInitials() }}
                    </AvatarFallback>
                  </Avatar>
                  <div class="grid flex-1 text-left text-sm leading-tight">
                    <span class="truncate font-semibold">{{ userName }}</span>
                    <span class="truncate text-xs text-muted-foreground">{{ userEmail }}</span>
                  </div>
                  <ChevronsUpDown class="ml-auto size-4" />
                </SidebarMenuButton>
              </DropdownMenuTrigger>
              <DropdownMenuContent class="w-[--radix-dropdown-menu-trigger-width] min-w-56 rounded-lg" side="bottom"
                align="end" :side-offset="4">
                <DropdownMenuItem @click="router.push('/perfil')" class="cursor-pointer">
                  <User class="mr-2 h-4 w-4" /> Perfil
                </DropdownMenuItem>
                <DropdownMenuSeparator />
                <DropdownMenuItem @click="handleLogout" class="text-red-400 cursor-pointer">
                  <LogOut class="mr-2 h-4 w-4" /> Cerrar Sesión
                </DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarFooter>
    </Sidebar>

    <SidebarInset>
      <header class="flex h-16 shrink-0 items-center gap-2 border-b ps-4 pe-1">
        <SidebarTrigger class="-ml-1" ref="sidebarTriggerRef" />
        <Separator orientation="vertical" class="mr-2 h-4" />
        <div class="flex items-center gap-2 flex-1"></div>
        <div class="flex items-center gap-2">
          <ShoppingCartButton v-if="activeOption === 'cotizar'"/>
          <ThemeButton />
        </div>
      </header>
      <div class="flex flex-1 flex-col gap-4 p-4 md:p-6">
        <slot />
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>

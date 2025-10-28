<script setup lang="ts">
import type { LucideIcon } from "lucide-vue-next"
import { Bell, ChevronRight, FileEdit, LayoutDashboard } from "lucide-vue-next"
import {
    Collapsible,
    CollapsibleContent,
    CollapsibleTrigger,
} from "@/shared/components/ui/collapsible"
import {
    SidebarGroup,
    SidebarGroupLabel,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarMenuSub,
    SidebarMenuSubButton,
    SidebarMenuSubItem,
} from "@/shared/components/ui/sidebar"

defineProps<{
    items: {
        title: string
        url: string
        icon?: LucideIcon
        isActive?: boolean
        items?: {
            title: string
            icon?: LucideIcon
            url: string
        }[]
    }[]
}>()


const handleActive = (item: any) => {
    item.isActive = !item.isActive
}
</script>

<template>
    <SidebarGroup>
        <SidebarGroupLabel>Menu principal</SidebarGroupLabel>
        <SidebarMenu>
            <RouterLink to="/admin/dashboard" class="flex items-center gap-2">
                <SidebarMenuButton tooltip="Dashboard">
                    <LayoutDashboard class="size-4" />
                    <span class="font-medium">Dashboard</span>
                </SidebarMenuButton>
            </RouterLink>
            <RouterLink to="/admin/cotizar" class="flex items-center gap-2">
                <SidebarMenuButton tooltip="Cotizar">
                    <FileEdit class="size-4" />
                    <span class="font-medium">Cotizar</span>
                </SidebarMenuButton>
            </RouterLink>
            <RouterLink to="/admin/solicitudes" class="flex items-center gap-2">
                <SidebarMenuButton tooltip="Solicitudes">
                    <Bell class="size-4" />
                    <span class="font-medium">Solicitudes</span>
                </SidebarMenuButton>
            </RouterLink>
        </SidebarMenu>
    </SidebarGroup>
    <SidebarGroup>
        <SidebarGroupLabel>Gestión del sistema</SidebarGroupLabel>
        <SidebarMenu>
            <Collapsible v-for="item in items" :key="item.title" as-child :default-open="item.isActive"
                class="group/collapsible">
                <SidebarMenuItem>
                    <CollapsibleTrigger as-child>
                        <SidebarMenuButton :tooltip="item.title" @click="handleActive(item)">
                            <component :is="item.icon" v-if="item.icon" />
                            <span class="font-medium">{{ item.title }}</span>
                            <ChevronRight
                                class="ml-auto transition-transform duration-200 group-data-[state=open]/collapsible:rotate-90" />
                        </SidebarMenuButton>
                    </CollapsibleTrigger>
                    <CollapsibleContent>
                        <SidebarMenuSub>
                            <SidebarMenuSubItem v-for="subItem in item.items" :key="subItem.title">
                                <SidebarMenuSubButton as-child>
                                    <RouterLink :to="subItem.url">
                                        <component :is="subItem.icon" v-if="subItem.icon" />
                                        <span>{{ subItem.title }}</span>
                                    </RouterLink>
                                </SidebarMenuSubButton>
                            </SidebarMenuSubItem>
                        </SidebarMenuSub>
                    </CollapsibleContent>
                </SidebarMenuItem>
            </Collapsible>
        </SidebarMenu>
    </SidebarGroup>
</template>

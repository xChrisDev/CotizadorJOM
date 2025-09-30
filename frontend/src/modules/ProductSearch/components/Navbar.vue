<script setup>
import { onMounted, ref } from "vue";
import { useColorMode, useDraggable } from "@vueuse/core";
import {
    NavigationMenu,
    NavigationMenuItem,
    NavigationMenuList,
} from "@/shared/components/ui/navigation-menu";
import {
    Sheet,
    SheetContent,
    SheetFooter,
    SheetHeader,
    SheetTitle,
    SheetTrigger,
} from "@/shared/components/ui/sheet";
import { Button } from "@/shared/components/ui/button";
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from '@/shared/components/ui/tooltip'
import { Separator } from "@/shared/components/ui/separator";
import ThemeButton from "@/shared/components/ThemeButton.vue";
import { Menu, Box, Home, ShoppingBag, User, Mail, Settings, LogInIcon, ShoppingCart } from "lucide-vue-next";
import { RouterLink } from "vue-router";
import ShoppingCartButton from "./ShoppingCartButton.vue";
import LoginButton from "@/shared/components/LoginButton.vue";

const mode = useColorMode();

const routeList = [
    {
        name: "Inicio",
        icon: Home,
        url: "/"
    },
    {
        name: "Productos",
        icon: Box,
        url: "/buscar"
    }
]


const isOpen = ref(false);
</script>

<template>
    <header :class="{
        'shadow-light': mode === 'light',
        'shadow-dark': mode === 'dark',
        'fixed top-0 left-0 right-0 z-998 w-full md:w-[70%] lg:w-[75%] lg:max-w-screen-xl lg:mt-2 mx-auto flex justify-between items-center px-4 py-2 bg-white/80 dark:bg-[#09090b]/70 backdrop-blur-xl transition-all duration-500 shadow-lg hover:shadow-2xl rounded-none md:rounded-2xl':
            true,
    }">

        <!-- Logo -->
        <a href="#" class="font-bold text-lg flex items-center gap-2">
            <img src="@/shared/assets/JOM.png" alt="JOM" class="h-12 md:h-16" />
        </a>

        <!-- Mobile -->
        <div class="flex items-center gap-2 lg:hidden">
            <ShoppingCartButton />
            <Sheet v-model:open="isOpen">
                <SheetTrigger class="flex items-center gap-3" as-child>
                    <Button @click="isOpen = true" variant="outline" size="icon" class="h-14 w-14 lg:hidden">
                        <Menu class="size-6" />
                    </Button>
                </SheetTrigger>

                <SheetContent side="left"
                    class="z-999 flex flex-col justify-between bg-card/90 backdrop-blur-lg border-r">
                    <div>
                        <SheetHeader class="mb-3 ml-2">
                            <SheetTitle class="flex items-center">
                                <a href="/" class="flex items-center gap-2">
                                    <img src="@/shared/assets/JOM.png" alt="JOM" class="rounded-lg h-16" />
                                </a>
                            </SheetTitle>
                            <Separator class="opacity-30 bg-primary" />
                        </SheetHeader>

                        <div class="flex flex-col gap-3 px-4">
                            <LoginButton type="mobile" />
                            <Button v-for="route in routeList" as-child variant="outline"
                                class="h-14 justify-start text-base hover:bg-primary/10 transition-colors duration-200">
                                <RouterLink @click="isOpen = false" :to="route.url" class="flex items-center gap-2">
                                    <component :is="route.icon" class="w-5 h-5" />
                                    {{ route.name }}
                                </RouterLink>
                            </Button>

                        </div>

                    </div>

                    <SheetFooter class="flex-col sm:flex-col justify-start items-start">
                        <Separator class="mb-3 opacity-30 bg-primary" />
                        <ThemeButton />
                    </SheetFooter>
                </SheetContent>
            </Sheet>
        </div>

        <!-- Desktop -->
        <NavigationMenu class="hidden lg:flex">
            <NavigationMenuList class="flex gap-4">
                <NavigationMenuItem v-for="route in routeList">
                    <RouterLink :to="route.url" class="relative flex items-center gap-2 px-3 py-2 text-base font-medium text-foreground hover:text-primary
               after:content-[''] after:absolute after:left-0 after:bottom-0 
               after:h-[3px] after:w-0 after:bg-primary after:transition-all after:duration-300
               hover:after:w-full">
                        <component :is="route.icon" class="w-4 h-4" />
                        {{ route.name }}
                    </RouterLink>
                </NavigationMenuItem>
            </NavigationMenuList>
        </NavigationMenu>

        <div class="hidden lg:flex gap-2">
            <ShoppingCartButton />
            <ThemeButton />
            <LoginButton type="desktop" />
        </div>
    </header>
</template>

<style scoped>
.shadow-light {
    box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.085);
}

.shadow-dark {
    box-shadow: inset 0 0 5px rgba(255, 255, 255, 0.141);
}
</style>

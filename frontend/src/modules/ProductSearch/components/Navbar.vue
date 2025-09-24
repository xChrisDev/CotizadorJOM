<script setup>
import { ref } from "vue";
import { useColorMode } from "@vueuse/core";
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
import { Separator } from "@/shared/components/ui/separator";
import { Box, Home, ShoppingBag } from "lucide-vue-next";
import ThemeButton from "@/shared/components/ThemeButton.vue";
import { User, Mail, Settings, LogInIcon, ShoppingCart } from "lucide-vue-next";
import { RouterLink } from "vue-router";

const mode = useColorMode();
mode.value = "light";

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
        'fixed top-0 left-0 right-0 z-1001 w-full md:w-[70%] lg:w-[75%] lg:max-w-screen-xl lg:mt-2 mx-auto flex justify-between items-center px-4 py-2 bg-white/80 dark:bg-gray-900/70 backdrop-blur-xl transition-all duration-500 shadow-lg hover:shadow-2xl rounded-none md:rounded-2xl':
            true,
    }">

        <!-- Logo -->
        <a href="#" class="font-bold text-lg flex items-center gap-2">
            <img src="@/shared/assets/JOM.png" alt="JOM" class="h-12 w-12 md:h-16 md:w-16" />
            <span class="hidden md:inline-block text-xl font-bold tracking-tight">JOM</span>
        </a>

        <!-- Mobile -->
        <div class="flex items-center lg:hidden">
            <Sheet v-model:open="isOpen">
                <SheetTrigger as-child>
                    <Menu @click="isOpen = true"
                        class="cursor-pointer hover:text-primary transition-colors duration-200" />
                </SheetTrigger>

                <SheetContent side="left"
                    class="z-9999 flex flex-col justify-between rounded-tr-2xl rounded-br-2xl bg-card/90 backdrop-blur-lg border-r">
                    <div>
                        <SheetHeader class="mb-6 ml-2">
                            <SheetTitle class="flex items-center">
                                <a href="/" class="flex items-center gap-2">
                                    <img src="@/shared/assets/JOM.png" alt="JOM" class="rounded-lg h-16 w-16" />
                                    <span class="font-semibold">JOM</span>
                                </a>
                            </SheetTitle>
                            <Button size="lg"
                                class="flex justify-start bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90">
                                <LogInIcon class="size-5" />
                                Ingresar
                            </Button>
                        </SheetHeader>

                        <div class="flex flex-col gap-3 p-4">
                            <Button v-for="{ href, label, icon } in routeList" :key="label" as-child variant="ghost"
                                size="lg"
                                class="justify-start text-base hover:bg-primary/10 transition-colors duration-200">
                                <a @click="isOpen = false" :href="href" class="flex items-center gap-2">
                                    <component :is="icon" class="w-5 h-5" />
                                    {{ label }}
                                </a>
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
            <ThemeButton />
            <!-- <Button size="lg" class="bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90">
                <LogInIcon class="size-5" />
                Ingresar
            </Button> -->
            <Button variant="outline" size="lg" >
                <ShoppingCart class="size-5" />
                Carrito
            </Button>
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

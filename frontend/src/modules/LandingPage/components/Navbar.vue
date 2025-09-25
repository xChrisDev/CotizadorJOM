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
import { Menu, LogInIcon, Box } from "lucide-vue-next";
import ThemeButton from "@/shared/components/ThemeButton.vue";
import { User, Mail, Settings } from "lucide-vue-next";
import { RouterLink } from "vue-router";

const mode = useColorMode();

const routeList = [
    { href: "#services", label: "Servicios", icon: Settings },
    { href: "#about-us", label: "Nosotros", icon: User },
    { href: "#contact", label: "Contacto", icon: Mail },
];


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
                    <Button @click="isOpen = true" variant="outline" size="icon"
                        class="h-14 w-14 lg:hidden">
                        <Menu class="size-6" />
                    </Button>
                </SheetTrigger>

                <SheetContent side="left"
                    class="z-9999 flex flex-col justify-between bg-card/90 backdrop-blur-lg border-r">
                    <div>
                        <SheetHeader class="ml-2">
                            <SheetTitle class="flex items-center">
                                <a href="/" class="flex items-center gap-2">
                                    <img src="@/shared/assets/JOM.png" alt="JOM" class="rounded-lg h-16 w-16" />
                                    <span class="font-semibold">JOM</span>
                                </a>
                            </SheetTitle>
                            <Separator class="my-3 opacity-30 bg-primary" />
                        </SheetHeader>

                        <div class="flex flex-col gap-3 px-4">
                            <Button
                                class="h-14 text-base flex justify-start bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90">
                                <LogInIcon class="size-5" />
                                Ingresar
                            </Button>
                            <Button v-for="route in routeList" as-child variant="outline"
                                class="h-14 justify-start text-base hover:bg-primary/10 transition-colors duration-200">
                                <a @click="isOpen = false" :href="route.href" class="flex items-center gap-2">
                                    <component :is="route.icon" class="w-5 h-5" />
                                    {{ route.label }}
                                </a>
                            </Button>
                            <Button as-child variant="outline"
                                class="h-14 justify-start text-base hover:bg-primary/10 transition-colors duration-200">
                                <RouterLink @click="isOpen = false" to="/buscar" class="flex items-center gap-2">
                                    <component :is="Box" class="w-5 h-5" />
                                    Productos
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
                    <a :href="route.href" class="relative flex items-center gap-2 px-3 py-2 text-base font-medium text-foreground hover:text-primary
               after:content-[''] after:absolute after:left-0 after:bottom-0 
               after:h-[3px] after:w-0 after:bg-primary after:transition-all after:duration-300
               hover:after:w-full">
                        <component :is="route.icon" class="w-4 h-4" />
                        {{ route.label }}
                    </a>
                </NavigationMenuItem>
                <NavigationMenuItem>
                    <RouterLink to="/buscar" class="relative flex items-center gap-2 px-3 py-2 text-base font-medium text-foreground hover:text-primary
               after:content-[''] after:absolute after:left-0 after:bottom-0 
               after:h-[3px] after:w-0 after:bg-primary after:transition-all after:duration-300
               hover:after:w-full">
                        <component :is="Box" class="w-4 h-4" />
                        Productos
                    </RouterLink>
                </NavigationMenuItem>
            </NavigationMenuList>
        </NavigationMenu>

        <div class="hidden lg:flex gap-2">
            <ThemeButton />
            <Button size="lg" class="h-14 bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90">
                <LogInIcon class="size-5" />
                Ingresar
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

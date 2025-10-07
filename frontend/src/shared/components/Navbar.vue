<script setup>
import { ref, computed, onMounted } from "vue";
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
import { Avatar, AvatarFallback } from "./ui/avatar";
import { Menu, Box, Home, User, Mail, Settings } from "lucide-vue-next";
import { RouterLink } from "vue-router";
// import { useUserStore } from "@/shared/stores/user.js";
import ThemeButton from "@/shared/components/ThemeButton.vue";
import LoginButton from "@/shared/components/LoginButton.vue";
import ShoppingCartButton from "@/modules/ProductSearch/components/ShoppingCartButton.vue";

const props = defineProps({
    variant: {
        type: String,
        validator: (value) => ["landing", "app", "auth"].includes(value),
        default: "app",
    }
});

const mode = useColorMode();
const isOpen = ref(false);

// const userStore = useUserStore();

const landingRoutes = [
    { type: 'anchor', href: "#services", label: "Servicios", icon: Settings },
    { type: 'anchor', href: "#about-us", label: "Nosotros", icon: User },
    { type: 'anchor', href: "#contact", label: "Contacto", icon: Mail },
    { type: 'router', url: "/buscar", label: "Productos", icon: Box },
];

const appRoutes = [
    { type: 'router', url: "/", label: "Inicio", icon: Home },
    { type: 'router', url: "/buscar", label: "Productos", icon: Box },
];

const navigationRoutes = computed(() => {
    switch (props.variant) {
        case "landing":
            return landingRoutes;
        case "app":
            return appRoutes;
        case "auth":
            return appRoutes;
        default:
            return appRoutes;
    }
});

// const getUserInitials = (name) => {
//     console.log(name)
//     return name
//         .split(' ')
//         .map(n => n[0])
//         .join('')
//         .toUpperCase()
//         .slice(0, 2)
// }

</script>

<template>
    <header :class="{
        'shadow-light': mode === 'light',
        'shadow-dark': mode === 'dark',
        'fixed top-0 left-0 right-0 z-1001 w-full md:w-[70%] lg:w-[75%] lg:max-w-screen-xl lg:mt-2 mx-auto flex justify-between items-center px-4 py-2 bg-white/80 dark:bg-[#09090b]/70 backdrop-blur-xl transition-all duration-500 shadow-lg hover:shadow-2xl rounded-none md:rounded-2xl':
            true,
    }">

        <a href="/" class="font-bold text-lg flex items-center gap-2">
            <img src="@/shared/assets/JOM.png" alt="JOM" class="h-12 md:h-16" />
        </a>

        <div class="flex items-center gap-2 lg:hidden">
            <ShoppingCartButton v-if="variant === 'app'" />

            <Sheet v-model:open="isOpen">
                <SheetTrigger as-child>
                    <Button @click="isOpen = true" variant="outline" size="icon" class="h-14 w-14 lg:hidden">
                        <Menu class="size-6" />
                    </Button>
                </SheetTrigger>

                <SheetContent side="left"
                    class="z-9999 flex flex-col justify-between bg-card/90 backdrop-blur-lg border-r">
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
                            <LoginButton v-if="variant === 'app' || variant === 'landing'" type="mobile" />

                            <Button v-for="route in navigationRoutes" :key="route.label" as-child variant="outline"
                                class="h-14 justify-start text-base hover:bg-primary/10 transition-colors duration-200">
                                <a v-if="route.type === 'anchor'" @click="isOpen = false" :href="route.href"
                                    class="flex items-center gap-2">
                                    <component :is="route.icon" class="w-5 h-5" />
                                    {{ route.label }}
                                </a>
                                <RouterLink v-else @click="isOpen = false" :to="route.url"
                                    class="flex items-center gap-2">
                                    <component :is="route.icon" class="w-5 h-5" />
                                    {{ route.label }}
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

        <NavigationMenu class="hidden lg:flex">
            <NavigationMenuList class="flex gap-4">
                <NavigationMenuItem v-for="route in navigationRoutes" :key="route.label">
                    <a v-if="route.type === 'anchor'" :href="route.href"
                        class="relative flex items-center gap-2 px-3 py-2 text-base font-medium text-foreground hover:text-primary after:content-[''] after:absolute after:left-0 after:bottom-0 after:h-[3px] after:w-0 after:bg-primary after:transition-all after:duration-300 hover:after:w-full">
                        <component :is="route.icon" class="w-4 h-4" />
                        {{ route.label }}
                    </a>
                    <RouterLink v-else :to="route.url"
                        class="relative flex items-center gap-2 px-3 py-2 text-base font-medium text-foreground hover:text-primary after:content-[''] after:absolute after:left-0 after:bottom-0 after:h-[3px] after:w-0 after:bg-primary after:transition-all after:duration-300 hover:after:w-full">
                        <component :is="route.icon" class="w-4 h-4" />
                        {{ route.label }}
                    </RouterLink>
                </NavigationMenuItem>
            </NavigationMenuList>
        </NavigationMenu>

        <div class="hidden lg:flex gap-2">
            <template v-if="variant === 'app'">
                <ShoppingCartButton />
                <ThemeButton />

                <!-- <Avatar v-if="userStore.user" class="h-8 w-8 rounded-lg">
                    <AvatarFallback class="rounded-lg bg-gradient-to-r from-[#4ed636] to-[#09cb6d] text-white">
                        {{ getUserInitials(user.first_name + " " + user.last_name) }}
                    </AvatarFallback>
                </Avatar> -->

                <LoginButton type="desktop" />
            </template>

            <template v-else-if="variant === 'landing'">
                <ThemeButton />
                <!-- <Avatar v-if="userStore.user" class="h-8 w-8 rounded-lg">
                    <AvatarFallback class="rounded-lg bg-gradient-to-r from-[#4ed636] to-[#09cb6d] text-white">
                        {{ getUserInitials(user.first_name + " " + user.last_name) }}
                    </AvatarFallback>
                </Avatar> -->

                <LoginButton type="desktop" />
            </template>

            <template v-else-if="variant === 'auth'">
                <ThemeButton />
            </template>
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
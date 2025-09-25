<script setup>
import Button from '@/shared/components/ui/button/Button.vue';
import Input from '@/shared/components/ui/input/Input.vue';
import { Search } from 'lucide-vue-next';
</script>

<template>
    <section class="w-[90%] md:w-[70%] lg:w-[75%] lg:max-w-screen-xl mx-auto pb-32">
        <div class="flex flex-col items-center gap-16 text-center pt-10 md:pt-32 mt-12">
            <div>
                <h2 class="text-3xl md:text-4xl font-bold mb-3">
                    Encuentra tus
                    <span class="text-transparent bg-gradient-to-r from-[#4ed636] to-[#048044] bg-clip-text">
                        refacciones
                    </span>
                    al mejor precio
                </h2>

                <p class="text-md text-muted-foreground max-w-3xl mx-auto">
                    Busca entre cientos de productos de las mejores marcas con
                    precios competitivos.
                </p>
            </div>

            <div class="flex items-center justify-center gap-4 w-full">
                <div class="relative w-full max-w-md items-center">
                    <Input id="search" type="text" placeholder="Buscar por nombre..." autocomplete="off"
                        class="pl-10" />
                    <span class="absolute start-0 inset-y-0 flex items-center justify-center px-2">
                        <Search class="size-5 text-muted-foreground" />
                    </span>
                </div>
                <Button size="lg" class="bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90">
                    <Search class="size-5" />
                    <span class="hidden lg:block">Buscar</span>
                </Button>
            </div>
        </div>
    </section>
</template>

<script setup lang="ts">
import { Badge } from "@/shared/components/ui/badge";
import { Button } from "@/shared/components/ui/button";
import { ArrowRight } from "lucide-vue-next";
</script>

<template>
    <section class="w-[90%] md:w-[70%] lg:w-[75%] lg:max-w-screen-xl mx-auto">
        <div class="flex flex-col lg:flex-row items-start lg:items-center gap-10 mx-auto py-20 md:py-32">

            <!-- Texto -->
            <div class="space-y-8 text-left w-full lg:w-1/2">
                <Badge variant="outline" class="text-sm py-2">
                    <span class="mr-1 text-primary">
                        <Badge class="bg-[#3fc029] font-bold">Nuevo</Badge>
                    </span>
                    <span class="font-bold">Cotizador ya disponible!</span>
                </Badge>

                <div class="text-5xl md:text-6xl font-bold">
                    <h1>
                        Obtén tus refacciones en
                        <span class="text-transparent bg-gradient-to-r from-[#4ed636] to-[#048044] bg-clip-text">
                            JOM
                        </span>
                        al mejor precio.
                    </h1>
                </div>

                <p class="text-xl text-muted-foreground">
                    En refaccionaria JOM encontrar y cotizar las piezas que necesitas es rápido, sencillo y preciso.
                    Empieza hoy mismo y optimiza tu cotización.
                </p>

                <div class="space-y-4 md:space-y-0 md:space-x-4">
                    <Button
                        class="w-full lg:w-2/4 font-bold group/arrow bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90 text-lg md:text-xl py-4 md:py-5">
                        Cotizar ahora
                        <ArrowRight class="size-5 ml-2 group-hover/arrow:translate-x-1 transition-transform" />
                    </Button>
                </div>
            </div>

            <!-- Imagen -->
            <div class="relative group w-full lg:w-1/2 mb-8 lg:mb-0">
                <div
                    class="absolute -top-6 right-12 w-[90%] h-12 lg:h-[80%] bg-[#4ed636]/60 blur-3xl rounded-full img-shadow-animation -z-10">
                </div>

                <img class="w-full h-124 object-cover rounded-lg border" src="@/shared/assets/hero-image.jpg"
                    alt="refacciones" />
                <div
                    class="absolute bottom-0 left-0 w-full h-20 md:h-28 bg-gradient-to-b from-background/0 via-background/50 to-background rounded-lg">
                </div>
            </div>
        </div>
    </section>
</template>

<style scoped>
.img-shadow-animation {
    animation-name: img-shadow-animation;
    animation-iteration-count: infinite;
    animation-duration: 2s;
    animation-timing-function: linear;
    animation-direction: alternate;
}

@keyframes img-shadow-animation {
    from {
        opacity: 0.5;
        transform: translateY(30px);
    }

    to {
        opacity: 1;
        transform: translateY(0px);
    }
}
</style>

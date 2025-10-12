<script setup>
import Navbar from "@/shared/components/Navbar.vue";
import { ShieldCheck } from "lucide-vue-next";

const policies = [
    {
        title: "Validez de la cotización",
        description: "Esta cotización es válida por 30 días a partir de la fecha de emisión.",
    },
    {
        title: "Precios",
        description: "Los precios están expresados en M.N. más IVA.",
    },
    {
        title: "Tiempo de entrega",
        description: "La entrega se realiza al día siguiente hábil a partir de la confirmación del pedido (para crédito) o de la confirmación del pago (para contado).",
    },
    {
        title: "Forma de pago",
        description: "Aceptamos pagos en efectivo, transferencia electrónica, tarjeta de débito, tarjeta de crédito, o mediante línea de crédito autorizada.",
    },
    {
        title: "Garantía",
        description: "Debido a la naturaleza de los productos, la garantía no es aplicable en la mayoría de los casos. Consulta con tu vendedor para casos específicos.",
    },
    {
        title: "Transporte y Envío",
        description: "El envío de la mercancía no está incluido en el precio y genera un costo adicional dependiendo del destino y el volumen del pedido.",
    },
    {
        title: "Aceptación de la cotización",
        description: "La confirmación de un pedido basado en esta cotización implica la total conformidad con las condiciones aquí detalladas.",
    },
    {
        title: "Cambios o cancelaciones",
        description: "Solo se aceptan cambios por defecto de fábrica al momento de la entrega. No aplica en partes eléctricas ni en productos cuyo empaque original esté alterado o dañado.",
    },
];

const iconComponent = ShieldCheck;
</script>

<template>
    <div>
        <Navbar variant="app" />
        <section class="bg-gradient-to-b from-gray-50/50 to-white dark:from-gray-900/50 dark:to-background">
            <div class="w-[90%] md:w-[70%] lg:w-[75%] lg:max-w-screen-xl mx-auto py-20 md:py-32">

                <div class="text-center mb-16">
                    <h2 class="text-4xl md:text-5xl font-bold mb-6">
                        Terminos y
                        <span class="text-transparent bg-gradient-to-r from-[#4ed636] to-[#048044] bg-clip-text">
                            Condiciones
                        </span>
                    </h2>
                    <p class="text-xl text-muted-foreground max-w-3xl mx-auto">
                        Para asegurar una transacción transparente y satisfactoria, te pedimos revisar nuestras
                        condiciones
                        generales de cotización.
                    </p>
                </div>

                <div
                    class="max-w-4xl mx-auto bg-white dark:bg-gray-900/50 p-8 md:p-12 rounded-2xl shadow-lg border border-gray-200 dark:border-gray-800">
                    <div class="space-y-8">
                        <div v-for="policy in policies" :key="policy.title" class="flex items-start gap-4">
                            <div class="flex-shrink-0 mt-1">
                                <component :is="iconComponent" class="w-6 h-6 text-[#048044]" />
                            </div>
                            <div>
                                <h3 class="text-lg font-semibold text-foreground">
                                    {{ policy.title }}
                                </h3>
                                <p class="text-muted-foreground leading-relaxed">
                                    {{ policy.description }}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </section>
    </div>
</template>
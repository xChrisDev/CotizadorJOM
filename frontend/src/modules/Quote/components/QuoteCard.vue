<script setup>
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from '@/shared/components/ui/card'
import { DollarSign, User, FileText } from 'lucide-vue-next'
import { Badge } from '@/shared/components/ui/badge'

defineProps({
    quote: {
        type: Object,
        required: true,
        default: () => ({ cliente: 'N/A', cotizaciones: 0, importe: '0' })
    },
    index: {
        type: Number,
        required: true
    }
})
</script>

<template>
    <Card class="w-full bg-card/80 dark:bg-[#18181bd2] border border-border/50
           hover:shadow-xl hover:border-primary/40 transition-all duration-300 
           hover:scale-[1.03] cursor-pointer rounded-2xl">
        <CardHeader class="flex flex-col gap-0">

            <CardTitle class="text-xl font-bold text-primary flex items-center gap-2">
                {{ quote.importe }}
            </CardTitle>

            <CardDescription class="text-xs text-muted-foreground">
                Total de la cotización
            </CardDescription>
        </CardHeader>

        <CardContent class="flex flex-col rounded-2xl space-y-2">
            <div class="flex flex-col gap-2">
                <Badge class="text-xs font-semibold">
                    <User class="w-4 h-4"/>Cliente
                </Badge>
                <p class="flex items-center text-sm">

                    {{ quote.cliente }}
                </p>
            </div>

            <div class="flex flex-col gap-2">
                <Badge class="text-xs font-semibold">
                    <FileText class="w-4 h-4"/>Cotizaciones
                </Badge>
                <p class="flex items-center text-sm">

                    {{ quote.cotizaciones }}
                </p>
            </div>
        </CardContent>
    </Card>
</template>

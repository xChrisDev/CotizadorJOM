<script setup>
import { Badge } from '@/shared/components/ui/badge'
import QuoteCard from './QuoteCard.vue'

defineProps({
    column: {
        type: Object,
        required: true,
        default: () => ({ id: '', title: '', color:'', cards: [] })
    }
})
</script>

<template>
    <div class="flex flex-col p-2 rounded-lg" :class="column.color">
        <h4 class="text-lg font-medium mb-2 flex items-center justify-between pb-2 border-b border-black/20 dark:border-white/30">
            <span>{{ column.title }}</span>
            <Badge class="bg-white text-black text-sm font-semibold">{{ column.cards.length }}</Badge>
        </h4>

        <div class="lg:h-[calc(100vh-300px)] h-[200px] overflow-y-auto p-2 space-y-4">
            <QuoteCard v-for="(card, index) in column.cards" :key="`${column.id}-${index}`" :quote="card"
                :index="index" />
        </div>
    </div>
</template>
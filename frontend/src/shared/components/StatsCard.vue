<script setup>
import { Card, CardContent, CardHeader, CardTitle } from '@/shared/components/ui/card'

defineProps({
  title: {
    type: String,
    required: true
  },
  value: {
    type: [String, Number],
    required: true
  },
  icon: {
    type: Object,
    required: true
  },
  description: {
    type: String,
    default: ''
  },
  variant: {
    type: String,
    default: 'default',
    validator: (value) => ['default', 'success', 'warning', 'danger', 'info'].includes(value)
  }
})

const getVariantClasses = (variant) => {
  const classes = {
    default: 'bg-card',
    success: 'bg-gradient-to-r from-[#4ed636]/50 to-[#09cb6d]/30 border-green-200 dark:border-green-800',
    warning: 'bg-gradient-to-r from-[#FBBF24]/50 to-[#F59E0B]/30 border-yellow-200 dark:border-yellow-800',
    danger: 'bg-gradient-to-r from-[#EF4444]/50 to-[#DC2626]/30 border-red-200 dark:border-red-800',
    info: 'bg-gradient-to-r from-[#3B82F6]/50 to-[#2563EB]/30 border-blue-200 dark:border-blue-800'
  }
  return classes[variant]
}

const getIconClasses = (variant) => {
  const classes = {
    default: 'text-primary',
    success: 'text-green-600 dark:text-green-400',
    warning: 'text-yellow-600 dark:text-yellow-400',
    danger: 'text-red-600 dark:text-red-400',
    info: 'text-blue-600 dark:text-blue-400'
  }
  return classes[variant]
}
</script>

<template>
  <Card :class="getVariantClasses(variant)">
    <CardHeader class="flex flex-row items-center justify-between">
      <CardTitle class="text-md font-medium">
        {{ title }}
      </CardTitle>
      <component :is="icon" :class="['w-5 h-5', getIconClasses(variant)]" />
    </CardHeader>
    <CardContent>
      <div class="text-3xl font-bold">{{ value }}</div>
      <p v-if="description" class="text-xs text-muted-foreground mt-1">
        {{ description }}
      </p>
    </CardContent>
  </Card>
</template>
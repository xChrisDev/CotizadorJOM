<script setup>
import { Button } from '@/shared/components/ui/button'
import { LogInIcon } from 'lucide-vue-next'
import { useRouter } from 'vue-router'

const router = useRouter()
const props = defineProps({
    type: {
        type: String,
        required: true
    }
})

</script>
<template>
    <div>
        <div v-if="type === 'desktop'">
            <Button @click="router.push('/ingresar')" size="lg"
                class="h-14 bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90">
                <LogInIcon class="size-5" />
                Ingresar
            </Button>
        </div>
        <div v-else-if="type === 'mobile'" class="w-full">
            <Button @click="router.push('/ingresar')"
                class="w-full h-14 text-base flex justify-start bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90">
                <LogInIcon class="size-5" />
                Ingresar
            </Button>
        </div>
    </div>
</template>

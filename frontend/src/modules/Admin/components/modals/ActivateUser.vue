<script setup>
import { ref } from "vue"
import { Ban, Check } from "lucide-vue-next"
import { useToast } from "vue-toastification"
import { Button } from "@/shared/components/ui/button"
import {
    Dialog,
    DialogClose,
    DialogContent,
    DialogDescription,
    DialogFooter,
    DialogHeader,
    DialogTitle,
    DialogTrigger,
} from "@/shared/components/ui/dialog"
import { Card, CardContent } from "@/shared/components/ui/card"
import { fetchUserById, patchUser } from "@/modules/Admin/services/userService.js"
import { Avatar, AvatarFallback } from "@/shared/components/ui/avatar"

const toast = useToast()
const user = ref(null)
const loading = ref(false)

const props = defineProps({
    id: { type: Number, required: true },
    role: { type: String, required: true },
})

const emit = defineEmits(["update"])

const fetchUser = async () => {
    try {
        loading.value = true
        const data = await fetchUserById(props.id)
        user.value = data
    } catch (error) {
        toast.error("Error al obtener la información del usuario.")
        console.error(error)
    } finally {
        loading.value = false
    }
}

const submit = async () => {
    const data = {
        status: "ACTIVE"
    }
    try {
        await patchUser(props.id, data)
        toast.info(`El ${props.role} ha sido reactivado`)
        emit('update')
    } catch (error) {
        console.error(error)
    }
}

const getUserInitials = () => {
    if (!user.value) return "??"

    const first = user.value.first_name?.toUpperCase().slice(0, 1) || ""
    const last = user.value.last_name?.toUpperCase().slice(0, 1) || ""

    return (first + last) || "??"
}

</script>

<template>
    <Dialog>
        <DialogTrigger as-child>
            <Button @click="fetchUser" class="bg-[#4ed636] hover:bg-[#4ed636]/80" size="icon">
                <Check class="size-5" />
            </Button>
        </DialogTrigger>

        <DialogContent class="sm:max-w-[440px]">
            <DialogHeader>
                <DialogTitle>¿Reactivar {{ props.role }}?</DialogTitle>
                <DialogDescription>
                    <p class="text-sm pt-2 text-muted-foreground">
                        Esta acción solo se puede revertir por el administrador del sistema.
                    </p>
                </DialogDescription>
            </DialogHeader>

            <div v-if="loading" class="text-center py-6 text-sm text-muted-foreground">
                Cargando información...
            </div>

            <div v-else-if="user" class="">
                <div class="flex items-center gap-3 p-2 border rounded-lg border-gray-200 dark:border-gray-800">
                    <Avatar class="w-16 h-16 rounded-full">
                        <AvatarFallback class="rounded-full border-2 text-black">
                            {{ getUserInitials() }}
                        </AvatarFallback>
                    </Avatar>
                    <div class="flex flex-col gap-1">
                        <p class="font-semibold text-lg">{{ user.first_name }} {{ user.last_name }}</p>
                        <p class="text-sm text-gray-600">{{ user.email || "Sin email" }}</p>
                        <p class="text-sm text-gray-600">{{ user.phone_number || "Sin teléfono" }}</p>
                    </div>
                </div>
            </div>

            <DialogFooter class="sm:justify-end gap-2 pt-6">
                <DialogClose as-child>
                    <Button variant="outline">Cancelar</Button>
                </DialogClose>

                <Button type="button"
                    class="bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90"
                    @click="submit">
                    Confirmar
                </Button>
            </DialogFooter>
        </DialogContent>
    </Dialog>
</template>

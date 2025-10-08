<script setup>
import { ref, reactive, onMounted, watch } from "vue"
import { z } from "zod"
import { Button } from "@/shared/components/ui/button"
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogFooter,
    DialogHeader,
    DialogTitle,
    DialogTrigger,
} from "@/shared/components/ui/dialog"
import { Label } from "@/shared/components/ui/label"
import { Input } from "@/shared/components/ui/input"
import { PencilLine } from "lucide-vue-next"
import { fetchSellerByID, putSeller } from "../../services/sellerService.js"

const props = defineProps({
    id: Number
})

const seller = ref(null)

const form = reactive({
    first_name: "",
    last_name: "",
    username: "",
    email: "",
    phone_number: "",
    workstation: "",
})

const errors = reactive({
    first_name: null,
    last_name: null,
    username: null,
    email: null,
    phone_number: null,
    workstation: null,
})

const schema = z.object({
    first_name: z.string().min(2, "El nombre debe tener al menos 2 caracteres"),
    last_name: z.string().min(2, "El apellido debe tener al menos 2 caracteres"),
    username: z.string().min(3, "El usuario debe tener al menos 3 caracteres"),
    email: z.string().email("Correo electrónico no válido"),
    phone_number: z
        .string()
        .regex(/^\+?\d{10,15}$/, "Número telefónico inválido"),
    workstation: z.string().min(3, "La estación de trabajo es obligatoria"),
})

watch(seller, (newSeller) => {
    if (newSeller) {
        form.first_name = newSeller.profile.user.first_name
        form.last_name = newSeller.profile.user.last_name
        form.username = newSeller.profile.user.username
        form.email = newSeller.profile.user.email
        form.phone_number = newSeller.profile.phone_number
        form.workstation = newSeller.workstation
    }
})

onMounted(async () => {
    const values = await fetchSellerByID(props.id)
    seller.value = values
})

const submitForm = async () => {
    const result = schema.safeParse(form)
    Object.keys(errors).forEach((key) => (errors[key] = null))

    if (!result.success) {
        result.error.issues.forEach((issue) => {
            const field = issue.path[0]
            errors[field] = issue.message
        })
        return
    }

    try {
        const response = await putSeller(props.id, JSON.stringify(form))
        console.log(response)
    } catch (err) {
        console.error("Error al guardar:", err)
    }
}
</script>


<template>
    <Dialog>
        <DialogTrigger as-child>
            <Button class="bg-gradient-to-r from-[#FBBF24] to-[#F59E0B]" size="icon">
                <PencilLine class="size-5" />
            </Button>
        </DialogTrigger>

        <DialogContent class="sm:max-w-[500px]">
            <DialogHeader>
                <DialogTitle>Editar perfil</DialogTitle>
                <DialogDescription>
                    Modifica la información del vendedor y guarda los cambios.
                </DialogDescription>
            </DialogHeader>

            <div class="grid gap-4 py-4">
                <!-- Nombre -->
                <div class="grid grid-cols-4 items-center gap-4">
                    <Label for="first_name" class="text-right">Nombre</Label>
                    <div class="col-span-3">
                        <Input id="first_name" v-model="form.first_name" />
                        <p v-if="errors.first_name" class="text-red-500 text-sm">
                            {{ errors.first_name }}
                        </p>
                    </div>
                </div>

                <!-- Apellido -->
                <div class="grid grid-cols-4 items-center gap-4">
                    <Label for="last_name" class="text-right">Apellido</Label>
                    <div class="col-span-3">
                        <Input id="last_name" v-model="form.last_name" />
                        <p v-if="errors.last_name" class="text-red-500 text-sm">
                            {{ errors.last_name }}
                        </p>
                    </div>
                </div>

                <!-- Usuario -->
                <div class="grid grid-cols-4 items-center gap-4">
                    <Label for="username" class="text-right">Usuario</Label>
                    <div class="col-span-3">
                        <Input id="username" v-model="form.username" />
                        <p v-if="errors.username" class="text-red-500 text-sm">
                            {{ errors.username }}
                        </p>
                    </div>
                </div>

                <!-- Email -->
                <div class="grid grid-cols-4 items-center gap-4">
                    <Label for="email" class="text-right">Email</Label>
                    <div class="col-span-3">
                        <Input id="email" type="email" v-model="form.email" />
                        <p v-if="errors.email" class="text-red-500 text-sm">
                            {{ errors.email }}
                        </p>
                    </div>
                </div>

                <!-- Teléfono -->
                <div class="grid grid-cols-4 items-center gap-4">
                    <Label for="phone_number" class="text-right">Teléfono</Label>
                    <div class="col-span-3">
                        <Input id="phone_number" v-model="form.phone_number" />
                        <p v-if="errors.phone_number" class="text-red-500 text-sm">
                            {{ errors.phone_number }}
                        </p>
                    </div>
                </div>

                <!-- Estación de trabajo -->
                <div class="grid grid-cols-4 items-center gap-4">
                    <Label for="workstation" class="text-right">Estación</Label>
                    <div class="col-span-3">
                        <Input id="workstation" v-model="form.workstation" />
                        <p v-if="errors.workstation" class="text-red-500 text-sm">
                            {{ errors.workstation }}
                        </p>
                    </div>
                </div>
            </div>

            <DialogFooter>
                <Button type="button" @click="submitForm">
                    Guardar cambios
                </Button>
            </DialogFooter>
        </DialogContent>
    </Dialog>
</template>

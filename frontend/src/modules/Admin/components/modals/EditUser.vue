<script setup>
import { ref, reactive, onMounted } from "vue"
import { z } from "zod"
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
import { Label } from "@/shared/components/ui/label"
import { Input } from "@/shared/components/ui/input"
import { CircleCheckBig, PencilLine } from "lucide-vue-next"
import { fetchUserById, patchUser } from "@/modules/Admin/services/userService.js"
import { useToast } from "vue-toastification"

const toast = useToast()
const props = defineProps({
    id: { type: Number, required: true },
    role: { type: String, required: true },
})
const emit = defineEmits(["update"])

const form = ref({
    first_name: "",
    last_name: "",
    username: "",
    email: "",
    phone_number: "",
})

const errors = reactive({
    first_name: null,
    last_name: null,
    username: null,
    email: null,
    phone_number: null,
})

const schema = z.object({
    username: z.string().min(3, { message: "Debe tener al menos 3 caracteres." }),
    first_name: z.string().min(2, { message: "El nombre es demasiado corto." }),
    last_name: z.string().min(2, { message: "El apellido es demasiado corto." }),
    email: z.string().email({ message: "El formato del correo no es válido." }),
    phone_number: z.string().regex(/^\d{10}$/, { message: "Debe ser un número de 10 dígitos." }),
})

const fetchUser = async () => {
    try {
        const data = await fetchUserById(props.id)
        form.value = data
    } catch (error) {
        toast.error("Error al obtener la información del usuario.")
        console.error(error)
    }
}
const submitForm = async () => {
    const result = schema.safeParse(form.value)
    Object.keys(errors).forEach((key) => (errors[key] = null))

    if (!result.success) {
        result.error.issues.forEach((issue) => {
            const field = issue.path[0]
            errors[field] = issue.message
        })
        return
    }

    try {
        const data = { ...form.value }
        data.phone_number = "+52" + data.phone_number
        console.log(data)
        await patchUser(props.id, data)

        toast.success(`${props.role} actualizado correctamente.`, {
            position: "top-right",
            icon: CircleCheckBig,
        })

        emit("update")
    } catch (err) {
        if (err.response.data) {
            for (let field in err.response.data) {
                err.response.data[field].forEach(msg => {
                    toast.error(msg, { position: "top-right" })
                })
            }
        } else {
            toast.error("Error al actualizar el usuario.")
        }
    }
}
</script>


<template>
    <Dialog>
        <DialogTrigger as-child>
            <Button @click="fetchUser" class="bg-yellow-500 hover:bg-orange-400" size="icon">
                <PencilLine class="size-5" />
            </Button>
        </DialogTrigger>

        <DialogContent class="sm:max-w-[500px]">
            <DialogHeader>
                <DialogTitle>
                    <div class="w-fit py-1 font-medium">
                        Editar perfil</div>
                </DialogTitle>
                <DialogDescription>
                    Modifica la información del {{ props.role }} y guarda los cambios.
                </DialogDescription>
            </DialogHeader>

            <div class="grid gap-4 py-4">
                <!-- Nombre -->
                <div class="grid gap-2">
                    <Label for="first_name" class="text-right">Nombre</Label>
                    <div>
                        <Input autocomplete="off" id="first_name" v-model="form.first_name" />
                        <p v-if="errors.first_name" class="text-red-500 text-sm">
                            {{ errors.first_name }}
                        </p>
                    </div>
                </div>

                <!-- Apellido -->
                <div class="grid gap-2">
                    <Label for="last_name" class="text-right">Apellido</Label>
                    <div>
                        <Input autocomplete="off" id="last_name" v-model="form.last_name" />
                        <p v-if="errors.last_name" class="text-red-500 text-sm">
                            {{ errors.last_name }}
                        </p>
                    </div>
                </div>

                <!-- Usuario -->
                <div class="grid gap-2">
                    <Label for="username" class="text-right">Usuario</Label>
                    <div>
                        <Input autocomplete="off" id="username" v-model="form.username" />
                        <p v-if="errors.username" class="text-red-500 text-sm">
                            {{ errors.username }}
                        </p>
                    </div>
                </div>

                <!-- Email -->
                <div class="grid gap-2">
                    <Label for="email" class="text-right">Email</Label>
                    <div>
                        <Input autocomplete="off" id="email" type="email" v-model="form.email" />
                        <p v-if="errors.email" class="text-red-500 text-sm">
                            {{ errors.email }}
                        </p>
                    </div>
                </div>

                <!-- Numero Telefonico -->
                <div class="grid gap-2">
                    <Label for="phone_number" class="text-right">Número de telefono</Label>
                    <div>
                        <Input autocomplete="off" id="phone_number" v-model="form.phone_number" />
                        <p v-if="errors.phone_number" class="text-red-500 text-sm">
                            {{ errors.phone_number }}
                        </p>
                    </div>
                </div>
            </div>

            <DialogFooter>
                <DialogClose as-child>
                    <Button type="button" variant="outline">
                        Cancelar
                    </Button>
                </DialogClose>
                <Button class="bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90" type="button"
                    @click="submitForm">
                    Guardar cambios
                </Button>
            </DialogFooter>
        </DialogContent>
    </Dialog>
</template>

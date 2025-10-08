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
import { CircleCheckBig, PencilLine } from "lucide-vue-next"
import { fetchSellerByID, putSeller } from "../../services/sellerService.js"
import { useToast } from "vue-toastification"
const toast = useToast()

const props = defineProps({
    id: Number
})

const seller = ref(null)
const emit = defineEmits(["update"])
const form = reactive({
    first_name: "",
    last_name: "",
    username: "",
    email: "",
    workstation: "",
})

const errors = reactive({
    first_name: null,
    last_name: null,
    username: null,
    email: null,
    workstation: null,
})

const schema = z.object({
    first_name: z.string().min(2, "El nombre debe tener al menos 2 caracteres"),
    last_name: z.string().min(2, "El apellido debe tener al menos 2 caracteres"),
    username: z.string().min(3, "El usuario debe tener al menos 3 caracteres"),
    email: z.string().email("Correo electrónico no válido"),
    workstation: z.string().min(3, "La estación de trabajo es obligatoria"),
})

watch(seller, (newSeller) => {
    if (newSeller) {
        form.first_name = newSeller.user.first_name
        form.last_name = newSeller.user.last_name
        form.username = newSeller.user.username
        form.email = newSeller.user.email
        form.workstation = newSeller.workstation
    }
})

const fetchSeller = async () => {
    const values = await fetchSellerByID(props.id)
    seller.value = values
}

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
        const data = {
            user: {
                username: form.username,
                first_name: form.first_name,
                last_name: form.last_name,
                email: form.email
            },
            workstation: form.workstation
        }
        const response = await putSeller(props.id, data)
        toast.success("Vendedor actualizado.", {
            position: "top-center",
            icon: CircleCheckBig,
        })
        emit("update")
    } catch (err) {
        for (let field in err.response.data.user) {
            const messages = err.response.data.user[field];
            messages.forEach(msg => {
                toast.error(msg, { position: "top-center" });
            });
        }
    }
}
</script>


<template>
    <Dialog>
        <DialogTrigger as-child>
            <Button @click="fetchSeller" class="bg-gradient-to-r from-[#FBBF24] to-[#F59E0B]" size="icon">
                <PencilLine class="size-5" />
            </Button>
        </DialogTrigger>

        <DialogContent class="sm:max-w-[500px]">
            <DialogHeader>
                <DialogTitle>
                    <div
                        class="w-fit px-2 py-1 rounded-sm bg-gradient-to-r from-[#FBBF24] to-[#F59E0B] font-medium text-white dark:text-black">
                        Editar perfil</div>
                </DialogTitle>
                <DialogDescription>
                    Modifica la información del vendedor y guarda los cambios.
                </DialogDescription>
            </DialogHeader>

            <div class="grid gap-4 py-4">
                <!-- Nombre -->
                <div class="grid gap-2">
                    <Label for="first_name" class="text-right">Nombre</Label>
                    <div>
                        <Input id="first_name" v-model="form.first_name" />
                        <p v-if="errors.first_name" class="text-red-500 text-sm">
                            {{ errors.first_name }}
                        </p>
                    </div>
                </div>

                <!-- Apellido -->
                <div class="grid gap-2">
                    <Label for="last_name" class="text-right">Apellido</Label>
                    <div>
                        <Input id="last_name" v-model="form.last_name" />
                        <p v-if="errors.last_name" class="text-red-500 text-sm">
                            {{ errors.last_name }}
                        </p>
                    </div>
                </div>

                <!-- Usuario -->
                <div class="grid gap-2">
                    <Label for="username" class="text-right">Usuario</Label>
                    <div>
                        <Input id="username" v-model="form.username" />
                        <p v-if="errors.username" class="text-red-500 text-sm">
                            {{ errors.username }}
                        </p>
                    </div>
                </div>

                <!-- Email -->
                <div class="grid gap-2">
                    <Label for="email" class="text-right">Email</Label>
                    <div>
                        <Input id="email" type="email" v-model="form.email" />
                        <p v-if="errors.email" class="text-red-500 text-sm">
                            {{ errors.email }}
                        </p>
                    </div>
                </div>

                <!-- Estación de trabajo -->
                <div class="grid gap-2">
                    <Label for="workstation" class="text-right">Estación</Label>
                    <div>
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

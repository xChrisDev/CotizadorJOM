<script setup>
import { ref, reactive, onMounted, computed } from "vue"
import { z } from "zod"
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
import { Label } from "@/shared/components/ui/label"
import { Input } from "@/shared/components/ui/input"
import {
  CircleCheckBig,
  PencilLine,
  User,
  IdCard,
  UserRound,
  Store,
  ShoppingCart,
  Mail,
  Phone,
  LoaderCircle,
} from "lucide-vue-next"
import { fetchUserById, patchUser } from "@/modules/Admin/services/userService.js"

const toast = useToast()
const props = defineProps({
  id: { type: Number, required: true },
  role: { type: String, required: true },
})
const emit = defineEmits(["update"])
const isLoading = ref(false)

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

// Icono dinámico según rol
const roleIcon = computed(() => {
  switch (props.role.toLowerCase()) {
    case "vendedor": return Store
    case "cliente": return UserRound
    case "compras": return ShoppingCart
    default: return User
  }
})

const fetchUser = async () => {
  try {
    const data = await fetchUserById(props.id)
    form.value = data

    form.value.phone_number = form.value.phone_number.replace(/^\+52/, "") 
  } catch (error) {
    toast.error("Error al obtener la información del usuario.")
    console.error(error)
  }
}

const onSubmit = async () => {
  const result = schema.safeParse(form.value)
  Object.keys(errors).forEach(key => (errors[key] = null))

  if (!result.success) {
    result.error.issues.forEach(issue => {
      const field = issue.path[0]
      errors[field] = issue.message
    })
    return
  }

  try {
    isLoading.value = true
    const data = { ...form.value }
    data.phone_number = "+52" + data.phone_number

    await patchUser(props.id, data)
    toast.success(`${props.role} actualizado correctamente.`, {
      position: "top-right",
      icon: CircleCheckBig,
    })
    emit("update")
  } catch (err) {
    if (err.response?.data) {
      for (let field in err.response.data) {
        err.response.data[field].forEach(msg => toast.error(msg))
      }
    } else {
      toast.error("Error al actualizar el usuario.")
    }
  } finally {
    isLoading.value = false
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

    <DialogContent class="sm:max-w-[480px] rounded-2xl shadow-xl border border-border/40 backdrop-blur-md">
      <DialogHeader class="text-center">
        <div class="flex justify-center mb-2">
          <component :is="roleIcon" class="size-10 text-green-500" />
        </div>
        <DialogTitle class="text-2xl font-semibold">
          Editar {{ props.role }}
        </DialogTitle>
        <DialogDescription class="text-muted-foreground text-sm">
          Modifica la información del {{ props.role.toLowerCase() }} y guarda los cambios.
        </DialogDescription>
      </DialogHeader>

      <form @submit.prevent="onSubmit" class="grid gap-4 py-4">
        <!-- Nombre -->
        <div class="relative">
          <IdCard class="absolute left-3 top-3 text-muted-foreground size-4" />
          <Input autocomplete="off" v-model="form.first_name" placeholder="Nombre(s)" class="pl-9" />
          <p v-if="errors.first_name" class="text-red-500 text-xs mt-1">{{ errors.first_name }}</p>
        </div>

        <!-- Apellido -->
        <div class="relative">
          <UserRound class="absolute left-3 top-3 text-muted-foreground size-4" />
          <Input autocomplete="off" v-model="form.last_name" placeholder="Apellido(s)" class="pl-9" />
          <p v-if="errors.last_name" class="text-red-500 text-xs mt-1">{{ errors.last_name }}</p>
        </div>

        <!-- Usuario -->
        <div class="relative">
          <User class="absolute left-3 top-3 text-muted-foreground size-4" />
          <Input autocomplete="off" v-model="form.username" placeholder="Usuario" class="pl-9" />
          <p v-if="errors.username" class="text-red-500 text-xs mt-1">{{ errors.username }}</p>
        </div>

        <!-- Email -->
        <div class="relative">
          <Mail class="absolute left-3 top-3 text-muted-foreground size-4" />
          <Input autocomplete="off" type="email" v-model="form.email" placeholder="Correo electrónico" class="pl-9" />
          <p v-if="errors.email" class="text-red-500 text-xs mt-1">{{ errors.email }}</p>
        </div>

        <!-- Teléfono -->
        <div class="relative">
          <Phone class="absolute left-3 top-3 text-muted-foreground size-4" />
          <Input autocomplete="off" v-model="form.phone_number" placeholder="Ej. 4931234567" class="pl-9" />
          <p v-if="errors.phone_number" class="text-red-500 text-xs mt-1">{{ errors.phone_number }}</p>
        </div>

        <DialogFooter class="pt-6 flex justify-end gap-3">
          <DialogClose as-child>
            <Button type="button" variant="outline" class="rounded-xl">Cancelar</Button>
          </DialogClose>

          <Button type="submit" :disabled="isLoading" class="rounded-xl bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90">
            <LoaderCircle v-if="isLoading" class="mr-2 h-4 w-4 animate-spin" />
            {{ isLoading ? "Guardando..." : "Guardar cambios" }}
          </Button>
        </DialogFooter>
      </form>
    </DialogContent>
  </Dialog>
</template>

<script setup>
import { ref, computed } from "vue"
import { useForm } from "vee-validate"
import { toTypedSchema } from "@vee-validate/zod"
import * as z from "zod"
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
  LoaderCircle,
  Plus,
  User,
  Mail,
  Lock,
  Phone,
  IdCard,
  UserRound,
  Store,
  ShoppingCart,
} from "lucide-vue-next"
import { useToast } from "vue-toastification"
import { registerUser } from "@/modules/Auth/services/authService.js"

const toast = useToast()

const props = defineProps({
  role: { type: String, required: true },
})
const emit = defineEmits(["update"])
const isLoading = ref(false)

// Ícono dinámico según el rol
const roleIcon = computed(() => {
  switch (props.role.toLowerCase()) {
    case "vendedor":
      return Store
    case "cliente":
      return UserRound
    case "compras":
      return ShoppingCart
    default:
      return User
  }
})

// Validación con zod
const formSchema = toTypedSchema(
  z.object({
    username: z.string().min(3, { message: "Debe tener al menos 3 caracteres." }),
    firstName: z.string().min(2, { message: "El nombre es demasiado corto." }),
    lastName: z.string().min(2, { message: "El apellido es demasiado corto." }),
    email: z.string().email({ message: "El formato del correo no es válido." }),
    password: z.string().min(8, { message: "Debe tener al menos 8 caracteres." }),
    phoneNumber: z.string().regex(/^\d{10}$/, { message: "Debe ser un número de 10 dígitos." }),
  })
)

const { handleSubmit, defineField, errors, resetForm } = useForm({
  validationSchema: formSchema,
})

const [username, usernameAttrs] = defineField("username")
const [firstName, firstNameAttrs] = defineField("firstName")
const [lastName, lastNameAttrs] = defineField("lastName")
const [email, emailAttrs] = defineField("email")
const [password, passwordAttrs] = defineField("password")
const [phoneNumber, phoneNumberAttrs] = defineField("phoneNumber")

const onSubmit = handleSubmit(async (values) => {
  isLoading.value = true
  try {
    const userData = {
      username: values.username,
      first_name: values.firstName,
      last_name: values.lastName,
      email: values.email,
      password: values.password,
      phone_number: "+52" + values.phoneNumber,
      role: props.role,
    }

    const response = await registerUser(userData)

    if (!response.success) {
      for (let field in response.errors) {
        response.errors[field].forEach(msg => toast.error(msg))
      }
      isLoading.value = false
      return
    }

    toast.success(`${props.role} registrado correctamente.`, {
      icon: CircleCheckBig,
      position: "top-center",
    })

    emit("update")
    resetForm()
  } catch (error) {
    toast.error("Error al registrar el usuario.")
  } finally {
    isLoading.value = false
  }
})
</script>

<template>
  <Dialog>
    <DialogTrigger as-child>
      <Button class="bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90 shadow-md">
        <Plus class="size-4 mr-1" />
        Nuevo
      </Button>
    </DialogTrigger>

    <DialogContent class="sm:max-w-[480px] rounded-2xl shadow-xl border border-border/40 backdrop-blur-md">
      <DialogHeader class="text-center">
        <div class="flex justify-center mb-2">
          <component :is="roleIcon" class="size-10 text-green-500" />
        </div>
        <DialogTitle class="text-2xl font-semibold">
          Registrar {{ props.role }}
        </DialogTitle>
        <DialogDescription class="text-muted-foreground text-sm">
          Completa la información para agregar un nuevo {{ props.role.toLowerCase() }}.
        </DialogDescription>
      </DialogHeader>

      <form @submit.prevent="onSubmit" class="grid gap-4 py-4">
        <!-- Username -->
        <div class="relative">
          <User class="absolute left-3 top-3 text-muted-foreground size-4" />
          <Input id="username" v-model="username" v-bind="usernameAttrs" placeholder="Nombre de usuario" class="pl-9"
            autocomplete="off" />
          <p v-if="errors.username" class="text-red-500 text-xs mt-1">{{ errors.username }}</p>
        </div>

        <!-- Nombre -->
        <div class="relative">
          <IdCard class="absolute left-3 top-3 text-muted-foreground size-4" />
          <Input id="first-name" v-model="firstName" v-bind="firstNameAttrs" placeholder="Nombre(s)" class="pl-9"
            autocomplete="off" />
          <p v-if="errors.firstName" class="text-red-500 text-xs mt-1">{{ errors.firstName }}</p>
        </div>

        <!-- Apellido -->
        <div class="relative">
          <UserRound class="absolute left-3 top-3 text-muted-foreground size-4" />
          <Input id="last-name" v-model="lastName" v-bind="lastNameAttrs" placeholder="Apellidos" class="pl-9"
            autocomplete="off" />
          <p v-if="errors.lastName" class="text-red-500 text-xs mt-1">{{ errors.lastName }}</p>
        </div>

        <!-- Email -->
        <div class="relative">
          <Mail class="absolute left-3 top-3 text-muted-foreground size-4" />
          <Input id="email" type="email" v-model="email" v-bind="emailAttrs" placeholder="Correo electrónico"
            class="pl-9" autocomplete="off" />
          <p v-if="errors.email" class="text-red-500 text-xs mt-1">{{ errors.email }}</p>
        </div>

        <!-- Contraseña -->
        <div class="relative">
          <Lock class="absolute left-3 top-3 text-muted-foreground size-4" />
          <Input id="password" type="password" v-model="password" v-bind="passwordAttrs" placeholder="Contraseña"
            class="pl-9" autocomplete="off" />
          <p v-if="errors.password" class="text-red-500 text-xs mt-1">{{ errors.password }}</p>
        </div>

        <!-- Teléfono -->
        <div class="relative">
          <Phone class="absolute left-3 top-3 text-muted-foreground size-4" />
          <Input id="phone-number" v-model="phoneNumber" v-bind="phoneNumberAttrs" placeholder="Ej. 4931234567"
            class="pl-9" autocomplete="off" />
          <p v-if="errors.phoneNumber" class="text-red-500 text-xs mt-1">{{ errors.phoneNumber }}</p>
        </div>

        <DialogFooter class="pt-6 flex justify-end gap-3">
          <DialogClose as-child>
            <Button type="button" variant="outline" class="rounded-xl">
              Cancelar
            </Button>
          </DialogClose>

          <Button :disabled="isLoading" type="submit"
            class="rounded-xl bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90">
            <LoaderCircle v-if="isLoading" class="mr-2 h-4 w-4 animate-spin" />
            {{ isLoading ? "Guardando..." : "Registrar" }}
          </Button>
        </DialogFooter>
      </form>
    </DialogContent>
  </Dialog>
</template>

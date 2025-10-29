<script setup>
import { ref, computed, onMounted } from "vue"
import { useForm } from "vee-validate"
import { toTypedSchema } from "@vee-validate/zod"
import * as z from "zod"
import { Button } from "@/shared/components/ui/button"
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/shared/components/ui/select"
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

const isDialogOpen = ref(false)
const props = defineProps({ role: { type: String, required: true } })
const emit = defineEmits(["update"])
const isLoading = ref(false)
const isClientRole = computed(() => props.role.toLowerCase() === 'cliente')

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

const formSchema = computed(() => {
  const baseSchema = {
    username: z.string().min(3, { message: "Debe tener al menos 3 caracteres." }),
    firstName: z.string().min(2, { message: "El nombre es demasiado corto." }),
    email: z.string().email({ message: "El formato del correo no es válido." }),
    password: z.string().min(8, { message: "Debe tener al menos 8 caracteres." }),
    phoneNumber: z.string().regex(/^\d{10}$/, { message: "Debe ser un número de 10 dígitos." }),
  };

  if (isClientRole.value) {
    baseSchema.clientType = z.string({ message: "Debe seleccionar un tipo." })
  } else {
    baseSchema.clientType = z.string().optional().nullable()
  }

  return toTypedSchema(z.object(baseSchema))
})

const { handleSubmit, defineField, errors, resetForm } = useForm({
  validationSchema: formSchema.value,
  initialValues: {
    clientType: isClientRole.value ? undefined : 'NOT_APPLICABLE',
    username: "",
    firstName: "",
    email: "",
    password: "",
    phoneNumber: ""
  }
})

const [clientType, clientTypeAttrs] = defineField("clientType")
const [username, usernameAttrs] = defineField("username")
const [firstName, firstNameAttrs] = defineField("firstName")
const [email, emailAttrs] = defineField("email")
const [password, passwordAttrs] = defineField("password")
const [phoneNumber, phoneNumberAttrs] = defineField("phoneNumber")

const onSubmit = handleSubmit(async (values) => {
  isLoading.value = true
  let role = 'CUSTOMER'

  switch (props.role.toLowerCase()) {
    case "vendedor":
      role = 'SELLER'
      break
    case "cliente":
      role = 'CUSTOMER'
      break
    case "compras":
      role = 'STAFF'
      break
  }

  try {
    const userData = {
      username: values.username,
      name: values.firstName,
      email: values.email,
      password: values.password,
      phone_number: "+52" + values.phoneNumber,
      role: role,
      status: 'ACTIVE'
    }

    if (isClientRole.value) {
      userData.type = values.clientType
    }

    console.log(userData);


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

    isDialogOpen.value = false
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
  <Dialog v-model:open="isDialogOpen">
    <DialogTrigger as-child>
      <Button class="bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90 shadow-md">
        <Plus class="size-4 mr-1" />
        Nuevo
      </Button>
    </DialogTrigger>

    <DialogContent class="sm:max-w-[480px] rounded-2xl shadow-xl border border-border/40 backdrop-blur-md">
      <DialogHeader class="text-center flex">
        <div class="flex mb-2 gap-4 items-center">
          <div
            class="p-3 rounded-xl bg-gradient-to-r from-[#4ed636]/10 to-[#09cb6d]/10 group-hover:from-[#4ed636]/20 group-hover:to-[#09cb6d]/20 transition-all duration-300">
            <component :is="roleIcon" class="size-10 text-green-500" />
          </div>
          <div>
            <h1 class="text-2xl font-semibold">
              Registrar {{ props.role }}
            </h1>
            <span class="text-muted-foreground text-xs">
              Completa la información del {{ props.role.toLowerCase() }}.
            </span>
          </div>
        </div>
      </DialogHeader>

      <form @submit.prevent="onSubmit" class="grid gap-4 py-4">
        <div v-if="isClientRole" class="relative">
          <User class="absolute left-3 top-2.5 text-muted-foreground size-4" />
          <Select v-model="clientType" v-bind="clientTypeAttrs">
            <SelectTrigger :class="{ 'border-red-500': errors.clientType }" class="w-full pl-9">
              <SelectValue placeholder="Selecciona un tipo de cliente" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                <SelectLabel>Tipo de cliente</SelectLabel>
                <SelectItem value="PERSON">
                  Persona
                </SelectItem>
                <SelectItem value="BUSINESS">
                  Empresa
                </SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>
          <p v-if="errors.clientType" class="text-red-500 text-xs mt-1">{{ errors.clientType }}</p>
        </div>

        <div class="relative">
          <User class="absolute left-3 top-2.5 text-muted-foreground size-4" />
          <Input id="username" v-model="username" v-bind="usernameAttrs" placeholder="Nombre de usuario" class="pl-9"
            autocomplete="off" />
          <p v-if="errors.username" class="text-red-500 text-xs mt-1">{{ errors.username }}</p>
        </div>

        <div class="relative">
          <IdCard class="absolute left-3 top-2.5 text-muted-foreground size-4" />
          <Input id="first-name" v-model="firstName" v-bind="firstNameAttrs" placeholder="Nombre completo" class="pl-9"
            autocomplete="off" />
          <p v-if="errors.firstName" class="text-red-500 text-xs mt-1">{{ errors.firstName }}</p>
        </div>

        <div class="relative">
          <Mail class="absolute left-3 top-2.5 text-muted-foreground size-4" />
          <Input id="email" type="email" v-model="email" v-bind="emailAttrs" placeholder="Correo electrónico"
            class="pl-9" autocomplete="off" />
          <p v-if="errors.email" class="text-red-500 text-xs mt-1">{{ errors.email }}</p>
        </div>

        <div class="relative">
          <Lock class="absolute left-3 top-2.5 text-muted-foreground size-4" />
          <Input id="password" type="password" v-model="password" v-bind="passwordAttrs" placeholder="Contraseña"
            class="pl-9" autocomplete="off" />
          <p v-if="errors.password" class="text-red-500 text-xs mt-1">{{ errors.password }}</p>
        </div>

        <div class="relative">
          <Phone class="absolute left-3 top-2.5 text-muted-foreground size-4" />
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
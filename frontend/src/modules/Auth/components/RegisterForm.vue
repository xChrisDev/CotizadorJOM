<script setup>
import { ref } from 'vue'
import { useForm } from 'vee-validate'
import { toTypedSchema } from '@vee-validate/zod'
import * as z from 'zod'
import { Button } from '@/shared/components/ui/button'
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/shared/components/ui/card'
import { Input } from '@/shared/components/ui/input'
import { Label } from '@/shared/components/ui/label'
import { CircleCheckBig, Eye, EyeClosed, LoaderCircle } from 'lucide-vue-next'
import { useToast } from 'vue-toastification'
import { registerUser } from '../services/authService.js'
const toast = useToast()
const showPassword = ref(false)
const isLoading = ref(false)

const formSchema = toTypedSchema(
  z.object({
  username: z.string()
    .min(1, { message: "El nombre de usuario es obligatorio." })
    .min(3, { message: "Debe tener al menos 3 caracteres." }),

  firstName: z.string()
    .min(1, { message: "El nombre es obligatorio." })
    .min(2, { message: "El nombre es demasiado corto." }),

  lastName: z.string()
    .min(1, { message: "Los apellidos son obligatorios." })
    .min(2, { message: "El apellido es demasiado corto." }),

  email: z.string()
    .min(1, { message: "El correo es obligatorio." })
    .email({ message: "El formato del correo no es válido." }),

  password: z.string()
    .min(1, { message: "La contraseña es obligatoria." })
    .min(8, { message: "La contraseña debe tener al menos 8 caracteres." }),

  phoneNumber: z.string()
    .min(1, { message: "El número telefónico es obligatorio." })
    .regex(/^\d{10}$/, { message: "Debe ser un número de 10 dígitos." }),
})
)

const { handleSubmit, defineField, errors, resetForm } = useForm({
  validationSchema: formSchema,
})

const [username, usernameAttrs] = defineField('username')
const [firstName, firstNameAttrs] = defineField('firstName')
const [lastName, lastNameAttrs] = defineField('lastName')
const [email, emailAttrs] = defineField('email')
const [password, passwordAttrs] = defineField('password')
const [phoneNumber, phoneNumberAttrs] = defineField('phoneNumber')

const onSubmit = handleSubmit(async (values) => {
  isLoading.value = true
  const userData = {
    username: values.username,
    password: values.password,
    first_name: values.firstName,
    last_name: values.lastName,
    email: values.email,
    phone_number: "+52" + values.phoneNumber,
    client_type: "A"
  }

  const response = await registerUser(userData)

  if (!response.success) {
    for (let field in response.errors) {
      response.errors[field].forEach(msg => {
        toast.error(`${msg}`, { position: "top-center" })
      })
    }
    isLoading.value = false
    return
  }

  try {
    toast.success("Nuestro equipo validará tu solicitud pronto.", {
      position: "top-center",
      icon: CircleCheckBig,
    })
    resetForm()
  } catch (error) {
    toast.error("Hubo un problema al enviar la solicitud.")
  } finally {
    isLoading.value = false
  }
})


</script>
<template>
  <Card class="w-full max-w-sm">
    <CardHeader>
      <CardTitle class="text-2xl">
        Solicitar registro
      </CardTitle>
      <CardDescription>
        Ingresa tus datos para registrarte. Tu solicitud será revisada.
      </CardDescription>
    </CardHeader>
    <form @submit.prevent="onSubmit">
      <CardContent class="grid gap-4">
        <div class="grid gap-2">
          <Label for="username">Nombre de usuario</Label>
          <Input autocomplete="off" id="username" placeholder="Ej. JoseMar99" v-model="username"
            v-bind="usernameAttrs" />
          <p v-if="errors.username" class="text-red-500 text-xs mt-1">{{ errors.username }}</p>
        </div>

        <div class="grid gap-2">
          <Label for="first-name">Nombre(s)</Label>
          <Input autocomplete="off" id="first-name" placeholder="Ej. José Martin" v-model="firstName"
            v-bind="firstNameAttrs" />
          <p v-if="errors.firstName" class="text-red-500 text-xs mt-1">{{ errors.firstName }}</p>
        </div>

        <div class="grid gap-2">
          <Label for="last-name">Apellido(s)</Label>
          <Input autocomplete="off" id="last-name" placeholder="Ej. Mendez Sosa" v-model="lastName"
            v-bind="lastNameAttrs" />
          <p v-if="errors.lastName" class="text-red-500 text-xs mt-1">{{ errors.lastName }}</p>
        </div>

        <div class="grid gap-2">
          <Label for="email">Correo Electrónico</Label>
          <Input autocomplete="off" id="email" type="email" placeholder="Ej. tudirección@correo.com" v-model="email"
            v-bind="emailAttrs" />
          <p v-if="errors.email" class="text-red-500 text-xs mt-1">{{ errors.email }}</p>
        </div>

        <div class="grid gap-2">
          <Label for="password">Contraseña</Label>
          <div class="relative w-full max-w-sm items-center">
            <Input autocomplete="off" id="password" v-model="password" v-bind="passwordAttrs"
              :type="showPassword ? 'text' : 'password'" />
            <span class="absolute end-0 inset-y-0 flex items-center justify-center p-0.5">
              <div class="cursor-pointer rounded-md p-1 hover:bg-gray-50/10" @click="showPassword = !showPassword">
                <Eye class="size-6 text-muted-foreground" v-if="!showPassword" />
                <EyeClosed class="size-6 text-muted-foreground" v-if="showPassword" />
              </div>
            </span>
          </div>
          <p v-if="errors.password" class="text-red-500 text-xs mt-1">{{ errors.password }}</p>
        </div>

        <div class="grid gap-2">
          <Label for="phone-number">Teléfono</Label>
          <Input autocomplete="off" id="phone-number" type="text" placeholder="4931234567" v-model="phoneNumber"
            v-bind="phoneNumberAttrs" />
          <p v-if="errors.phoneNumber" class="text-red-500 text-xs mt-1">{{ errors.phoneNumber }}</p>
        </div>
      </CardContent>
      <CardFooter>
        <div class="flex flex-col w-full">
          <Button :disabled="isLoading" type="submit"
            class="mt-6 w-full bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90">
            <LoaderCircle v-if="isLoading" class="mr-2 h-4 w-4 animate-spin" />
            {{ isLoading ? 'Enviando...' : 'Solicitar registro' }}
          </Button>
          <div class="mt-4 text-center text-sm">
            ¿Ya tienes una cuenta?,
            <RouterLink to="/ingresar" class="font-medium hover:underline underline-offset-2 text-green-500">
              Inicia Sesión
            </RouterLink>
          </div>
        </div>
      </CardFooter>
    </form>
  </Card>
</template>
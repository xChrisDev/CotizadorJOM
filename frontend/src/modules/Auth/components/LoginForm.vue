<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useForm } from 'vee-validate'
import { toTypedSchema } from '@vee-validate/zod'
import * as z from 'zod'
import { Button } from '@/shared/components/ui/button'
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/shared/components/ui/card'
import { Input } from '@/shared/components/ui/input'
import { Label } from '@/shared/components/ui/label'
import { CircleCheckBig, Eye, EyeClosed, LoaderCircle } from 'lucide-vue-next'
import { useToast } from 'vue-toastification'
import { loginUser } from '../services/authService.js'
import { useAuthStore } from '@/shared/stores/auth.js'
import { useUserStore } from "@/shared/stores/user.js";

const router = useRouter()
const toast = useToast()
const authStore = useAuthStore();
const userStore = useUserStore();
const showPassword = ref(false)
const isLoading = ref(false)

const formSchema = toTypedSchema(
  z.object({
    username: z.string().min(1, 'El nombre de usuario es requerido'),
    password: z.string().min(1, 'La contraseña es requerida'),
  })
)

const { handleSubmit, defineField, errors, resetForm } = useForm({
  validationSchema: formSchema,
})

const [username, usernameAttrs] = defineField('username')
const [password, passwordAttrs] = defineField('password')

const onSubmit = handleSubmit(async (values) => {
  isLoading.value = true;
  const response = await loginUser(values);

  if (!response.success) {
    for (let field in response.errors) {
      const msg = response.errors[field];
      toast.error(msg, { position: "top-center" });
    }
    isLoading.value = false;
    return;
  }

  try {
    toast.success(`Bienvenido ${response.data.user.username}`, {
      position: "top-center",
      icon: CircleCheckBig,
    });
    resetForm();
    authStore.login(response.data.token, response.data.user.rol);
    // userStore.fetchUser();

    switch (response.data.user.rol) {
      case "ADMIN":
        router.push("/admin");
        break;
      case "SELLER":
        router.push("/vendedor");
        break;
      case "SHOPPER":
        router.push("/compras");
        break;
      default:
        router.push("/buscar");
        break;
    }
  } catch (error) {
    toast.error("Hubo un problema al procesar la solicitud.", { position: "top-center" });
  } finally {
    isLoading.value = false;
  }
});

</script>

<template>
  <Card class="w-full max-w-sm">
    <CardHeader>
      <CardTitle class="text-2xl">
        Iniciar Sesión
      </CardTitle>
      <CardDescription>
        Ingresa tu nombre de usuario y contraseña para acceder.
      </CardDescription>
    </CardHeader>
    <form @submit="onSubmit">
      <CardContent class="grid gap-4">
        <div class="grid gap-2">
          <Label for="username">Nombre de usuario</Label>
          <Input id="username" type="text" placeholder="Ej. JoseMar99" autocomplete="off" v-model="username"
            v-bind="usernameAttrs" />
          <p v-if="errors.username" class="text-red-500 text-xs mt-1">{{ errors.username }}</p>
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
      </CardContent>
      <CardFooter>
        <div class="flex flex-col w-full">
          <Button :disabled="isLoading" type="submit"
            class="mt-6 w-full bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90">
            <LoaderCircle v-if="isLoading" class="mr-2 h-4 w-4 animate-spin" />
            {{ isLoading ? 'Ingresando...' : 'Ingresar' }}
          </Button>
          <div class="mt-4 text-center text-sm">
            ¿No tienes una cuenta?,
            <RouterLink to="/registrarse" class="font-medium hover:underline underline-offset-2 text-green-500">
              Regístrate
            </RouterLink>
          </div>
        </div>
      </CardFooter>
    </form>
  </Card>
</template>
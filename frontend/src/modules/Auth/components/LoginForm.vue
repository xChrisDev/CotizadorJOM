<script setup>
import { ref } from 'vue'
import { Button } from '@/shared/components/ui/button'
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/shared/components/ui/card'
import { Input } from '@/shared/components/ui/input'
import { Label } from '@/shared/components/ui/label'

const email = ref('')
const password = ref('')

function handleSubmit() {

}
</script>

<template>
  <Card class="w-full max-w-sm">
    <CardHeader>
      <CardTitle class="text-2xl">
        Iniciar Sesión
      </CardTitle>
      <CardDescription>
        Ingresa tu correo electrónico y contraseña para acceder a tu cuenta.
      </CardDescription>
    </CardHeader>
    <form @submit.prevent="handleSubmit">
      <CardContent class="grid gap-4">
        <div class="grid gap-2">
          <Label for="email">Correo Electrónico</Label>
          <Input id="email" type="email" placeholder="tu@correo.com" required v-model="email" />
        </div>
        <div class="grid gap-2">
          <div class="flex items-center">
            <Label for="password">Contraseña</Label>
          </div>
          <Input id="password" type="password" required v-model="password" />
        </div>
      </CardContent>
      <CardFooter>
        <div class="flex flex-col w-full">
          <Button class="mt-6 w-full bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90">
            Ingresar
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
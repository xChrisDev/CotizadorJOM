<script setup>
import { ref } from 'vue'
import { Button } from '@/shared/components/ui/button'
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/shared/components/ui/card'
import { Input } from '@/shared/components/ui/input'
import { Label } from '@/shared/components/ui/label'

const fullName = ref('')
const email = ref('')
const password = ref('')
const phoneNumber = ref('')

function handleSubmit() {

}
</script>

<template>
  <Card class="w-full max-w-sm">
    <CardHeader>
      <CardTitle class="text-2xl">
        Solicitar registro
      </CardTitle>
      <CardDescription>
        Ingresa tus datos para registrarte.
      </CardDescription>
    </CardHeader>
    <form @submit.prevent="handleSubmit">
      <CardContent class="grid gap-4">
        <div class="grid gap-2">
          <Label for="full-name">Nombre Completo</Label>
          <Input id="full-name" placeholder="Ej. José Mendez" required v-model="fullName" />
        </div>
        <div class="grid gap-2">
          <Label for="email">Correo Electrónico</Label>
          <Input id="email" type="email" placeholder="tudirección@correo.com" required v-model="email" />
        </div>
        <div class="grid gap-2">
          <Label for="password">Contraseña</Label>
          <Input id="password" type="password" required v-model="password" />
        </div>
        <div class="grid gap-2">
          <Label for="phone-number">Teléfono</Label>
          <Input id="phone-number" type="tel" required v-model="phoneNumber" />
          <!-- Checar si es necesario usar la regex en este campo:  pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"  -->
        </div>
      </CardContent>
      <CardFooter>
        <div class="flex flex-col w-full">
          <Button class="mt-6 w-full bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90">
            Solicitar registro
          </Button>
          <div class="text-white mt-4 text-center text-sm">
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
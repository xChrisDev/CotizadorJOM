<script setup>
import { useRouter } from 'vue-router'
import { Button } from '@/shared/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/shared/components/ui/card'
import { AlertTriangle } from 'lucide-vue-next'

const router = useRouter()

const redirectToLogin = () => {
  router.push('/ingresar')
}
</script>

<template>
  <div
    class="relative flex items-center justify-center min-h-screen p-4 bg-[url(@/shared/assets/hero-image.jpg)] bg-cover bg-center">
    <div class="absolute inset-0 bg-black/80"></div>

    <div class="relative w-full max-w-md">
      <Card>
        <CardHeader class="text-center">
          <div class="flex justify-center mb-4">
            <AlertTriangle class="w-12 h-12 text-destructive sm:w-16 sm:h-16" />
          </div>
          <CardTitle class="text-xl font-bold sm:text-2xl">
            Acceso Denegado
          </CardTitle>
        </CardHeader>
        <CardContent class="flex flex-col items-center space-y-4">
          <p class="text-center text-muted-foreground">
            Por favor, inicia sesión con una cuenta autorizada para continuar.
          </p>
          <Button @click="redirectToLogin" class="w-full">
            Volver al inicio
          </Button>
        </CardContent>
      </Card>
    </div>
  </div>
</template>

<style scoped>
/* Estilos adicionales si son necesarios */
</style>
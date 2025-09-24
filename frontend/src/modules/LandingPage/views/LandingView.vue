<script setup>
import Hero from '../components/Hero.vue';
import Navbar from '../components/Navbar.vue';
import { Card, CardHeader, CardContent } from "@/shared/components/ui/card"
</script>

<template>
    <Navbar />
    <Hero />

    <!-- Footer -->
    <footer class="border-t py-6 text-center text-sm text-muted-foreground">
        © 2025 JOM Cotizador. Todos los derechos reservados.
    </footer>
</template>

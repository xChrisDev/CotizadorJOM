<script setup>
import { RouterLink } from 'vue-router';
import RegisterForm from '../components/RegisterForm.vue'
import Navbar from '@/shared/components/Navbar.vue';
</script>

<template>
    <div
        class="relative min-h-screen w-full bg-cover bg-center bg-[url(@/shared/assets/hero-image.jpg)] flex items-center justify-center p-4">
        <Navbar variant="auth"/>

        <div class="absolute inset-0 bg-gray-600 opacity-60 dark:bg-black dark:opacity-80"></div>

        <div class="relative z-10 flex flex-col items-center justify-center w-full pt-20">
            <RegisterForm />
        </div>
    </div>
</template>
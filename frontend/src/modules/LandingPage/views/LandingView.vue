<script setup>
import Hero from '../components/Hero.vue';
import Navbar from '@/shared/components/Navbar.vue';
import Services from '../components/Services.vue';
import About from '../components/About.vue';
import Testimonials from '../components/Testimonials.vue';
import Contact from '../components/Contact.vue';
import Footer from '../components/Footer.vue';
</script>

<template>
  <div class="min-h-screen">
    <Navbar variant="landing" />
    <Hero />
    <Services />
    <About />
    <Testimonials />
    <Contact />
    <Footer />
  </div>
</template>

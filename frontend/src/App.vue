<script setup>
import { Transition } from "vue";
import { RouterView } from "vue-router";
</script>

<template>
    <router-view v-slot="{ Component, route }">
      <Transition name="fade-zoom" mode="out-in">
        <component :is="Component" :key="route.path" />
      </Transition>
    </router-view>
</template>

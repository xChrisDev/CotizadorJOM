<script setup lang="ts">
import { useColorMode } from "@vueuse/core";
const mode = useColorMode();
import { Button } from "@/shared/components/ui/button";
import { Moon, Sun } from "lucide-vue-next";
</script>

<template>
  <Button
    @click="mode = mode === 'dark' ? 'light' : 'dark'"
    size="lg"
    variant="outline"
    class="h-14 lg:w-14 w-24 lg:justify-center"
  >
    <div
      v-if="mode == 'light'"
      class="flex gap-2"
    >
      <Moon class="size-5" />
      <span class="block lg:hidden"> Dark </span>
    </div>

    <div
      v-else="mode == 'dark'"
      class="flex gap-2"
    >
      <Sun class="size-5" />
      <span class="block lg:hidden">Light</span>
    </div>

    <span class="sr-only">Toggle theme</span>
  </Button>
</template>
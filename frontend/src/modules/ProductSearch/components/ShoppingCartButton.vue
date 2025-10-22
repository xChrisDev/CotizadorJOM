<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { Button } from '@/shared/components/ui/button';
import { Sheet, SheetContent, SheetFooter, SheetHeader, SheetTitle, SheetTrigger } from '@/shared/components/ui/sheet';
import { Separator } from '@/shared/components/ui/separator';
import { ShoppingCart, PackageX, FileInput } from 'lucide-vue-next';
import CartItem from './CartItem.vue';
import { useCartStore } from '../stores/cart.js';

const cartStore = useCartStore();
const router = useRouter();
const isOpenCart = ref(false);

function handleCheckout() {
  isOpenCart.value = false;
  router.push('/cotizacion');
}
</script>

<template>
  <Sheet v-model:open="isOpenCart">
    <SheetTrigger as-child>
      <Button size="lg" variant="outline" class="h-14 lg:w-14 lg:justify-center justify-start relative">
        <ShoppingCart class="size-6" />
        <span v-if="cartStore.cartCount > 0"
          class="absolute -top-1 -right-2 flex h-6 w-6 items-center justify-center rounded-full bg-red-500 text-xs font-bold text-white">
          {{ cartStore.cartCount }}
        </span>
      </Button>
    </SheetTrigger>

    <SheetContent side="right" class="z-[9999] flex flex-col bg-card/90 backdrop-blur-lg border-r w-full sm:max-w-md">
      <SheetHeader class="mx-2">
        <SheetTitle class="flex items-center gap-2">
          <ShoppingCart class="size-7" />
          <span class="text-lg">Mi cotización</span>
        </SheetTitle>
        <Separator class="opacity-30 bg-primary" />
      </SheetHeader>

      <div class="flex-grow overflow-y-auto px-3">
        <div v-if="cartStore.items.length > 0" class="flex flex-col gap-3">
          <CartItem v-for="item in cartStore.items" :key="item.id" :item="item" />
        </div>

        <div v-else class="flex flex-col items-center justify-center h-full text-center text-muted-foreground">
          <PackageX class="size-16 mb-4" />
          <h3 class="text-lg font-semibold">Tu carrito está vacío</h3>
          <p class="text-sm">¡Agrega articulos para verlos aquí!</p>
        </div>
      </div>

      <SheetFooter v-if="cartStore.items.length > 0" class="flex-col sm:flex-col justify-start items-start p-4">
        <Separator class="mb-4 opacity-30 bg-primary" />
        <Button size="lg" class="w-full text-base bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90"
          @click="handleCheckout">
          <FileInput class="size-6 mr-2" />
          Completar Cotización
        </Button>
      </SheetFooter>
    </SheetContent>
  </Sheet>
</template>
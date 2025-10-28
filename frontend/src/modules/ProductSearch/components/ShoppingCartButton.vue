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
            <Button size="lg" variant="outline" class="fixed bottom-8 right-8 z-50 h-16 w-16 rounded-full
         border-2 border-transparent
         bg-gradient-to-tr from-gray-900 to-gray-800
         text-white dark:from-green-500 dark:to-green-400
         shadow-[0_4px_14px_rgba(0,0,0,0.25)]
         hover:scale-110 hover:shadow-[0_6px_20px_rgba(0,0,0,0.35)]
         transition-all duration-300 ease-out
         flex items-center justify-center">
                <ShoppingCart class="size-6 text-white dark:text-gray-900" />
                <span v-if="cartStore.cartCount > 0" class="absolute -top-1.5 -right-1.5 flex h-6 w-6 items-center justify-center
           rounded-full bg-red-600 text-xs font-bold text-white
           border-2 border-white dark:border-gray-900 shadow-md">
                    {{ cartStore.cartCount }}
                </span>
            </Button>


        </SheetTrigger>
        <SheetContent side="right" class=" flex flex-col bg-card border-r w-full sm:max-w-md">
            <SheetHeader class="mx-2">
                <SheetTitle class="flex items-center gap-2">
                    <ShoppingCart class="size-7" />
                    <span class="text-lg">Cotización</span>        
                </SheetTitle>
                <Separator class="opacity-30 bg-primary" />
            </SheetHeader>

            <div class="px-3 flex flex-col max-h-[70vh]">
  <div v-if="cartStore.items.length > 0" class="overflow-y-auto pr-2 space-y-3">
    <CartItem
      v-for="item in cartStore.items"
      :key="item.id"
      :item="item"
    />
  </div>

  <div
    v-else
    class="flex flex-col items-center justify-center py-10 text-center text-muted-foreground"
  >
    <PackageX class="size-16 mb-2" />
    <h3 class="text-lg font-semibold">Tu carrito está vacío</h3>
    <p class="text-sm">¡Agrega artículos para verlos aquí!</p>
  </div>
</div>


            <SheetFooter v-if="cartStore.items.length > 0" class="flex flex-col px-4"> 
                <Separator class="mb-2 opacity-30 bg-primary" />
                <Button size="lg" class="w-full text-base bg-gradient-to-r from-[#4ed636] to-[#09cb6d] hover:opacity-90"
                    @click="handleCheckout">
                    <FileInput class="size-6 mr-2" />Completar Cotización
                </Button>
            </SheetFooter> 
        </SheetContent>

    </Sheet>
</template>
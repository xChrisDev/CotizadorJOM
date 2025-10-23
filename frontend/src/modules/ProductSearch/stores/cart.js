import { ref, computed, watch } from "vue";
import { defineStore } from "pinia";
import { useToast } from "vue-toastification";

export const useCartStore = defineStore("cart", () => {
  const STORAGE_KEY = "quote_cart";
  const toast = useToast();
  const items = ref(JSON.parse(localStorage.getItem(STORAGE_KEY)) || []);

  const cartCount = computed(() =>
    items.value.reduce((total, item) => total + item.quantity, 0)
  );

  const cartTotal = computed(() =>
    items.value
      .reduce((total, item) => total + item.price * item.quantity, 0)
      .toFixed(2)
  );

  function addToCart(product, amount = 1) {
    const existingItem = items.value.find((item) => item.id === product.id);
    if (existingItem) {
      existingItem.quantity += amount;
    } else {
      items.value.push({ ...product, quantity: amount });
      toast.info(`${product.article_name} ha sido agregado`)
    }
  }

  function removeFromCart(productId) {
    items.value = items.value.filter((item) => item.id !== productId);
  }

  function updateQuantity(productId, newQuantity) {
    const item = items.value.find((item) => item.id === productId);
    if (item) {
      if (newQuantity > 0) {
        item.quantity = newQuantity;
      } else {
        removeFromCart(productId);
      }
    }
  }

  function clearCart() {
    items.value = [];
  }

  watch(
    items,
    (newItems) => {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(newItems));
    },
    { deep: true }
  );

  return {
    items,
    cartCount,
    cartTotal,
    addToCart,
    removeFromCart,
    updateQuantity,
    clearCart,
  };
});

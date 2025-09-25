import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const useCartStore = defineStore("cart", () => {
  const items = ref([]);

  const cartCount = computed(() => {
    return items.value.reduce((total, item) => total + item.quantity, 0);
  });

  const cartTotal = computed(() => {
    return items.value
      .reduce((total, item) => total + item.price * item.quantity, 0)
      .toFixed(2);
  });

  function addToCart(product, amount = 1) {
    const existingItem = items.value.find((item) => item.id === product.id);
    if (existingItem) {
      existingItem.quantity += amount;
    } else {
      items.value.push({ ...product, quantity: amount });
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

<script setup>
import { ref, watch, onMounted, onBeforeUnmount } from 'vue';
import { Input } from '@/shared/components/ui/input';
import { Search } from 'lucide-vue-next';
import { fetchArticles } from '@/shared/services/productService.js';
import placeholderImage from '@/shared/assets/default-image.jpg';
const props = defineProps({ value: String });
const emit = defineEmits(['update:value']);

const searchQuery = ref(props.value ?? '');
const results = ref([]);
const showDropdown = ref(false);
let debounceTimeout = null;
const totalItems = ref(0);
const dropdownRef = ref(null);

const fetchResults = async (query) => {
    try {
        const data = await fetchArticles({
            search: query,
            ordering: 'article_name',
            page: 1,
            page_size: 20,
        });
        results.value = data.results ?? [];
        showDropdown.value = results.value.length > 0;
        totalItems.value = data.count ?? 0;
    } catch (err) {
        console.error(err);
        results.value = [];
        showDropdown.value = false;
    }
};

watch(searchQuery, (val) => {
    clearTimeout(debounceTimeout);
    if (val.length > 0) {
        debounceTimeout = setTimeout(() => fetchResults(val), 300);
    } else {
        results.value = [];
        showDropdown.value = false;
    }
});

const selectItem = (item) => {
    searchQuery.value = item.article_name;
    showDropdown.value = false;
    emit('update:value', item.article_name);
};

const handleClickOutside = (event) => {
    if (dropdownRef.value && !dropdownRef.value.contains(event.target)) {
        showDropdown.value = false;
    }
};

onMounted(() => {
    document.addEventListener('mousedown', handleClickOutside);
});
onBeforeUnmount(() => {
    document.removeEventListener('mousedown', handleClickOutside);
});
</script>

<template>
    <div ref="dropdownRef" class="relative w-full max-w-xl">
        <input v-model="searchQuery" placeholder="Buscar..." class="pl-12 w-full py-2 pr-4 border-2 border-[#4ed636] rounded-lg" />
        <span
            class="absolute start-0 inset-y-0 flex items-center justify-center px-3 bg-gradient-to-r from-[#4ed636] to-[#09cb6d] rounded-s-lg">
            <Search class="size-5 dark:text-black text-white" />
        </span>

        <ul v-if="showDropdown"
            class="absolute z-10 w-full mt-2 bg-white dark:bg-[#27272a] border-2 border-[#4ed636] rounded-lg shadow-lg max-h-60 overflow-y-auto scrollbar-transparent p-2">
            <li class="font-bold flex justify-center py-2">Se encontraron {{ totalItems }} coincidencias</li>
            <li v-for="(item, index) in results" :key="index" @click="selectItem(item)"
                class="flex items-center gap-3 p-2 rounded-md cursor-pointer hover:bg-gray-200 dark:hover:bg-[#37373b] transition-all duration-150">
                <img :src="item.image_url || placeholderImage" :alt="item.article_name"
                    class="w-10 h-10 object-cover rounded-md flex-shrink-0" />

                <div class="flex flex-col overflow-hidden">
                    <span class="font-medium text-sm line-clamp-1">{{ item.article_name }}</span>
                    <span class="text-xs text-gray-500 truncate">{{ item.category.name }} | {{ item.family.name
                    }}</span>
                </div>
            </li>

        </ul>
    </div>
</template>

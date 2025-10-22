<script setup>
import { ref, watch, onMounted, onBeforeUnmount, nextTick } from 'vue'
import { Search } from 'lucide-vue-next'
import { fetchUsers } from '@/modules/Admin/services/userService.js'
import { useDebounce } from '@/shared/utils/useDebounce.js'

const props = defineProps({
    modelValue: {
        type: String,
        default: ''
    }
})
const emit = defineEmits(['update:modelValue','select:client'])

const searchQuery = ref(props.modelValue)
watch(() => props.modelValue, (val) => (searchQuery.value = val))
watch(searchQuery, (val) => emit('update:modelValue', val))

const results = ref([])
const showDropdown = ref(false)
const totalItems = ref(0)
const inputRef = ref(null)
const dropdownPosition = ref({ top: 0, left: 0, width: 0 })
const isLoading = ref(false)
const justSelected = ref(false)

// Debounced search
const debouncedSearch = useDebounce(searchQuery, 500)

watch(debouncedSearch, async (val) => {
    if (justSelected.value) return
    if (val.length === 0) {
        results.value = []
        totalItems.value = 0
        showDropdown.value = false
        isLoading.value = false
        return
    }
    isLoading.value = true
    try {
        const data = await fetchUsers('CUSTOMER', {
            search: val,
            ordering: 'first_name',
            page: 1,
            page_size: 10
        })
        results.value = data.results ?? []
        totalItems.value = data.count ?? 0
        showDropdown.value = results.value.length > 0
    } catch (err) {
        console.error(err)
        results.value = []
        totalItems.value = 0
        showDropdown.value = false
    } finally {
        isLoading.value = false
    }
})

const selectItem = (item) => {
    emit('select:client', item)
    searchQuery.value = item.first_name + ' ' + item.last_name
    showDropdown.value = false
    justSelected.value = true
    nextTick(() => {
        justSelected.value = false
    })
}

const updateDropdownPosition = () => {
    if (!inputRef.value) return
    const rect = inputRef.value.getBoundingClientRect()
    dropdownPosition.value = {
        top: rect.bottom + window.scrollY,
        left: rect.left + window.scrollX,
        width: rect.width
    }
}

const handleClickOutside = (event) => {
    if (
        inputRef.value &&
        !inputRef.value.contains(event.target) &&
        !event.target.closest('.search-dropdown')
    ) {
        showDropdown.value = false
    }
}

onMounted(() => {
    document.addEventListener('mousedown', handleClickOutside)
    window.addEventListener('resize', updateDropdownPosition)
    window.addEventListener('scroll', updateDropdownPosition, true)
})
onBeforeUnmount(() => {
    document.removeEventListener('mousedown', handleClickOutside)
    window.removeEventListener('resize', updateDropdownPosition)
    window.removeEventListener('scroll', updateDropdownPosition, true)
})
</script>

<template>
<div class="relative w-full max-w-xl" ref="inputRef">
    <input
        v-model="searchQuery"
        placeholder="Buscar..."
        class="pl-12 pr-10 w-full py-1 border-2 border-[#4ed636] rounded-lg focus:outline-none"
        @focus="updateDropdownPosition(); if (results.length) showDropdown = true"
    />
    <span
        class="absolute start-0 inset-y-0 flex items-center justify-center px-3 bg-gradient-to-r from-[#4ed636] to-[#09cb6d] rounded-s-lg"
    >
        <Search class="size-5 dark:text-black text-white" />
    </span>

    <teleport to="body">
        <ul
            v-if="showDropdown"
            class="search-dropdown absolute mt-2 z-[99999] bg-white dark:bg-[#27272a] border-2 border-[#4ed636] rounded-md shadow-xl overflow-y-auto scrollbar-transparent p-2"
            :style="{
                top: dropdownPosition.top + 'px',
                left: dropdownPosition.left + 'px',
                width: dropdownPosition.width + 'px'
            }"
        >
            <li v-if="isLoading" class="flex justify-center items-center py-4">
                <div class="w-6 h-6 border-4 border-gray-300 border-t-green-500 rounded-full animate-spin"></div>
                <span class="ml-2 text-gray-600 dark:text-gray-300">Buscando...</span>
            </li>

            <template v-else>
                <li class="font-bold flex justify-center py-2">
                    Se encontraron {{ totalItems }} coincidencias
                </li>
                <li
                    v-for="(user, index) in results"
                    :key="index"
                    @click="selectItem(user)"
                    class="flex items-center gap-3 p-2 rounded-md cursor-pointer hover:bg-gray-200 dark:hover:bg-[#37373b] transition-all duration-150"
                >
                    <div class="flex flex-col overflow-hidden">
                        <span class="font-medium text-sm line-clamp-1">
                            {{ user.first_name }} {{ user.last_name }}
                        </span>
                        <span class="text-xs text-gray-500 truncate">
                            {{ user.email }} | {{ user.phone_number }}
                        </span>
                    </div>
                </li>
                <li v-if="!results.length" class="text-center text-sm text-gray-500 py-2">
                    No se encontraron resultados
                </li>
            </template>
        </ul>
    </teleport>
</div>
</template>

<script setup lang="ts">
import { Button } from "@/shared/components/ui/button"
import {
    Dialog,
    DialogClose,
    DialogContent,
    DialogDescription,
    DialogFooter,
    DialogHeader,
    DialogTitle,
    DialogTrigger,
} from "@/shared/components/ui/dialog"
import { Ban } from "lucide-vue-next"
</script>

<template>
    <Dialog>
        <DialogTrigger as-child>
            <Button class="bg-gradient-to-r from-[#EF4444] to-[#DC2626]" size="icon">
                <Ban class="size-5" />
            </Button>
        </DialogTrigger>
        <DialogContent class="sm:max-w-[425px]">
            <DialogHeader>
                <DialogTitle>¿Estás seguro?</DialogTitle>
                <DialogDescription>
                    Suspenderas este usuario permanentemente.
                </DialogDescription>
            </DialogHeader>
            <DialogFooter class="sm:justify-end gap-2 pt-4">
                <DialogClose as-child>
                    <Button type="button" variant="outline">
                        Cancelar
                    </Button>
                </DialogClose>
                <Button type="button" class="bg-gradient-to-r from-[#EF4444] to-[#DC2626]">
                    Confirmar
                </Button>
            </DialogFooter>
        </DialogContent>
    </Dialog>
</template>
<script setup>
import { ref } from 'vue';
import { Input } from '@/shared/components/ui/input';
import { Label } from '@/shared/components/ui/label';
import { Checkbox } from '@/shared/components/ui/checkbox';
import { RadioGroup, RadioGroupItem } from '@/shared/components/ui/radio-group';
import { Star, Filter } from 'lucide-vue-next';
import {Card, CardContent} from '@/shared/components/ui/card';

const categories = ['Frenos y suspensión', 'Motor y transmisión', 'Filtros y lubricantes', 'Sistema eléctrico', 'Carrocería', 'Neumáticos y llantas'];
const brands = ['STP', 'Value', 'FRAM', 'Roadstar','Bardahl','GROB','Mobil','Mitsubishi','UNIFIL'];
</script>

<template>
    <Card>
        <CardContent class="space-y-8">
            <h2 class="text-xl font-bold flex items-center gap-2">
                <Filter class="w-5 h-5" />
                Filtros
            </h2>

            <div>
                <h3 class="font-semibold mb-3">Categoría</h3>
                <RadioGroup default-value="frenos" class="space-y-2">
                    <div v-for="cat in categories" :key="cat" class="flex items-center">
                        <RadioGroupItem :id="cat" :value="cat.toLowerCase().replace(' ', '-')" />
                        <Label :for="cat" class="ml-2 font-normal">{{ cat }}</Label>
                    </div>
                </RadioGroup>
            </div>

            <div>
                <h3 class="font-semibold mb-3">Precio</h3>
                <div class="flex items-center gap-2">
                    <Input type="number" placeholder="Mínimo" />
                    <span>-</span>
                    <Input type="number" placeholder="Máximo" />
                </div>
            </div>

            <div>
                <h3 class="font-semibold mb-3">Disponibilidad</h3>
                <RadioGroup default-value="todos" class="space-y-2">
                    <div class="flex items-center">
                        <RadioGroupItem id="todos" value="todos" />
                        <Label for="todos" class="ml-2 font-normal">Todos los productos</Label>
                    </div>
                    <div class="flex items-center">
                        <RadioGroupItem id="disponible" value="disponible" />
                        <Label for="disponible" class="ml-2 font-normal">Disponible</Label>
                    </div>
                    <div class="flex items-center">
                        <RadioGroupItem id="agotado" value="agotado" />
                        <Label for="agotado" class="ml-2 font-normal">Agotado</Label>
                    </div>
                </RadioGroup>
            </div>

            <div>
                <h3 class="font-semibold mb-3">Marca</h3>
                <div class="space-y-2">
                    <div v-for="brand in brands" :key="brand" class="flex items-center">
                        <Checkbox :id="brand.toLowerCase()" />
                        <Label :for="brand.toLowerCase()" class="ml-2 font-normal">{{ brand }}</Label>
                    </div>
                </div>
            </div>
        </CardContent>
    </Card>
</template>
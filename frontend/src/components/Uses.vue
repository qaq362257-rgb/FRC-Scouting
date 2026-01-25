<script setup>
import { Uses } from '@/Constants';

defineProps({
    label: String
});
const uses = defineModel([]);
function toggleUse(use) {
    if (uses.value.includes(use)) {
        uses.value = uses.value.filter((t) => t !== use);
    } else {
        uses.value.push(use);
    }
}
</script>
<template>
    <div class="flex flex-col gap-1 mb-4">
        <label v-if="label" class="text-gray-700 font-bold ml-1">
            {{ label }}
        </label>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 items-stretch border-2 border-gray-300 rounded-xl overflow-hidden bg-white shadow-sm">
            <div
                @click="toggleUse(Uses.SHOOT)"
                class="h-12 grid grow items-center justify-center bg-gray-100 text-gray-600 transition text-2xl font-bold border-r border-gray-200"
                :class="{'bg-gray-300': uses.includes(Uses.SHOOT)}"
            >
                Shoot
            </div>
            <div
                @click="toggleUse(Uses.HANGING)"
                class="h-12 grid grow items-center justify-center bg-gray-100 text-gray-600 transition text-2xl font-bold border-r border-gray-200"
                :class="{'bg-gray-300': uses.includes(Uses.HANGING)}"
            >
                Hanging
            </div>
            <div
                @click="toggleUse(Uses.DEFENSE)"
                class="h-12 grid grow items-center justify-center bg-gray-100 text-gray-600 transition text-2xl font-bold border-r border-gray-200"
                :class="{'bg-gray-300': uses.includes(Uses.DEFENSE)}"
            >
                Defense
            </div>
            <div
                @click="toggleUse(Uses.SUPPORT)"
                class="h-12 grid grow items-center justify-center bg-gray-100 text-gray-600 transition text-2xl font-bold border-r border-gray-200"
                :class="{'bg-gray-300': uses.includes(Uses.SUPPORT)}"
            >
                Support
            </div>
        </div>
    </div>
</template>
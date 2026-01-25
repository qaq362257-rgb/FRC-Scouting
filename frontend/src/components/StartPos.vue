<script setup>
import { StartPos } from '@/Constants';

defineProps({
    label: String
});
const pos = defineModel(StartPos.MIDDLE);

function changePos(newPos) {
    pos.value = newPos;
}
</script>
<template>
    <div class="flex flex-col gap-1 mb-4">
        <label v-if="label" class="text-gray-700 font-bold ml-1">
            {{ label }}
        </label>
        <div class="flex flex-col sm:flex-row items-stretch border-2 border-gray-300 rounded-xl overflow-hidden bg-white shadow-sm">
            <div
                @click="changePos(StartPos.DEPOT)"
                class="h-12 flex grow items-center justify-center bg-gray-100 text-gray-600 transition text-2xl font-bold border-r border-gray-200"
                :class="{ 'bg-gray-300': pos === StartPos.DEPOT }"
            >
                Depot
            </div>
            <div
                @click="changePos(StartPos.MIDDLE)"
                class="h-12 flex grow items-center justify-center bg-gray-100 text-gray-600 transition text-2xl font-bold border-l border-gray-200"
                :class="{ 'bg-gray-300': pos === StartPos.MIDDLE }"
            >
                Middle
            </div>
            <div
                @click="changePos(StartPos.PLAYER)"
                class="h-12 flex grow items-center justify-center bg-gray-100 text-gray-600 transition text-2xl font-bold border-l border-gray-200"
                :class="{ 'bg-gray-300': pos === StartPos.PLAYER }"
            >
                Player
            </div>
        </div>
    </div>
</template>
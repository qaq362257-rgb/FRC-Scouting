<script setup>
import { TeamColor } from '@/Constants';

defineProps({
    label: String
});
const teamColor = defineModel(TeamColor.RED);

function setColor(color) {
    teamColor.value = color;
}
</script>
<template>
    <div class="flex flex-col gap-1 mb-4">
        <label v-if="label" class="text-gray-700 font-bold ml-1">
            {{ label }}
        </label>
        <div class="flex items-center border-2 border-gray-300 rounded-xl overflow-hidden bg-white shadow-sm">
            <div
                @click="setColor(TeamColor.RED)"
                class="h-12 flex grow items-center justify-center bg-red-100 text-red-600 transition text-2xl font-bold border-r border-gray-200"
                :class="{ 'bg-red-300': teamColor === TeamColor.RED }"
            >
                Red
            </div>
            <div
                @click="setColor(TeamColor.BLUE)"
                class="h-12 flex grow items-center justify-center bg-blue-100 text-blue-600 transition text-2xl font-bold border-l border-gray-200"
                :class="{ 'bg-blue-300': teamColor === TeamColor.BLUE }"
            >
                Blue
            </div>
        </div>
    </div>
</template>
<script setup>
import { HangingState } from '@/Constants';

defineProps({
    label: String
});
const state = defineModel(HangingState.NO);

function changeState(newState) {
    state.value = newState;
}
</script>
<template>
    <div class="flex flex-col gap-1 mb-4">
        <label v-if="label" class="text-gray-700 font-bold ml-1">
            {{ label }}
        </label>
        <div class="flex flex-col sm:flex-row items-stretch border-2 border-gray-300 rounded-xl overflow-hidden bg-white shadow-sm">
            <div
                @click="changeState(HangingState.NO)"
                class="h-12 flex grow items-center justify-center bg-red-100 text-red-600 transition text-2xl font-bold border-r border-gray-200"
                :class="{ 'bg-red-300': state === HangingState.NO }"
            >
                None
            </div>
            <div
                @click="changeState(HangingState.FAIL)"
                class="h-12 flex grow items-center justify-center bg-yellow-100 text-yellow-600 transition text-2xl font-bold border-l border-gray-200"
                :class="{ 'bg-yellow-300': state === HangingState.FAIL }"
            >
                Fail
            </div>
            <div
                @click="changeState(HangingState.SUCCESS)"
                class="h-12 flex grow items-center justify-center bg-green-100 text-green-600 transition text-2xl font-bold border-l border-gray-200"
                :class="{ 'bg-green-300': state === HangingState.SUCCESS }"
            >
                Success
            </div>
        </div>
    </div>
</template>
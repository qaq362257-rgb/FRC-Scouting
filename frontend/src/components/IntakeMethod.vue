<script setup>
import { IntakeMethod } from '@/Constants';

defineProps({
    label: String
});
const method = defineModel(IntakeMethod.NO);
function changeMethod(nowMethod) {
    if (nowMethod === IntakeMethod.FLOOR) {
        method.value = IntakeMethod.FLOOR;
    } else if (nowMethod === IntakeMethod.PLAYER) {
        method.value = IntakeMethod.PLAYER;
    } else if (nowMethod === IntakeMethod.BOTH) {
        method.value = IntakeMethod.BOTH;
    } else if (nowMethod === IntakeMethod.NO) {
        method.value = IntakeMethod.NO;
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
                @click="changeMethod(IntakeMethod.FLOOR)"
                class="h-12 grid grow items-center justify-center bg-blue-100 text-blue-600 transition text-2xl font-bold border-r border-gray-200"
                :class="{'bg-blue-300': method === IntakeMethod.FLOOR}"
            >
                Only Floor
            </div>
            <div
                @click="changeMethod(IntakeMethod.PLAYER)"
                class="h-12 grid grow items-center justify-center bg-orange-100 text-orange-600 transition text-2xl font-bold border-r border-gray-200"
                :class="{'bg-orange-300': method === IntakeMethod.PLAYER}"
            >
                Only Human Player
            </div>
            <div
                @click="changeMethod(IntakeMethod.BOTH)"
                class="h-12 grid grow items-center justify-center bg-green-100 text-green-600 transition text-2xl font-bold border-r border-gray-200"
                :class="{'bg-green-300': method === IntakeMethod.BOTH}"
            >
                Both
            </div>
            <div
                @click="changeMethod(IntakeMethod.NO)"
                class="h-12 grid grow items-center justify-center bg-red-100 text-red-600 transition text-2xl font-bold border-r border-gray-200"
                :class="{'bg-red-300': method === IntakeMethod.NO}"
            >
                None
            </div>
        </div>
    </div>
</template>
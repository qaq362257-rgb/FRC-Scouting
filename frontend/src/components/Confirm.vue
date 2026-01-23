<script setup>
defineProps({
    label: String
});
const isTrue = defineModel({type: Boolean, default: true});

function setTrue() {
    isTrue.value = true;
}

function setFalse() {
    isTrue.value = false;
}
</script>
<template>
    <div class="flex flex-col gap-1 mb-4">
        <label v-if="label" class="text-gray-700 font-bold ml-1">
            {{ label }}
        </label>
        <div class="flex items-center border-2 border-gray-300 rounded-xl overflow-hidden bg-white shadow-sm">
            <div
                @click="setFalse"
                class="h-12 flex grow items-center justify-center bg-red-100 text-red-600 transition text-2xl font-bold border-r border-gray-200"
                :class="{ 'bg-red-300': !isTrue }"
            >
                No
            </div>
            <div
                @click="setTrue"
                class="h-12 flex grow items-center justify-center bg-green-100 text-green-600 transition text-2xl font-bold border-l border-gray-200"
                :class="{ 'bg-green-300': isTrue }"
            >
                Yes
            </div>
        </div>
    </div>
</template>
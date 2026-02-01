<script setup>
import Option from './Option.vue';

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
            <Option name="True" :selected="isTrue" @click="setTrue()"></Option>
            <Option name="False" :selected="!isTrue" @click="setFalse()"></Option>
        </div>
    </div>
</template>
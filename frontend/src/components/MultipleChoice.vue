<script setup>
import Option from './Option.vue';

const props = defineProps({
    label: String,
    options: {
        type: Array,
        default: () => [] 
    }
});

const results = defineModel([]);

function choose(option) {
    if (results.value.includes(option)) {
        results.value = results.value.filter((t) => t !== option);
    } else {
        results.value.push(option);
    }
}
</script>
<template>
    <div class="flex flex-col gap-1 mb-4">
        <label v-if="label" class="text-gray-700 font-bold ml-1">
            {{ label }}
        </label>
        <div class="flex flex-col items-stretch border-2 border-gray-300 rounded-xl overflow-hidden bg-white shadow-sm">
            <Option
                v-for="(option, id) in options"
                :name="option"
                :key="id"
                @click="choose(option)"
                :selected="results.includes(option)"
            ></Option>
        </div>
    </div>
</template>
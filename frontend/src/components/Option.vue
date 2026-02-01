<script setup>

defineProps({
    name: String,
    selected:Boolean
});

</script>
<template>
    <div
        class="h-12 grid grow items-center justify-center bg-gray-100 text-gray-600 transition text-2xl font-bold border-r border-gray-200"
        :class="{'bg-gray-300': selected}"
    >
        {{ name }}
    </div>
</template>
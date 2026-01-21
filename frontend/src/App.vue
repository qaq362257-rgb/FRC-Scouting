<script setup>
import counter from './components/Counter.vue';
import { ref } from 'vue';
const hitCount = ref(0);
</script>
<template>
    <counter label="Hit" v-model="hitCount"></counter>
    <div>Hit : {{ hitCount }}</div>
</template>
<style scoped>

</style>
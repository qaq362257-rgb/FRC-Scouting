<script setup>
import counter from './components/Counter.vue';
import confirm from './components/Confirm.vue';
import { ref } from 'vue';
const hitCount = ref(0);
const doLeaveLine = ref(true);
</script>
<template>
    <counter label="Hit" v-model="hitCount"></counter>
    <div>Hit : {{ hitCount }}</div>
    <confirm label="Leave Line" v-model="doLeaveLine"></confirm>
    <div>Leave Line : {{ doLeaveLine }}</div>
</template>
<style scoped>

</style>
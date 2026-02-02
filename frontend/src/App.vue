<script setup>
import counter from './components/Counter.vue';
import confirm from './components/Confirm.vue';
import SingleChoice from './components/SingleChoice.vue';
import { ref } from 'vue';
import { IntakeMethodArr } from './Constants';
const hitCount = ref(0);
const doLeaveLine = ref(true);
const intake = ref();
</script>
<template>
    <counter label="Hit" v-model="hitCount"></counter>
    <div>Hit : {{ hitCount }}</div>
    <confirm label="Leave Line" v-model="doLeaveLine"></confirm>
    <div>Leave Line : {{ doLeaveLine }}</div>
    <SingleChoice label="intake" v-model="intake", :options="IntakeMethodArr"></SingleChoice>
    <div>Leave Line : {{ intake }}</div>
</template>
<style scoped>

</style>
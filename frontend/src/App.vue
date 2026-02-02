<script setup>
import counter from './components/Counter.vue';
import confirm from './components/Confirm.vue';
import SingleChoice from './components/SingleChoice.vue';
import { ref } from 'vue';
import { IntakeMethodArr, UsesArr } from './Constants';
import MultipleChoice from './components/MultipleChoice.vue';
const hitCount = ref(0);
const doLeaveLine = ref(true);
const intake = ref();
const uses = ref([]);
</script>
<template>
    <counter label="Hit" v-model="hitCount"></counter>
    <div>Hit : {{ hitCount }}</div>
    <confirm label="Leave Line" v-model="doLeaveLine"></confirm>
    <div>Leave Line : {{ doLeaveLine }}</div>
    <SingleChoice label="intake" v-model="intake" :options="IntakeMethodArr"></SingleChoice>
    <div>Intake Method : {{ intake }}</div>
    <MultipleChoice label="uses" v-model="uses" :options="UsesArr"></MultipleChoice>
    <div>Uses : {{ uses }}</div>
</template>
<style scoped>

</style>
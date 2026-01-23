<script setup>
import counter from './components/Counter.vue';
import confirm from './components/Confirm.vue';
import hangingState from './components/HangingState.vue';
import intakeMethod from './components/IntakeMethod.vue';
import { HangingState, IntakeMethod } from './Constants';
import { ref } from 'vue';
const hitCount = ref(0);
const doLeaveLine = ref(true);
const autoHangingState = ref(HangingState.NO);
const intake = ref(IntakeMethod.NO);
</script>
<template>
    <counter label="Hit" v-model="hitCount"></counter>
    <div>Hit : {{ hitCount }}</div>
    <confirm label="Leave Line" v-model="doLeaveLine"></confirm>
    <div>Leave Line : {{ doLeaveLine }}</div>
    <hangingState label="Auto Hanging" v-model="autoHangingState"></hangingState>
    <div>Auto Hanging : {{ autoHangingState }}</div>
    <intakeMethod label="Intake Method" v-model="intake"></intakeMethod>
    <div>Intake Method : {{ intake }}</div>
</template>
<style scoped>

</style>
<script setup>
import counter from './components/Counter.vue';
import confirm from './components/Confirm.vue';
import hangingState from './components/HangingState.vue';
import intakeMethod from './components/IntakeMethod.vue';
import teamColor from './components/TeamColor.vue';
import startPos from './components/StartPos.vue';
import uses from './components/Uses.vue';
import { HangingState, IntakeMethod, TeamColor, StartPos } from './Constants';
import { ref } from 'vue';
const hitCount = ref(0);
const doLeaveLine = ref(true);
const autoHangingState = ref(HangingState.NO);
const intake = ref(IntakeMethod.NO);
const color = ref(TeamColor.RED)
const pos = ref(StartPos.MIDDLE)
const use = ref([])
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
    <teamColor label="Team Color" v-model="color"></teamColor>
    <div>Team Color : {{ color }}</div>
    <startPos label="Start Position" v-model="pos"></startPos>
    <div>Start Position : {{ pos }}</div>
    <uses label="Uses" v-model="use"></uses>
    <div>Uses : {{ use }}</div>
</template>
<style scoped>

</style>
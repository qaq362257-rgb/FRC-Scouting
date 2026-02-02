<script setup>
const prop = defineProps({
  label: String,
  max: {
    type: Number,
    default: -1
  }
});
const count = defineModel({ type: Number, default: 0 })

const increment = () => {
  if (prop.max !== -1) {
    if (count.value < prop.max) {
      count.value++;
    }
  } else {
    count.value++;
  }
}

const decrement = () => {
  if (count.value > 0) {
    count.value--;
  }
}
</script>

<template>
  <div class="flex flex-col gap-1 mb-4">
    <label v-if="label" class="text-gray-700 font-bold ml-1">
      {{ label }}
    </label>
    <div class="flex items-center border-2 border-gray-300 rounded-xl overflow-hidden bg-white shadow-sm">
      <button 
        type="button" 
        @click="decrement" 
        :disabled="count<=0"
        class="w-12 h-12 flex items-center justify-center bg-red-100 text-red-600 active:bg-red-200 transition text-2xl font-bold border-r border-gray-200 disabled:opacity-50 disabled:bg-gray-100 disabled:text-gray-400"
      >
        -
      </button>
      <div class="flex-1 text-center text-2xl font-mono font-medium py-2">
        {{ count }}
      </div>
      <button 
        type="button" 
        @click="increment" 
        :disabled="max!==-1&&count>=max"
        class="w-12 h-12 flex items-center justify-center bg-green-100 text-green-600 active:bg-green-200 transition text-2xl font-bold border-l border-gray-200 disabled:opacity-50 disabled:bg-gray-100 disabled:text-gray-400"
      >
        +
      </button>
    </div>
  </div>
</template>
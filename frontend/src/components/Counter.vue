<script setup>
defineProps({
  label: String
});
const count = defineModel({ type: Number, default: 0 })

const increment = () => {
  count.value++
}

const decrement = () => {
  if (count.value > 0) {
    count.value--
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
        class="w-12 h-12 flex items-center justify-center bg-red-100 text-red-600 active:bg-red-200 transition text-2xl font-bold border-r border-gray-200"
      >
        -
      </button>
      <div class="flex-1 text-center text-2xl font-mono font-medium py-2">
        {{ count }}
      </div>
      <button 
        type="button" 
        @click="increment" 
        class="w-12 h-12 flex items-center justify-center bg-green-100 text-green-600 active:bg-green-200 transition text-2xl font-bold border-l border-gray-200"
      >
        +
      </button>
    </div>
  </div>
</template>
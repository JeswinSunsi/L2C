<script setup>
import { ref, computed } from 'vue';

const props = defineProps(['data']);
const emit = defineEmits(['completed']);

const currentValue = ref(props.data.initial_value);
const pipeline = ref([]);
const isComplete = ref(false);

const applyMethod = (method) => {
  if (isComplete.value) return;

  let val = currentValue.value;
  // Remove quotes for processing
  let rawVal = val.replace(/^"|"$/g, '');

  switch (method.name) {
    case '.strip()':
      rawVal = rawVal.trim();
      break;
    case '.lower()':
      rawVal = rawVal.toLowerCase();
      break;
    case '.upper()':
      rawVal = rawVal.toUpperCase();
      break;
    case ".replace(' ', '_')":
      rawVal = rawVal.replaceAll(' ', '_');
      break;
  }

  currentValue.value = `"${rawVal}"`;
  pipeline.value.push(method.name);

  if (currentValue.value === props.data.target_value) {
    isComplete.value = true;
    setTimeout(() => {
      emit('completed');
    }, 1500);
  }
};

const reset = () => {
  currentValue.value = props.data.initial_value;
  pipeline.value = [];
  isComplete.value = false;
};
</script>

<template>
  <div class="flex flex-col gap-8">
    <!-- Display Area -->
    <div class="bg-white border border-gray-200 rounded-xl p-8 text-center shadow-sm flex flex-col items-center gap-4 relative">
      <div v-if="isComplete" class="absolute -top-4 bg-green-600 text-white px-4 py-1 rounded-full text-sm font-bold shadow-lg animate-bounce">
        Success!
      </div>
      
      <div class="flex items-center gap-2 text-sm text-gray-500 bg-gray-50 px-4 py-2 rounded-full border border-gray-200">
        Target: <span class="font-mono font-bold text-gray-900">{{ data.target_value }}</span>
      </div>
      
      <div class="text-xs font-bold text-gray-400 uppercase tracking-wider mt-2">Current Value</div>
      <div 
        class="font-mono text-2xl text-gray-900 bg-gray-100 px-6 py-3 rounded-lg border border-gray-200 transition-all duration-300"
        :class="{ 'bg-blue-50 border-blue-500 scale-105': pipeline.length > 0, 'bg-green-50 border-green-500': isComplete }"
      >
        {{ currentValue }}
      </div>
    </div>

    <!-- Methods Grid -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
      <button 
        v-for="method in data.methods" 
        :key="method.name"
        @click="applyMethod(method)"
        :disabled="isComplete"
        class="bg-white border border-gray-200 p-4 rounded-lg text-left hover:border-blue-500 hover:bg-blue-50 transition-all group disabled:opacity-50 disabled:cursor-not-allowed"
      >
        <div class="font-mono text-blue-600 font-bold mb-1 group-hover:text-blue-700">{{ method.name }}</div>
        <div class="text-xs text-gray-500">{{ method.desc }}</div>
      </button>
    </div>

    <!-- Pipeline -->
    <div class="border-t border-gray-200 pt-6">
      <div class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-4">Pipeline</div>
      <div class="flex flex-wrap gap-2 items-center text-sm font-mono text-gray-500">
        <span class="bg-gray-100 px-2 py-1 rounded border border-gray-200">{{ data.initial_value }}</span>
        <div v-for="(step, index) in pipeline" :key="index" class="flex items-center gap-2 animate-fade-in">
          <span class="text-gray-300">→</span>
          <span class="text-blue-600 font-bold">{{ step }}</span>
        </div>
      </div>
    </div>

    <button 
      @click="reset" 
      class="mt-auto py-3 border border-gray-300 text-gray-700 font-medium rounded-lg hover:bg-gray-50 transition-colors"
    >
      Reset
    </button>
  </div>
</template>

<style scoped>
.animate-fade-in {
  animation: fadeIn 0.3s ease-out forwards;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(5px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>

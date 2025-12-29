<script setup>
import { ref, computed } from 'vue';

const props = defineProps(['data']);
const emit = defineEmits(['completed']);

const currentStepIndex = ref(-1); // -1 means not started
const isComplete = ref(false);

const currentStep = computed(() => {
  if (currentStepIndex.value === -1) return null;
  return props.data.steps[currentStepIndex.value];
});

const currentVariables = computed(() => {
  if (!currentStep.value) return {};
  return currentStep.value.variables;
});

const currentOutput = computed(() => {
  // Accumulate output up to current step
  if (currentStepIndex.value === -1) return [];
  const outputs = [];
  for (let i = 0; i <= currentStepIndex.value; i++) {
    if (props.data.steps[i].output) {
      outputs.push(props.data.steps[i].output);
    }
  }
  return outputs;
});

const nextStep = () => {
  if (currentStepIndex.value < props.data.steps.length - 1) {
    currentStepIndex.value++;
  } else {
    isComplete.value = true;
    setTimeout(() => {
      emit('completed');
    }, 1500);
  }
};

const reset = () => {
  currentStepIndex.value = -1;
  isComplete.value = false;
};
</script>

<template>
  <div class="flex flex-col lg:flex-row gap-6 h-[500px]">
    <!-- Code Panel -->
    <div class="flex-1 flex flex-col bg-white border border-gray-200 rounded-lg overflow-hidden">
      <div class="bg-gray-50 px-4 py-3 border-b border-gray-200 text-xs font-bold text-gray-500 uppercase tracking-wider flex justify-between items-center">
        <span>Source Code</span>
        <button @click="reset" class="text-blue-600 hover:text-blue-800">Reset</button>
      </div>
      <div class="flex-1 bg-gray-800 overflow-y-auto py-4 font-mono text-sm">
        <div 
          v-for="(line, index) in data.code_lines" 
          :key="line.id"
          class="px-4 py-1 flex gap-4 relative transition-colors"
          :class="{ 'bg-gray-700': currentStep && currentStep.line === line.id }"
        >
          <div class="text-gray-500 w-6 text-right select-none">{{ index + 1 }}</div>
          <div class="text-gray-300" :class="`ml-${line.indent * 6}`">
            <span v-if="currentStep && currentStep.line === line.id" class="absolute left-1 text-blue-400 font-bold">→</span>
            <span v-html="line.html"></span>
          </div>
        </div>
      </div>
      <div class="p-4 border-t border-gray-200 bg-gray-50">
        <button 
          @click="nextStep" 
          class="w-full py-2 bg-blue-600 text-white font-medium rounded hover:bg-blue-700 transition-colors"
          :disabled="isComplete"
        >
          {{ currentStepIndex === -1 ? 'Start Debugging' : (isComplete ? 'Completed' : 'Step Into →') }}
        </button>
      </div>
    </div>

    <!-- State Panel -->
    <div class="flex-1 flex flex-col gap-6">
      <!-- Variables -->
      <div class="flex-1 bg-white border border-gray-200 rounded-lg overflow-hidden flex flex-col">
        <div class="bg-gray-50 px-4 py-3 border-b border-gray-200 text-xs font-bold text-gray-500 uppercase tracking-wider">
          Variables
        </div>
        <div class="p-4 font-mono text-sm">
          <div v-if="Object.keys(currentVariables).length === 0" class="text-gray-400 italic">
            No variables in memory
          </div>
          <div v-else class="flex flex-col gap-2">
            <div v-for="(value, name) in currentVariables" :key="name" class="flex justify-between border-b border-gray-100 pb-1 last:border-0">
              <span class="text-red-500">{{ name }}</span>
              <span class="text-blue-600">{{ value }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Output -->
      <div class="h-1/3 bg-black rounded-lg overflow-hidden flex flex-col text-green-400 font-mono text-sm">
        <div class="bg-gray-900 px-4 py-2 text-xs font-bold text-gray-500 uppercase tracking-wider">
          Terminal Output
        </div>
        <div class="p-4 flex-1 overflow-y-auto">
          <div v-for="(line, i) in currentOutput" :key="i">> {{ line }}</div>
          <div class="animate-pulse">_</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.ml-0 { margin-left: 0px; }
.ml-6 { margin-left: 24px; }
</style>

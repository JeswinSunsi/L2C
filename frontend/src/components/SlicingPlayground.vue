<script setup>
import { ref, computed } from 'vue';

const props = defineProps(['data']);
const emit = defineEmits(['completed']);

const start = ref(1);
const stop = ref(5);
const step = ref(1);

const listItems = computed(() => props.data.list_items);

const selectedIndices = computed(() => {
  const indices = [];
  const len = listItems.value.length;
  
  let s = start.value === '' ? 0 : parseInt(start.value);
  let e = stop.value === '' ? len : parseInt(stop.value);
  let st = step.value === '' ? 1 : parseInt(step.value);

  if (isNaN(s)) s = 0;
  if (isNaN(e)) e = len;
  if (isNaN(st)) st = 1;

  // Handle negative indices
  if (s < 0) s += len;
  if (e < 0) e += len;

  // Clamp
  // Python slicing is forgiving, but for visualization we'll try to match logic
  
  if (st > 0) {
    for (let i = s; i < e; i += st) {
      if (i >= 0 && i < len) indices.push(i);
    }
  } else if (st < 0) {
    for (let i = s; i > e; i += st) {
      if (i >= 0 && i < len) indices.push(i);
    }
  }
  
  return indices;
});

const result = computed(() => {
  return selectedIndices.value.map(i => listItems.value[i]);
});

const finish = () => {
    emit('completed');
}
</script>

<template>
  <div class="flex flex-col gap-8">
    <!-- List Visualization -->
    <div class="flex justify-center gap-2 overflow-x-auto py-4 min-h-[120px]">
      <div 
        v-for="(item, index) in listItems" 
        :key="index"
        class="flex flex-col items-center gap-2 min-w-[40px] transition-all duration-300"
        :class="{ '-translate-y-2': selectedIndices.includes(index) }"
      >
        <div class="text-xs font-mono text-gray-400" :class="{ 'text-blue-600 font-bold': selectedIndices.includes(index) }">{{ index }}</div>
        <div 
          class="w-12 h-12 flex items-center justify-center rounded-lg border-2 font-mono text-xl font-bold transition-colors duration-300"
          :class="selectedIndices.includes(index) ? 'bg-blue-100 border-blue-500 text-blue-700 shadow-lg' : 'bg-white border-gray-200 text-gray-700'"
        >
          {{ item }}
        </div>
        <div class="text-xs font-mono text-gray-400" :class="{ 'text-blue-600 font-bold': selectedIndices.includes(index) }">{{ index - listItems.length }}</div>
      </div>
    </div>

    <!-- Controls -->
    <div class="bg-white border border-gray-200 rounded-xl p-6 flex flex-col gap-6">
      <div class="font-mono text-lg text-center bg-gray-50 p-4 rounded-lg border border-gray-200">
        my_list[<span class="text-blue-600 font-bold">{{ start }}</span>:<span class="text-blue-600 font-bold">{{ stop }}</span>:<span class="text-blue-600 font-bold">{{ step }}</span>]
      </div>

      <div class="grid grid-cols-3 gap-6">
        <div class="flex flex-col gap-2">
          <label class="text-xs font-bold text-gray-500 uppercase">Start</label>
          <input type="number" v-model="start" class="p-2 border border-gray-300 rounded font-mono focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none">
        </div>
        <div class="flex flex-col gap-2">
          <label class="text-xs font-bold text-gray-500 uppercase">Stop</label>
          <input type="number" v-model="stop" class="p-2 border border-gray-300 rounded font-mono focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none">
        </div>
        <div class="flex flex-col gap-2">
          <label class="text-xs font-bold text-gray-500 uppercase">Step</label>
          <input type="number" v-model="step" class="p-2 border border-gray-300 rounded font-mono focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none">
        </div>
      </div>
    </div>

    <!-- Result -->
    <div class="text-center">
      <div class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-2">Result</div>
      <div class="font-mono text-xl text-green-600 min-h-[32px]">
        {{ JSON.stringify(result) }}
      </div>
    </div>
    
    <button 
      @click="finish" 
      class="w-full py-3 bg-blue-600 text-white font-medium rounded-lg hover:bg-blue-700 transition-colors mt-4"
    >
      Continue
    </button>
  </div>
</template>

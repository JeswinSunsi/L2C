<script setup>
import { ref, onMounted } from 'vue';

const props = defineProps(['data']);
const emit = defineEmits(['completed']);

const sourceLines = ref([]);
const solutionLines = ref([]);
const showFeedback = ref(false);
const isCorrect = ref(false);

onMounted(() => {
  // Shuffle lines initially
  sourceLines.value = [...props.data.puzzle_lines].sort(() => Math.random() - 0.5);
});

const moveToSolution = (line) => {
  sourceLines.value = sourceLines.value.filter(l => l.id !== line.id);
  solutionLines.value.push(line);
  showFeedback.value = false;
};

const moveToSource = (line) => {
  solutionLines.value = solutionLines.value.filter(l => l.id !== line.id);
  sourceLines.value.push(line);
  showFeedback.value = false;
};

const checkAnswer = () => {
  const currentOrder = solutionLines.value.map(l => l.id);
  const correctOrder = props.data.correct_order;
  
  isCorrect.value = JSON.stringify(currentOrder) === JSON.stringify(correctOrder);
  showFeedback.value = true;

  if (isCorrect.value) {
    setTimeout(() => {
      emit('completed');
    }, 1500);
  }
};
</script>

<template>
  <div class="flex flex-col gap-6">
    <!-- Solution Area -->
    <div>
      <div class="text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">Your Solution</div>
      <div 
        class="bg-gray-800 rounded-lg min-h-[180px] p-4 flex flex-col gap-1 border border-gray-700 transition-all"
        :class="{ 'ring-2 ring-green-500': isCorrect && showFeedback, 'ring-2 ring-red-500': !isCorrect && showFeedback }"
      >
        <div v-if="solutionLines.length === 0" class="flex-1 flex items-center justify-center text-gray-500 italic text-sm">
          Tap lines below to add them here
        </div>
        <div 
          v-for="line in solutionLines" 
          :key="line.id"
          @click="moveToSource(line)"
          class="py-2 px-0 text-gray-200 font-mono text-sm cursor-pointer hover:bg-white/5 rounded"
          :class="`ml-${line.indent * 6}`"
        >
          <span v-html="line.html"></span>
        </div>
      </div>
    </div>

    <!-- Source Area -->
    <div>
      <div class="text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">Available Lines</div>
      <div class="flex flex-col gap-2">
        <div 
          v-for="line in sourceLines" 
          :key="line.id"
          @click="moveToSolution(line)"
          class="p-3 bg-white border border-gray-200 rounded-md font-mono text-sm cursor-pointer hover:bg-gray-50 hover:border-gray-300 shadow-sm transition-all"
        >
          <span v-html="line.html"></span>
        </div>
      </div>
    </div>

    <div v-if="showFeedback" class="text-center font-medium" :class="isCorrect ? 'text-green-600' : 'text-red-600'">
      {{ isCorrect ? 'Correct! Logic verified.' : 'Incorrect order. Try again.' }}
    </div>

    <button 
      @click="checkAnswer" 
      :disabled="solutionLines.length === 0"
      class="w-full py-3 bg-blue-600 text-white font-medium rounded-lg hover:bg-blue-700 disabled:bg-gray-200 disabled:text-gray-400 disabled:cursor-not-allowed transition-colors mt-auto"
    >
      Run Code
    </button>
  </div>
</template>

<style scoped>
/* Indentation helpers since Tailwind might purge unused dynamic classes */
.ml-0 { margin-left: 0px; }
.ml-6 { margin-left: 24px; }
.ml-12 { margin-left: 48px; }
</style>

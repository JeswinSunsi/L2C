<script setup>
import { ref } from 'vue';

const props = defineProps(['data']);
const emit = defineEmits(['completed']);

const selectedOption = ref(null);
const isCorrect = ref(false);
const showFeedback = ref(false);

const selectOption = (option) => {
  if (showFeedback.value && isCorrect.value) return; // Prevent changing after success
  selectedOption.value = option;
  showFeedback.value = false;
};

const checkAnswer = () => {
  if (!selectedOption.value) return;
  
  isCorrect.value = selectedOption.value.is_correct;
  showFeedback.value = true;

  if (isCorrect.value) {
    setTimeout(() => {
      emit('completed');
    }, 1500);
  }
};
</script>

<template>
  <div>
    <div v-if="data.code_block" class="bg-gray-800 text-gray-200 p-6 rounded-lg font-mono text-sm mb-8 overflow-x-auto border border-gray-700" v-html="data.code_block"></div>

    <div class="mb-4 font-semibold text-gray-900">{{ data.quiz.question }}</div>

    <div class="flex flex-col gap-3 mb-8">
      <button 
        v-for="option in data.quiz.options" 
        :key="option.id"
        @click="selectOption(option)"
        class="p-4 text-left border rounded-lg transition-all flex items-center gap-3 hover:bg-gray-50"
        :class="{
          'border-blue-500 bg-blue-50 ring-1 ring-blue-500': selectedOption?.id === option.id && !showFeedback,
          'border-green-500 bg-green-50 ring-1 ring-green-500': showFeedback && selectedOption?.id === option.id && option.is_correct,
          'border-red-500 bg-red-50 ring-1 ring-red-500': showFeedback && selectedOption?.id === option.id && !option.is_correct,
          'border-gray-200': selectedOption?.id !== option.id
        }"
      >
        <div class="w-4 h-4 rounded-full border border-gray-300 flex-shrink-0"
             :class="{
               'border-blue-500 bg-blue-500': selectedOption?.id === option.id && !showFeedback,
               'border-green-500 bg-green-500': showFeedback && selectedOption?.id === option.id && option.is_correct,
               'border-red-500 bg-red-500': showFeedback && selectedOption?.id === option.id && !option.is_correct
             }"
        ></div>
        {{ option.text }}
      </button>
    </div>

    <div v-if="showFeedback" class="mb-4 text-center font-medium" :class="isCorrect ? 'text-green-600' : 'text-red-600'">
      {{ isCorrect ? data.quiz.feedback_correct : data.quiz.feedback_wrong }}
    </div>

    <button 
      @click="checkAnswer" 
      :disabled="!selectedOption"
      class="w-full py-3 bg-blue-600 text-white font-medium rounded-lg hover:bg-blue-700 disabled:bg-gray-200 disabled:text-gray-400 disabled:cursor-not-allowed transition-colors"
    >
      Check Answer
    </button>
  </div>
</template>

<style scoped>
/* Add any specific styles here if needed, mostly using Tailwind */
</style>

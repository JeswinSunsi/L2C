<script setup>
import { ref, onMounted, watch, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import Quiz from '../components/Quiz.vue';
import LogicBuilder from '../components/LogicBuilder.vue';
import VisualDebugger from '../components/VisualDebugger.vue';
import MethodLab from '../components/MethodLab.vue';
import SlicingPlayground from '../components/SlicingPlayground.vue';

const route = useRoute();
const router = useRouter();
const authStore = useAuthStore();
const lesson = ref(null);
const loading = ref(true);
const error = ref(null);

const fetchLesson = async (id) => {
  loading.value = true;
  error.value = null;
  try {
    const response = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/lessons/${id}`);
    if (!response.ok) throw new Error('Lesson not found');
    lesson.value = await response.json();
  } catch (err) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  fetchLesson(route.params.id);
});

watch(() => route.params.id, (newId) => {
  fetchLesson(newId);
});

const currentComponent = computed(() => {
  if (!lesson.value) return null;
  switch (lesson.value.type) {
    case 'quiz': return Quiz;
    case 'logic_builder': return LogicBuilder;
    case 'visual_debugger': return VisualDebugger;
    case 'method_lab': return MethodLab;
    case 'slicing_playground': return SlicingPlayground;
    default: return null;
  }
});

const handleNext = async (score = 100) => {
  if (authStore.isAuthenticated && lesson.value) {
    try {
        await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/lessons/${lesson.value.id}/complete`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${authStore.token}`
            },
            body: JSON.stringify({
                lesson_id: lesson.value.id,
                completed: true,
                score: score
            })
        });
    } catch (e) {
        console.error("Failed to save progress", e);
    }
  }

  if (lesson.value && lesson.value.next_lesson_id) {
    router.push(`/lesson/${lesson.value.next_lesson_id}`);
  } else {
    router.push('/dashboard');
  }
};
</script>

<template>
  <div class="min-h-screen bg-gray-50 flex flex-col">
    <header class="bg-white border-b border-gray-200 px-6 py-4 flex items-center gap-6 sticky top-0 z-10">
      <button @click="router.push('/dashboard')" class="text-gray-500 hover:text-gray-900 transition-colors">
        ← Dashboard
      </button>
      <div class="flex-1 h-1 bg-gray-200 rounded-full overflow-hidden">
        <div class="h-full bg-blue-600 transition-all duration-500" :style="{ width: `${(route.params.id / 12) * 100}%` }"></div>
      </div>
    </header>

    <main class="flex-1 max-w-3xl w-full mx-auto p-6 overflow-y-auto">
      <div v-if="loading" class="text-center py-12 text-gray-500">Loading lesson...</div>
      <div v-else-if="error" class="text-center py-12 text-red-500">{{ error }}</div>
      <div v-else>
        <h1 class="text-2xl font-bold text-gray-900 mb-4">{{ lesson.title }}</h1>
        <p class="text-gray-600 mb-8 leading-relaxed">{{ lesson.description }}</p>
        
        <component 
          :is="currentComponent" 
          :data="lesson" 
          @completed="handleNext"
        />
      </div>
    </main>
  </div>
</template>

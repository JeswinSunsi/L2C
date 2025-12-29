<script setup>
import { ref, onMounted } from 'vue';
import { useAuthStore } from '../stores/auth';

const authStore = useAuthStore();
const lessons = ref([]);
const progress = ref([]);
const error = ref(null);

onMounted(async () => {
  try {
    // Fetch lessons
    const resLessons = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/lessons`);
    if (!resLessons.ok) throw new Error('Failed to fetch lessons');
    lessons.value = await resLessons.json();

    // Fetch progress
    if (authStore.isAuthenticated) {
      const resProgress = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/users/me/progress`, {
          headers: {
              'Authorization': `Bearer ${authStore.token}`
          }
      });
      if (resProgress.ok) {
          progress.value = await resProgress.json();
      }
    }
  } catch (e) {
    console.error('Dashboard Error:', e);
    error.value = "Could not connect to the server. Please ensure the backend is running.";
  }
});

const isCompleted = (lessonId) => {
    const p = progress.value.find(p => p.lesson_id === lessonId);
    return p && p.completed;
};
</script>

<template>
  <div class="min-h-screen bg-slate-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-7xl mx-auto">
      <div v-if="error" class="mb-8 bg-red-50 border-l-4 border-red-400 p-4">
        <div class="flex">
          <div class="flex-shrink-0">
            <svg class="h-5 w-5 text-red-400" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
            </svg>
          </div>
          <div class="ml-3">
            <p class="text-sm text-red-700">{{ error }}</p>
          </div>
        </div>
      </div>
      <h1 class="text-3xl font-bold text-slate-900 mb-8">Your Learning Path</h1>
      
      <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        <div v-for="lesson in lessons" :key="lesson.id" class="bg-white overflow-hidden shadow rounded-lg hover:shadow-md transition-shadow">
          <div class="px-4 py-5 sm:p-6">
            <div class="flex items-center justify-between mb-4">
                <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-indigo-100 text-indigo-800 capitalize">
                    {{ lesson.type }}
                </span>
                <span v-if="isCompleted(lesson.id)" class="text-green-500">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                </span>
            </div>
            <h3 class="text-lg font-medium text-slate-900 truncate">{{ lesson.title }}</h3>
            <p class="mt-1 text-sm text-slate-500">{{ lesson.description || 'Master this concept to level up.' }}</p>
            <div class="mt-4">
                <router-link :to="`/lesson/${lesson.id}`" class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                    {{ isCompleted(lesson.id) ? 'Review' : 'Start Lesson' }}
                </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

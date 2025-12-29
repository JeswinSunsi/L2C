<script setup>
import { ref, onMounted } from 'vue';
import { useAuthStore } from '../stores/auth';

const authStore = useAuthStore();
const lessons = ref([]);
const progress = ref([]);

onMounted(async () => {
  // Fetch lessons
  const resLessons = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/lessons`);
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
});

const isCompleted = (lessonId) => {
    const p = progress.value.find(p => p.lesson_id === lessonId);
    return p && p.completed;
};
</script>

<template>
  <div class="min-h-screen bg-slate-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-7xl mx-auto">
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

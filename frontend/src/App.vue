<script setup>
import { useAuthStore } from './stores/auth';
import { useRouter, useRoute } from 'vue-router';

const authStore = useAuthStore();
const router = useRouter();
const route = useRoute();

const logout = () => {
  authStore.logout();
};
</script>

<template>
  <div class="min-h-screen bg-slate-50">
    <nav v-if="authStore.isAuthenticated && route.name !== 'Landing'" class="bg-white border-b border-slate-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
          <div class="flex">
            <div class="flex-shrink-0 flex items-center cursor-pointer" @click="router.push('/')">
              <div class="w-8 h-8 bg-slate-900 rounded-md flex items-center justify-center text-white font-mono font-bold text-sm">
                  &lt;/&gt;
              </div>
              <span class="ml-2 font-display font-bold text-xl tracking-tight text-slate-900">PolyGlot_Lab</span>
            </div>
            <div class="hidden sm:ml-6 sm:flex sm:space-x-8">
              <router-link to="/dashboard" class="border-transparent text-slate-500 hover:border-gray-300 hover:text-slate-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium" active-class="border-indigo-500 text-slate-900">
                Dashboard
              </router-link>
            </div>
          </div>
          <div class="flex items-center">
            <button @click="logout" class="text-slate-500 hover:text-slate-700 px-3 py-2 rounded-md text-sm font-medium">
              Sign out
            </button>
          </div>
        </div>
      </div>
    </nav>
    <router-view></router-view>
  </div>
</template>

<style>
</style>

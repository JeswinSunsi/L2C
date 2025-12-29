import { createRouter, createWebHistory } from 'vue-router'
import LandingView from '../views/LandingView.vue'
import LessonView from '../views/LessonView.vue'

const routes = [
  {
    path: '/',
    name: 'Landing',
    component: LandingView
  },
  {
    path: '/lesson/:id',
    name: 'Lesson',
    component: LessonView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { jwtDecode } from 'jwt-decode';

export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem('token'));
  const user = ref(null);
  const router = useRouter();

  const isAuthenticated = computed(() => !!token.value);

  async function login(email, password) {
    const formData = new FormData();
    formData.append('username', email);
    formData.append('password', password);

    const response = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/token`, {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      throw new Error('Login failed');
    }

    const data = await response.json();
    token.value = data.access_token;
    localStorage.setItem('token', data.access_token);
    
    // Decode token to get user info if needed, or fetch user profile
    await fetchUser();
    
    router.push('/dashboard');
  }

  async function register(email, password) {
    const response = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/register`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, password }),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Registration failed');
    }
    
    // Auto login after register
    await login(email, password);
  }

  async function fetchUser() {
    if (!token.value) return;
    
    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/users/me`, {
        headers: {
          'Authorization': `Bearer ${token.value}`
        }
      });
      
      if (response.ok) {
        user.value = await response.json();
      } else {
        logout();
      }
    } catch (e) {
      logout();
    }
  }

  function logout() {
    token.value = null;
    user.value = null;
    localStorage.removeItem('token');
    router.push('/login');
  }

  return { token, user, isAuthenticated, login, register, logout, fetchUser };
});

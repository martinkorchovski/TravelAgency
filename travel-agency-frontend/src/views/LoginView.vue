<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const router = useRouter()
const auth = useAuthStore()
const username = ref('')
const password = ref('')
const error = ref('')

async function login() {
  error.value = ''
  try {
    const response = await fetch('http://127.0.0.1:8000/api/users/login/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username: username.value, password: password.value })
    })
    const data = await response.json()
    if (response.ok) {
      auth.login(data.access, username.value)
      router.push('/')
    } else {
      error.value = 'Погрешно корисничко име или лозинка'
    }
  } catch {
    error.value = 'Грешка при поврзување со серверот'
  }
}
</script>

<template>
  <div
    class="min-h-screen flex items-center justify-center px-6 py-16 bg-cover bg-center relative"
    style="background-image: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1600');"
  >
    <div class="absolute inset-0 bg-black/50"></div>

    <div class="relative z-10 w-full max-w-5xl grid grid-cols-1 md:grid-cols-2 bg-white rounded-3xl shadow-2xl overflow-hidden">

      <!-- Left Side -->
      <div class="hidden md:flex flex-col justify-center p-10 bg-orange-500 text-white">
        <p class="uppercase tracking-wider font-semibold mb-3">TravelAgency</p>

        <h2 class="text-4xl font-bold mb-4">
          Добредојде назад
        </h2>

        <p class="text-white/90">
          Најави се и продолжи со пребарување и резервација на твојата следна авантура.
        </p>

        <div class="mt-8 space-y-4">
          <div class="flex items-center gap-3">
            <span class="bg-white/20 rounded-full p-2">✈️</span>
            <span>Најдобри туристички понуди</span>
          </div>

          <div class="flex items-center gap-3">
            <span class="bg-white/20 rounded-full p-2">🔥</span>
            <span>Last Minute аранжмани</span>
          </div>

          <div class="flex items-center gap-3">
            <span class="bg-white/20 rounded-full p-2">🏖️</span>
            <span>Резервирај за неколку секунди</span>
          </div>
        </div>
      </div>

      <!-- Right Side -->
      <div class="p-8 md:p-10">
        <div class="mb-8">
          <p class="text-orange-500 font-semibold uppercase tracking-wider mb-2">
            Најава
          </p>

          <h1 class="text-3xl font-bold text-gray-800">
            Најави се
          </h1>

          <p class="text-gray-500 mt-2">
            Внеси ги твоите податоци за пристап.
          </p>
        </div>

        <div
          v-if="error"
          class="bg-red-100 text-red-600 p-3 rounded-xl mb-4"
        >
          {{ error }}
        </div>

        <div class="mb-4">
          <label class="block text-gray-700 font-semibold mb-1">
            Корисничко име
          </label>

          <input
            v-model="username"
            type="text"
            placeholder="user123"
            class="w-full border rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-orange-500"
          />
        </div>

        <div class="mb-6">
          <label class="block text-gray-700 font-semibold mb-1">
            Лозинка
          </label>

          <input
            v-model="password"
            type="password"
            placeholder="••••••••"
            class="w-full border rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-orange-500"
          />
        </div>

        <button
          @click="login"
          class="w-full bg-orange-500 hover:bg-orange-600 text-white py-3 rounded-xl font-bold transition"
        >
          Најави се
        </button>

        <p class="text-center mt-6 text-gray-500">
          Немаш акаунт?

          <RouterLink
            to="/register"
            class="text-orange-500 font-semibold hover:underline"
          >
            Регистрирај се
          </RouterLink>
        </p>
      </div>
    </div>
  </div>
</template>
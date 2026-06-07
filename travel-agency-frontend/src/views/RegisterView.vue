<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const username = ref('')
const email = ref('')
const password = ref('')
const error = ref('')
const success = ref('')

async function register() {
  error.value = ''
  success.value = ''
  try {
    const response = await fetch('http://127.0.0.1:8000/api/users/register/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username: username.value, email: email.value, password: password.value })
    })
    const data = await response.json()
    if (response.ok) {
      success.value = 'Успешно регистриран! Пренасочување...'
      setTimeout(() => router.push('/login'), 1500)
    } else {
      error.value = JSON.stringify(data)
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
      
      <!-- Left side -->
      <div class="hidden md:flex flex-col justify-center p-10 bg-orange-500 text-white">
        <p class="uppercase tracking-wider font-semibold mb-3">TravelAgency</p>
        <h2 class="text-4xl font-bold mb-4">Започни го твоето патување</h2>
        <p class="text-white/90">
          Креирај профил и резервирај ги најдобрите дестинации за неколку чекори.
        </p>

        <div class="mt-8 space-y-4">
          <div class="flex items-center gap-3">
            <span class="bg-white/20 rounded-full p-2">✈️</span>
            <span>Брза онлајн резервација</span>
          </div>
          <div class="flex items-center gap-3">
            <span class="bg-white/20 rounded-full p-2">🔥</span>
            <span>Last minute и early booking понуди</span>
          </div>
          <div class="flex items-center gap-3">
            <span class="bg-white/20 rounded-full p-2">🎧</span>
            <span>Поддршка за секое патување</span>
          </div>
        </div>
      </div>

      <!-- Form side -->
      <div class="p-8 md:p-10">
        <div class="mb-8">
          <p class="text-orange-500 font-semibold uppercase tracking-wider mb-2">Регистрација</p>
          <h1 class="text-3xl font-bold text-gray-800">Креирај акаунт</h1>
          <p class="text-gray-500 mt-2">Внеси ги твоите податоци за да продолжиш.</p>
        </div>

        <div v-if="error" class="bg-red-100 text-red-600 p-3 rounded-xl mb-4">
          {{ error }}
        </div>

        <div v-if="success" class="bg-green-100 text-green-600 p-3 rounded-xl mb-4">
          {{ success }}
        </div>

        <div class="mb-4">
          <label class="block text-gray-700 font-semibold mb-1">Корисничко име</label>
          <input
            v-model="username"
            type="text"
            placeholder="user"
            class="w-full border rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-orange-500"
          />
        </div>

        <div class="mb-4">
          <label class="block text-gray-700 font-semibold mb-1">Е-маил</label>
          <input
            v-model="email"
            type="email"
            placeholder="user@gmail.com"
            class="w-full border rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-orange-500"
          />
        </div>

        <div class="mb-6">
          <label class="block text-gray-700 font-semibold mb-1">Лозинка</label>
          <input
            v-model="password"
            type="password"
            placeholder="••••••••"
            class="w-full border rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-orange-500"
          />
        </div>

        <button
          @click="register"
          class="w-full bg-orange-500 hover:bg-orange-600 text-white py-3 rounded-xl font-bold transition"
        >
          Регистрирај се
        </button>

        <p class="text-center mt-6 text-gray-500">
          Веќе имаш акаунт?
          <RouterLink to="/login" class="text-orange-500 font-semibold hover:underline">
            Најави се
          </RouterLink>
        </p>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { useAuthStore } from '../stores/auth'
import { useRouter } from 'vue-router'

const auth = useAuthStore()
const router = useRouter()

function logout() {
  auth.logout()
  router.push('/')
}
</script>

<template>
  <div class="bg-gray-900 text-white text-sm py-2 px-6 flex justify-between items-center">
    <div class="flex gap-4">
      <span>📞 +389 2 323 8083</span>
      <span>✉️ info@travelagency.mk</span>
    </div>
    <div class="flex gap-4 items-center">
      <template v-if="auth.isLoggedIn()">
        <span class="text-orange-400 font-medium">Здраво, {{ auth.username }}!</span>
        <button @click="logout" class="text-red-400 hover:text-red-300">Одјави се</button>
      </template>
      <template v-else>
        <RouterLink to="/login" class="hover:text-orange-400">Најави се</RouterLink>
        <RouterLink to="/register" class="hover:text-orange-400">Регистрирај се</RouterLink>
      </template>
    </div>
  </div>

  <nav class="bg-white shadow-md px-6 py-4 flex items-center justify-between sticky top-0 z-50">
    <div class="text-2xl font-bold text-orange-500">
      <RouterLink to="/">✈️ TravelAgency</RouterLink>
    </div>

    <div class="flex gap-6 text-gray-700 font-medium">
      <RouterLink to="/" class="hover:text-orange-500 transition">
        Дома
      </RouterLink>

      <RouterLink to="/destinations" class="hover:text-orange-500 transition">
        Дестинации
      </RouterLink>

      <RouterLink to="/bookings" class="hover:text-orange-500 transition">
        Резервации
      </RouterLink>

      <RouterLink
        v-if="auth.isLoggedIn()"
        to="/my-bookings"
        class="hover:text-orange-500 transition"
      >
        Мои резервации
      </RouterLink>

      <RouterLink to="/contact" class="hover:text-orange-500 transition">
        Контакт
      </RouterLink>
    </div>

    <RouterLink
      to="/bookings"
      class="bg-orange-500 hover:bg-orange-600 text-white font-bold px-6 py-2 rounded-full transition"
    >
      Резервирај →
    </RouterLink>
  </nav>
</template>

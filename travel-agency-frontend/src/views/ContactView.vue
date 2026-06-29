<script setup lang="ts">
import { ref } from 'vue'

const name = ref('')
const email = ref('')
const message = ref('')
const error = ref('')
const success = ref('')

async function sendMessage() {
  error.value = ''
  success.value = ''
  try {
    const response = await fetch('http://127.0.0.1:8000/api/contacts/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: name.value,
        email: email.value,
        message: message.value
      })
    })
    const data = await response.json()
    if (response.ok) {
      success.value = 'Пораката е успешно испратена!'
      name.value = ''
      email.value = ''
      message.value = ''
    } else {
      error.value = JSON.stringify(data)
    }
  } catch {
    error.value = 'Грешка при поврзување со серверот'
  }
}
</script>

<template>
  <div>
    <div class="relative h-64 flex items-center justify-center text-white"
      style="background-image: url('https://images.unsplash.com/photo-1423666639041-f56000c27a9a?w=1600'); background-size: cover; background-position: center;">
      <div class="absolute inset-0 bg-black/50"></div>
      <div class="relative z-10 text-center">
        <p class="text-orange-400 font-semibold uppercase tracking-wider mb-2">Поврзи се со нас</p>
        <h1 class="text-5xl font-bold">Контакт</h1>
      </div>
    </div>

    <div class="max-w-6xl mx-auto px-6 py-16 grid grid-cols-1 md:grid-cols-2 gap-12">
      
      <div class="bg-white rounded-2xl shadow-lg p-8">
        <h2 class="text-2xl font-bold mb-6">Испрати порака</h2>

        <div v-if="error" class="bg-red-100 text-red-600 p-3 rounded-xl mb-4">{{ error }}</div>
        <div v-if="success" class="bg-green-100 text-green-600 p-3 rounded-xl mb-4 font-bold">✅ {{ success }}</div>

        <div class="flex flex-col gap-4">
          <div>
            <label class="block text-gray-600 mb-1 font-medium">Име и Презиме</label>
            <input v-model="name" type="text" placeholder="Петар Петровски"
              class="w-full border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-orange-400" />
          </div>
          <div>
            <label class="block text-gray-600 mb-1 font-medium">Е-маил</label>
            <input v-model="email" type="email" placeholder="user@gmail.com"
              class="w-full border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-orange-400" />
          </div>
          <div>
            <label class="block text-gray-600 mb-1 font-medium">Порака</label>
            <textarea v-model="message" rows="5" placeholder="Напиши ја твојата порака..."
              class="w-full border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-orange-400"></textarea>
          </div>
          <button @click="sendMessage"
            class="w-full bg-orange-500 hover:bg-orange-600 text-white font-bold py-3 rounded-full transition">
            Испрати →
          </button>
        </div>
      </div>

      <div class="flex flex-col gap-6">
        <div>
          <h2 class="text-2xl font-bold mb-6">Контакт информации</h2>
          <p class="text-gray-500">Нашиот тим е достапен секој работен ден. Контактирај не за резервации, прашања или информации.</p>
        </div>

        <div class="bg-white rounded-2xl shadow p-6 flex items-center gap-4">
          <div class="bg-orange-100 text-orange-500 text-3xl p-4 rounded-full">📞</div>
          <div>
            <h3 class="font-bold text-gray-700">Call Center</h3>
            <p class="text-gray-500">+389 2 323 8083</p>
          </div>
        </div>

        <div class="bg-white rounded-2xl shadow p-6 flex items-center gap-4">
          <div class="bg-orange-100 text-orange-500 text-3xl p-4 rounded-full">✉️</div>
          <div>
            <h3 class="font-bold text-gray-700">Е-маил</h3>
            <p class="text-gray-500">info@travelagency.mk</p>
          </div>
        </div>

        <div class="bg-white rounded-2xl shadow p-6 flex items-center gap-4">
          <div class="bg-orange-100 text-orange-500 text-3xl p-4 rounded-full">📍</div>
          <div>
            <h3 class="font-bold text-gray-700">Адреса</h3>
            <p class="text-gray-500">Скопје, Македонија</p>
          </div>
        </div>

        <div class="bg-white rounded-2xl shadow p-6 flex items-center gap-4">
          <div class="bg-orange-100 text-orange-500 text-3xl p-4 rounded-full">💬</div>
          <div>
            <h3 class="font-bold text-gray-700">Viber & WhatsApp</h3>
            <p class="text-gray-500">070 404 488</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
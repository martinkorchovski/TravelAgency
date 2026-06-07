<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { getDestinations } from '../api/destinations'

const router = useRouter()
const auth = useAuthStore()

const destinations = ref<any[]>([])
const full_name = ref('')
const email = ref('')
const phone = ref('')
const persons = ref(1)
const travel_date = ref('')
const return_date = ref('')
const destination = ref('')
const error = ref('')
const success = ref('')

onMounted(async () => {
  if (!auth.isLoggedIn()) {
    router.push('/login')
    return
  }
  destinations.value = await getDestinations()
})

async function createBooking() {
  error.value = ''
  success.value = ''
  try {
    const response = await fetch('http://127.0.0.1:8000/api/bookings/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${auth.token}`
      },
      body: JSON.stringify({
        full_name: full_name.value,
        email: email.value,
        phone: phone.value,
        persons: persons.value,
        travel_date: travel_date.value,
        return_date: return_date.value,
        destination: destination.value
      })
    })
    const data = await response.json()
    if (response.ok) {
      success.value = 'Резервацијата е успешно направена!'
      full_name.value = ''
      email.value = ''
      phone.value = ''
      persons.value = 1
      travel_date.value = ''
      return_date.value = ''
      destination.value = ''
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
    <!-- Hero -->
    <div class="relative h-64 flex items-center justify-center text-white"
      style="background-image: url('https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=1600'); background-size: cover; background-position: center;">
      <div class="absolute inset-0 bg-black/50"></div>
      <div class="relative z-10 text-center">
        <p class="text-orange-400 font-semibold uppercase tracking-wider mb-2">Онлајн резервација</p>
        <h1 class="text-5xl font-bold">Направи резервација</h1>
      </div>
    </div>

    <div class="max-w-3xl mx-auto px-6 py-16">
      <div v-if="error" class="bg-red-100 text-red-600 p-4 rounded-xl mb-6">{{ error }}</div>
      <div v-if="success" class="bg-green-100 text-green-600 p-4 rounded-xl mb-6 text-center text-lg font-bold">
        ✅ {{ success }}
      </div>

      <div class="bg-white rounded-2xl shadow-lg p-8">
        <h2 class="text-2xl font-bold mb-6 text-gray-800">Внеси ги твоите податоци</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label class="block text-gray-600 mb-1 font-medium">Целосно име</label>
            <input v-model="full_name" type="text" placeholder="Иван Иванов"
              class="w-full border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-orange-400" />
          </div>
          <div>
            <label class="block text-gray-600 mb-1 font-medium">Е-маил</label>
            <input v-model="email" type="email" placeholder="user@gmail.com"
              class="w-full border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-orange-400" />
          </div>
          <div>
            <label class="block text-gray-600 mb-1 font-medium">Телефон</label>
            <input v-model="phone" type="text" placeholder="07X XXX XXX"
              class="w-full border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-orange-400" />
          </div>
          <div>
            <label class="block text-gray-600 mb-1 font-medium">Број на лица</label>
            <input v-model="persons" type="number" min="1"
              class="w-full border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-orange-400" />
          </div>
          <div>
            <label class="block text-gray-600 mb-1 font-medium">Датум на патување</label>
            <input v-model="travel_date" type="date"
              class="w-full border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-orange-400" />
          </div>
          <div>
            <label class="block text-gray-600 mb-1 font-medium">Датум на враќање</label>
            <input v-model="return_date" type="date"
              class="w-full border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-orange-400" />
          </div>
          <div class="md:col-span-2">
            <label class="block text-gray-600 mb-1 font-medium">Дестинација</label>
            <select v-model="destination"
              class="w-full border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-orange-400">
              <option value="">-- Избери дестинација --</option>
              <option v-for="dest in destinations" :key="dest.id" :value="dest.id">
                {{ dest.name }} — €{{ dest.price }}
              </option>
            </select>
          </div>
        </div>

        <button @click="createBooking"
          class="w-full mt-8 bg-orange-500 hover:bg-orange-600 text-white font-bold py-4 rounded-full text-lg transition">
          Резервирај сега →
        </button>
      </div>
    </div>
  </div>
</template>
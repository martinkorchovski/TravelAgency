<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { getDestinations, getHotelsByDestination } from '../api/destinations'

const router = useRouter()
const route = useRoute()
const auth = useAuthStore()

const destination = ref<number | string>('')
const destinations = ref([] as any[])
const selectedHotel = ref<any>(null)
const full_name = ref('')
const email = ref('')
const phone = ref('')
const persons = ref(1)
const travel_date = ref('')
const return_date = ref('')
const error = ref('')
const success = ref('')

const nights = computed(() => {
  if (!travel_date.value || !return_date.value) return 0
  const from = new Date(travel_date.value)
  const to = new Date(return_date.value)
  const diff = Math.ceil((to.getTime() - from.getTime()) / (1000 * 60 * 60 * 24))
  return diff > 0 ? diff : 0
})

const totalPrice = computed(() => {
  console.log('hotel:', selectedHotel.value)
  console.log('nights:', nights.value)
  console.log('persons:', persons.value)
  if (!selectedHotel.value || nights.value === 0) return 0
  return (parseFloat(selectedHotel.value.price_per_night) * nights.value * persons.value).toFixed(2)
})

onMounted(async () => {
  if (!auth.isLoggedIn()) {
    router.push('/login')
    return
  }
  destinations.value = await getDestinations()

  const destId = route.query.destinationId
  const hotelId = route.query.hotelId

  if (destId) {
    destination.value = Number(destId)
    const hotels = await getHotelsByDestination(Number(destId))
    if (hotelId) {
      selectedHotel.value = hotels.find((h: any) => String(h.id) === String(hotelId)) || null
    }
  }
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
        destination: destination.value,
        total_price: Math.round(Number(totalPrice.value))
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
      selectedHotel.value = null
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
            <label class="block text-gray-600 mb-1 font-medium">Целосно ime</label>
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
            <input
                :value="persons"
                @input="persons = Number(($event.target as HTMLInputElement).value)"
                type="number" min="1"
                class="w-full border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-orange-400"
            />
          </div>
          <div>
            <label class="block text-gray-600 mb-1 font-medium">Датум од</label>
            <input v-model="travel_date" type="date"
                   class="w-full border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-orange-400" />
          </div>
          <div>
            <label class="block text-gray-600 mb-1 font-medium">Датум до</label>
            <input v-model="return_date" type="date"
                   class="w-full border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-orange-400" />
          </div>
          <div class="md:col-span-2">
            <label class="block text-gray-600 mb-1 font-medium">Дестинација</label>
            <select v-model="destination"
                    class="w-full border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-orange-400">
              <option value="">-- Избери дестинација --</option>
              <option v-for="dest in destinations" :key="dest.id" :value="dest.id">
                {{ dest.name }}
              </option>
            </select>
          </div>
        </div>

        <div v-if="selectedHotel && nights > 0" class="mt-6 bg-orange-50 rounded-2xl p-6 border border-orange-100">
          <h3 class="text-lg font-bold text-gray-800 mb-4">Вкупно</h3>
          <div class="flex justify-between text-gray-600 mb-2">
            <span>Хотел</span>
            <span class="font-medium">{{ selectedHotel.name }}</span>
          </div>
          <div class="flex justify-between text-gray-600 mb-2">
            <span>Цена по ноќ</span>
            <span class="font-medium">€{{ selectedHotel.price_per_night }}</span>
          </div>
          <div class="flex justify-between text-gray-600 mb-2">
            <span>Ноќи</span>
            <span class="font-medium">{{ nights }}</span>
          </div>
          <div class="flex justify-between text-gray-600 mb-2">
            <span>Лица</span>
            <span class="font-medium">{{ persons }}</span>
          </div>
          <div class="border-t border-orange-200 mt-3 pt-3 flex justify-between text-xl font-bold text-orange-500">
            <span>Вкупно</span>
            <span>€{{ totalPrice }}</span>
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
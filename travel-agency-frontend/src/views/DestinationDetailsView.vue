<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getDestinations } from '../api/destinations'
import { getHotelsByDestination } from '../api/destinations'

const route = useRoute()
const router = useRouter()

const destination = ref<any>(null)
const hotels = ref<any[]>([])
const loading = ref(true)
const error = ref('')
const sortOrder = ref('none')

const sortedHotels = computed(() => {
  if (sortOrder.value === 'asc') {
    return [...hotels.value].sort((a, b) => parseFloat(a.price_per_night) - parseFloat(b.price_per_night))
  } else if (sortOrder.value === 'desc') {
    return [...hotels.value].sort((a, b) => parseFloat(b.price_per_night) - parseFloat(a.price_per_night))
  }
  return hotels.value
})

onMounted(async () => {
  try {
    const destinations = await getDestinations()
    destination.value = destinations.find((d: any) => String(d.id) === String(route.params.id))

    if (!destination.value) {
      error.value = 'Дестинацијата не е пронајдена.'
    } else {
      hotels.value = await getHotelsByDestination(destination.value.id)
    }
  } catch {
    error.value = 'Грешка при вчитување на дестинацијата.'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="bg-gray-50 min-h-screen">
    <div v-if="loading" class="py-24 text-center text-xl text-gray-500">
      Се вчитува...
    </div>

    <div v-else-if="error" class="py-24 text-center text-xl text-red-500">
      {{ error }}
    </div>

    <div v-else>
      <!-- Hero -->
      <div
          class="relative h-[420px] flex items-center justify-center text-white"
          :style="`background-image: url('${destination.image}'); background-size: cover; background-position: center;`"
      >
        <div class="absolute inset-0 bg-black/50"></div>
        <div class="relative z-10 text-center px-6">
          <p class="text-orange-400 font-semibold uppercase tracking-wider mb-2">{{ destination.country }}</p>
          <h1 class="text-5xl font-bold mb-4">{{ destination.name }}</h1>
        </div>
      </div>

      <!-- Info -->
      <div class="max-w-6xl mx-auto px-6 py-16">
        <div class="bg-white rounded-3xl shadow p-8 text-center">
          <h2 class="text-3xl font-bold mb-4 text-gray-800">За дестинацијата</h2>
          <p class="text-gray-600 leading-8 text-lg max-w-3xl mx-auto">{{ destination.description }}</p>

          <div class="grid grid-cols-3 gap-4 mt-8 max-w-xl mx-auto">
            <div class="bg-gray-50 rounded-2xl p-4 text-center">
              <div class="text-3xl mb-2">🌍</div>
              <p class="text-gray-500 text-sm">Држава</p>
              <p class="font-bold">{{ destination.country }}</p>
            </div>
            <div class="bg-gray-50 rounded-2xl p-4 text-center">
              <div class="text-3xl mb-2">✈️</div>
              <p class="text-gray-500 text-sm">Патување</p>
              <p class="font-bold">Авион</p>
            </div>
            <div class="bg-gray-50 rounded-2xl p-4 text-center">
              <div class="text-3xl mb-2">🏨</div>
              <p class="text-gray-500 text-sm">Хотел</p>
              <p class="font-bold">Вклучен</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Hotels -->
      <div class="max-w-3xl mx-auto px-6 pb-16">
        <div class="text-center mb-6">
          <p class="text-orange-500 font-semibold uppercase tracking-wider mb-2">Сместување</p>
          <h2 class="text-4xl font-bold text-gray-800">Хотели во {{ destination.city }} - {{ destination.country }}</h2>
        </div>

        <!-- Sort -->
        <div class="flex gap-3 justify-center mb-8">
          <button
              @click="sortOrder = 'asc'"
              :class="sortOrder === 'asc' ? 'bg-orange-500 text-white' : 'bg-white text-gray-600 border'"
              class="px-5 py-2 rounded-full font-medium transition text-sm"
          >
            Цена ↑
          </button>
          <button
              @click="sortOrder = 'desc'"
              :class="sortOrder === 'desc' ? 'bg-orange-500 text-white' : 'bg-white text-gray-600 border'"
              class="px-5 py-2 rounded-full font-medium transition text-sm"
          >
            Цена ↓
          </button>
        </div>

        <div v-if="hotels.length === 0" class="text-center text-gray-400 text-xl py-10">
          Нема достапни хотели.
        </div>

        <div v-else class="flex flex-col gap-4">
          <div
              v-for="hotel in sortedHotels"
              :key="hotel.id"
              class="bg-white rounded-2xl shadow-md overflow-hidden flex flex-row"
          >
            <img :src="hotel.image" class="w-48 h-40 object-cover flex-shrink-0" />
            <div class="p-5 flex flex-col justify-between flex-1">
              <div>
                <div class="flex items-center justify-between mb-1">
                  <h3 class="text-lg font-bold text-gray-800">{{ hotel.name }}</h3>
                  <span class="text-yellow-500 text-sm">{{ '★'.repeat(hotel.stars) }}</span>
                </div>
                <div class="flex items-center justify-between text-sm text-gray-500 mt-1">
                  <span>⭐ {{ hotel.rating }}/10</span>
                  <span class="text-orange-500 font-bold text-base">€{{ hotel.price_per_night }}<span class="text-gray-400 font-normal text-xs"> / ноќ</span></span>
                </div>
              </div>
              <button
                  @click="router.push(`/bookings?destinationId=${destination.id}&hotelId=${hotel.id}`)"
                  class="mt-3 bg-orange-500 hover:bg-orange-600 text-white font-bold py-2 rounded-full transition text-sm"
              >
                Резервирај →
              </button>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>
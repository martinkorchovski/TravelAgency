<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { getDestinations } from '../api/destinations'
import { useRouter } from 'vue-router'


const destinations = ref<any[]>([])
const search = ref('')
const selectedCountry = ref('all')
const selectedPrice = ref('all')

const filteredDestinations = computed(() => {
  return destinations.value.filter((dest) => {
    const matchesSearch =
      dest.name.toLowerCase().includes(search.value.toLowerCase()) ||
      dest.country.toLowerCase().includes(search.value.toLowerCase())

    const matchesCountry =
      selectedCountry.value === 'all' || dest.country === selectedCountry.value

    const matchesPrice =
      selectedPrice.value === 'all' ||
      (selectedPrice.value === 'under300' && dest.price <= 300) ||
      (selectedPrice.value === '300to600' && dest.price > 300 && dest.price <= 600) ||
      (selectedPrice.value === 'over600' && dest.price > 600)

    return matchesSearch && matchesCountry && matchesPrice
  })
})
const router = useRouter()

onMounted(async () => {
  destinations.value = await getDestinations()
})
const countries = computed(() => {
  return [...new Set(destinations.value.map((dest) => dest.country))]
})
</script>
  
<template>
  <div class="bg-gray-50">
    <!-- Hero -->
    <div class="relative h-64 flex items-center justify-center text-white"
      style="background-image: url('https://images.unsplash.com/photo-1488085061387-422e29b40080?w=1600'); background-size: cover; background-position: center;">
      <div class="absolute inset-0 bg-black/50"></div>
      <div class="relative z-10 text-center">
        <p class="text-orange-400 font-semibold uppercase tracking-wider mb-2">Пребарај</p>
        <h1 class="text-5xl font-bold">Сите дестинации</h1>
      </div>
    </div>
    <!-- Filter Box -->
<div class="relative z-20 max-w-6xl mx-auto px-6 -mt-10">
  <div class="bg-white rounded-3xl shadow-xl p-6 grid grid-cols-1 md:grid-cols-4 gap-4">
    <input
      v-model="search"
      type="text"
      placeholder="Пребарај дестинација..."
      class="border rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-orange-500"
    />

    <select
      v-model="selectedCountry"
      class="border rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-orange-500"
    >
     <option value="all">Сите држави</option>
<option
  v-for="country in countries"
  :key="country"
  :value="country"
>
  {{ country }}
</option>
    </select>

    <select
      v-model="selectedPrice"
      class="border rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-orange-500"
    >
      <option value="all">Сите цени</option>
      <option value="under300">До 300€</option>
      <option value="300to600">300€ - 600€</option>
      <option value="over600">Над 600€</option>
    </select>

    <button
      @click="search = ''; selectedCountry = 'all'; selectedPrice = 'all'"
      class="bg-orange-500 hover:bg-orange-600 text-white font-bold rounded-xl px-6 py-3"
    >
      Ресетирај
    </button>
  </div>
</div>

    <!-- Destinations Grid -->
  <div class="max-w-6xl mx-auto px-6 pt-20 pb-16">
      <div v-if="filteredDestinations.length === 0" class="text-center text-gray-400 text-xl py-20">
        Нема дестинации се уште.
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div
         v-for="dest in filteredDestinations"
          :key="dest.id"
         class="rounded-2xl shadow-md overflow-hidden hover:shadow-xl transition cursor-pointer group"
         @click="router.push(`/destinations/${dest.id}`)"
        >
          <div class="relative overflow-hidden h-52">
            <img :src="dest.image" class="w-full h-full object-cover group-hover:scale-105 transition duration-300" />
            <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/70 to-transparent p-4">
              <h3 class="text-white text-xl font-bold">{{ dest.name }}</h3>
              <p class="text-white/80 text-sm">{{ dest.country }}</p>
            </div>
          </div>
          <div class="p-4 flex items-center justify-between bg-white">
            <p class="text-gray-500 text-sm line-clamp-2 flex-1">{{ dest.description }}</p>
            <div class="text-right shrink-0 ml-4">
              <p class="text-gray-400 text-xs">по лице</p>
              <p class="text-orange-500 font-bold text-xl">€{{ dest.price }}</p>
            </div>
          </div>
          <div class="px-4 pb-4 bg-white">
           <button
  @click.stop="router.push(`/bookings?destinationId=${dest.id}`)"
  class="w-full bg-orange-500 hover:bg-orange-600 text-white font-bold py-2 rounded-full transition"
>
  Резервирај →
</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { getDestinations } from '../api/destinations'
import { useRouter, useRoute } from 'vue-router'

const destinations = ref([] as any[])
const search = ref('')
const selectedCountry = ref('all')
const router = useRouter()
const route = useRoute()

const applyFilters = (list: any[]) => {
  return list.filter((dest) => {
    const matchesSearch =
        dest.name.toLowerCase().includes(search.value.toLowerCase()) ||
        dest.country.toLowerCase().includes(search.value.toLowerCase())
    const matchesCountry =
        selectedCountry.value === 'all' || dest.country === selectedCountry.value
    return matchesSearch && matchesCountry
  })
}

const filteredFeatured = computed(() =>
    applyFilters(destinations.value.filter(d => d.is_featured))
)

const filteredRegular = computed(() =>
    applyFilters(destinations.value.filter(d => !d.is_featured))
)

const countries = computed(() => [
  ...new Set(destinations.value.map((dest) => dest.country))
])

onMounted(async () => {
  destinations.value = await getDestinations()

  const countryQuery = route.query.country as string
  if (countryQuery) {
    const match = destinations.value.find(
        d => d.country.toLowerCase() === countryQuery.toLowerCase()
    )
    if (match) {
      selectedCountry.value = match.country
    } else {
      search.value = countryQuery
    }
  }
})
</script>

<template>
  <div class="bg-gray-50">

    <div
        class="relative h-64 flex items-center justify-center text-white"
        style="background-image: url('https://images.unsplash.com/photo-1488085061387-422e29b40080?w=1600'); background-size: cover; background-position: center;"
    >
      <div class="absolute inset-0 bg-black/50"></div>
      <div class="relative z-10 text-center">
        <p class="text-orange-400 font-semibold uppercase tracking-wider mb-2">Пребарај</p>
        <h1 class="text-5xl font-bold">Сите дестинации</h1>
      </div>
    </div>

    <div class="relative z-20 max-w-6xl mx-auto px-6 -mt-10">
      <div class="bg-white rounded-3xl shadow-xl p-6 grid grid-cols-1 md:grid-cols-2 gap-4">
        <select
            v-model="selectedCountry"
            class="border rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-orange-500"
        >
          <option value="all">Сите држави</option>
          <option v-for="country in countries" :key="country" :value="country">
            {{ country }}
          </option>
        </select>
        <button
            @click="search = ''; selectedCountry = 'all'"
            class="bg-orange-500 hover:bg-orange-600 text-white font-bold rounded-xl px-6 py-3"
        >
          Ресетирај
        </button>
      </div>
    </div>

    <div class="max-w-6xl mx-auto px-6 pt-20 pb-16 space-y-16">

      <div v-if="filteredFeatured.length > 0">
        <div class="text-center mb-10">
          <p class="text-orange-500 font-semibold uppercase tracking-wider mb-2">Специјални понуди</p>
          <h2 class="text-4xl font-bold text-gray-800">Пакет аранжмани</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div
              v-for="dest in filteredFeatured"
              :key="dest.id"
              class="rounded-2xl shadow-md overflow-hidden hover:shadow-xl transition cursor-pointer group"
              @click="router.push(`/destinations/${dest.id}`)"
          >
            <div class="relative overflow-hidden h-52">
              <img :src="dest.image" class="w-full h-full object-cover group-hover:scale-105 transition duration-300" />
              <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/70 to-transparent p-4">
                <h3 class="text-white text-xl font-bold">{{ dest.name }}</h3>
              </div>
            </div>
            <div class="p-4 flex items-center justify-between bg-white">
              <div>
                <p class="text-gray-400 text-xs">Држава</p>
                <p class="text-gray-800 font-bold text-lg">{{ dest.country }}</p>
              </div>
              <button
                  @click.stop="router.push(`/destinations/${dest.id}`)"
                  class="bg-orange-500 hover:bg-orange-600 text-white font-bold px-5 py-2 rounded-full transition"
              >
                Детали
              </button>
            </div>
          </div>
        </div>
      </div>

      <div>
        <div class="text-center mb-10">
          <p class="text-orange-500 font-semibold uppercase tracking-wider mb-2">Дестинации</p>
          <h2 class="text-4xl font-bold text-gray-800">Каде сакате да патувате?</h2>
        </div>

        <div v-if="filteredRegular.length === 0 && filteredFeatured.length === 0" class="text-center text-gray-400 text-xl py-20">
          Нема дестинации.
        </div>

        <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div
              v-for="dest in filteredRegular"
              :key="dest.id"
              class="rounded-2xl shadow-md overflow-hidden hover:shadow-xl transition cursor-pointer group"
              @click="router.push(`/destinations/${dest.id}`)"
          >
            <div class="relative overflow-hidden h-52">
              <img :src="dest.image" class="w-full h-full object-cover group-hover:scale-105 transition duration-300" />
              <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/70 to-transparent p-4">
                <h3 class="text-white text-xl font-bold">{{ dest.name }}</h3>
              </div>
            </div>
            <div class="p-4 flex items-center justify-between bg-white">
              <div>
                <p class="text-gray-400 text-xs">Држава</p>
                <p class="text-gray-800 font-bold text-lg">{{ dest.country }}</p>
              </div>
              <button
                  @click.stop="router.push(`/destinations/${dest.id}`)"
                  class="bg-orange-500 hover:bg-orange-600 text-white font-bold px-5 py-2 rounded-full transition"
              >
                Детали
              </button>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>
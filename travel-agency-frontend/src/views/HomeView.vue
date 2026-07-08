<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { getDestinations } from '../api/destinations'
import { useRouter } from 'vue-router'

const destinations = ref([] as any[])
const router = useRouter()
const searchCountry = ref('')

const specialOffers = computed(() => destinations.value.filter(d => d.is_featured).slice(0, 3))
const regularDestinations = computed(() => destinations.value.filter(d => !d.is_featured).slice(0, 6))

const countries = computed(() => [
  ...new Set(destinations.value.map(d => d.country))
])

onMounted(async () => {
  destinations.value = await getDestinations()
})

function handleSearch() {
  router.push({
    path: '/destinations',
    query: {
      country: searchCountry.value || undefined,
    }
  })
}
</script>

<template>
  <div>

    <div
        class="relative h-[550px] flex items-center justify-center text-white"
        style="background-image: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1600'); background-size: cover; background-position: center;"
    >
      <div class="absolute inset-0 bg-black/50"></div>
      <div class="relative z-10 text-center px-6">
        <h1 class="text-5xl font-bold mb-4 drop-shadow-lg">Откријте го светот со нас</h1>
        <p class="text-xl mb-8 drop-shadow">Најдобри дестинации, најдобри цени — резервирај онлајн</p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <RouterLink
              to="/destinations"
              class="bg-orange-500 hover:bg-orange-600 text-white font-bold px-10 py-4 rounded-full text-lg transition"
          >
            Погледни дестинации
          </RouterLink>
          <RouterLink
              to="/bookings"
              class="bg-white/10 hover:bg-white/20 border-2 border-white text-white font-bold px-10 py-4 rounded-full text-lg backdrop-blur-sm transition hover:scale-105"
          >
            Резервирај сега
          </RouterLink>
        </div>
      </div>
    </div>

    <div class="relative z-20 max-w-6xl mx-auto px-6 -mt-16">
      <div class="bg-white rounded-3xl shadow-xl p-6 grid grid-cols-1 md:grid-cols-2 gap-4">
        <select
            v-model="searchCountry"
            class="border rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-orange-500"
        >
          <option value="">Сите држави</option>
          <option v-for="country in countries" :key="country" :value="country">
            {{ country }}
          </option>
        </select>
        <button
            @click="handleSearch"
            class="bg-orange-500 hover:bg-orange-600 text-white font-bold rounded-xl px-6 py-3"
        >
          Барај
        </button>
      </div>
    </div>

    <div class="max-w-6xl mx-auto px-6 py-14">
      <div class="text-center mb-10">
        <p class="text-orange-500 font-semibold uppercase tracking-wider mb-2">Категории</p>
        <h2 class="text-4xl font-bold text-gray-800">Избери тип на патување</h2>
      </div>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-5">
        <div class="bg-white rounded-2xl shadow p-6 text-center hover:shadow-xl transition cursor-pointer">
          <div class="text-4xl mb-3">☀️</div>
          <h3 class="font-bold text-gray-800">Лето 2026</h3>
        </div>
        <div class="bg-white rounded-2xl shadow p-6 text-center hover:shadow-xl transition cursor-pointer">
          <div class="text-4xl mb-3">✈️</div>
          <h3 class="font-bold text-gray-800">Авионски аранжмани</h3>
        </div>
        <div class="bg-white rounded-2xl shadow p-6 text-center hover:shadow-xl transition cursor-pointer">
          <div class="text-4xl mb-3">🚌</div>
          <h3 class="font-bold text-gray-800">Автобуски аранжмани</h3>
        </div>
        <div class="bg-white rounded-2xl shadow p-6 text-center hover:shadow-xl transition cursor-pointer">
          <div class="text-4xl mb-3">🔥</div>
          <h3 class="font-bold text-gray-800">Last Minute</h3>
        </div>
      </div>
    </div>

    <div class="bg-gray-50 pt-24 pb-10 border-b">
      <div class="max-w-5xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
        <div>
          <div class="text-3xl font-bold text-orange-500">25.000+</div>
          <div class="text-gray-500 mt-1">Патници годишно</div>
        </div>
        <div>
          <div class="text-3xl font-bold text-orange-500">20+</div>
          <div class="text-gray-500 mt-1">Години искуство</div>
        </div>
        <div>
          <div class="text-3xl font-bold text-orange-500">50+</div>
          <div class="text-gray-500 mt-1">Дестинации</div>
        </div>
        <div>
          <div class="text-3xl font-bold text-orange-500">7/7</div>
          <div class="text-gray-500 mt-1">Чартер летови</div>
        </div>
      </div>
    </div>

    <div class="bg-gray-50 py-16 px-6">
      <div class="max-w-6xl mx-auto">
        <div class="text-center mb-10">
          <p class="text-orange-500 font-semibold uppercase tracking-wider mb-2">
            Специјални понуди
          </p>
          <h2 class="text-4xl font-bold text-gray-800">Пакет аранжмани</h2>
        </div>

        <div
            v-if="specialOffers.length === 0"
            class="text-center text-gray-400 text-xl"
        >
          Нема понуди се уште.
        </div>

        <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div
              v-for="(dest, index) in specialOffers"
              :key="dest.id"
              class="bg-white rounded-2xl shadow-md overflow-hidden hover:shadow-xl transition duration-300 cursor-pointer group"
              @click="router.push(`/destinations/${dest.id}`)"
          >
            <div class="relative overflow-hidden h-56">
              <img
                  :src="dest.image"
                  class="w-full h-full object-cover group-hover:scale-105 transition duration-300"
              />

              <span
                  class="absolute top-4 left-4 text-white text-sm font-bold px-3 py-1 rounded-full"
                  :class="index === 0 ? 'bg-red-500' : index === 1 ? 'bg-orange-500' : 'bg-green-500'"
              >
            {{ index === 0 ? '-20%' : index === 1 ? 'Last Minute' : 'Early Booking' }}
          </span>

              <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-transparent"></div>

              <div class="absolute bottom-4 left-4">
                <h3 class="text-white text-2xl font-bold">
                  {{ dest.name }}
                </h3>
              </div>
            </div>

            <div class="p-4 flex items-center justify-between">
              <div>
                <p class="text-gray-400 text-xs">Држава</p>
                <p class="text-gray-900 font-bold text-lg">
                  {{ dest.country }}
                </p>
              </div>

              <button
                  @click.stop="router.push(`/destinations/${dest.id}`)"
                  class="bg-orange-500 hover:bg-orange-600 text-white px-5 py-2 rounded-full font-bold transition"
              >
                Детали
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="max-w-6xl mx-auto px-6 py-16">
      <div class="text-center mb-10">
        <p class="text-orange-500 font-semibold uppercase tracking-wider mb-2">
          Дестинации
        </p>
        <h2 class="text-4xl font-bold">Каде сакате да патувате?</h2>
      </div>

      <div
          v-if="regularDestinations.length === 0"
          class="text-center text-gray-400 text-xl"
      >
        Нема дестинации се уште.
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div
            v-for="dest in regularDestinations"
            :key="dest.id"
            class="bg-white rounded-2xl shadow-md overflow-hidden hover:shadow-xl hover:-translate-y-1 transition duration-300 cursor-pointer group"
            @click="router.push(`/destinations/${dest.id}`)"
        >
          <div class="relative overflow-hidden h-56">
            <img
                :src="dest.image"
                class="w-full h-full object-cover group-hover:scale-105 transition duration-300"
            />

            <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-transparent"></div>

            <div class="absolute bottom-4 left-4">
              <h3 class="text-white text-2xl font-bold">
                {{ dest.name }}
              </h3>
            </div>
          </div>

          <div class="p-4 flex items-center justify-between bg-white">
            <div>
              <p class="text-gray-400 text-xs">Држава</p>
              <p class="text-gray-900 font-bold text-lg">
                {{ dest.country }}
              </p>
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

      <div class="text-center mt-8">
        <RouterLink
            to="/destinations"
            class="border-2 border-orange-500 text-orange-500 hover:bg-orange-500 hover:text-white font-bold px-8 py-3 rounded-full transition"
        >
          Погледни ги сите →
        </RouterLink>
      </div>
    </div>

    <div class="bg-gray-50 py-16 px-6">
      <div class="max-w-5xl mx-auto text-center mb-10">
        <p class="text-orange-500 font-semibold uppercase tracking-wider mb-2">Зошто ние?</p>
        <h2 class="text-4xl font-bold">Вашиот одмор е наш приоритет</h2>
      </div>
      <div class="max-w-5xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white rounded-2xl p-6 shadow text-center">
          <div class="text-5xl mb-4">✈️</div>
          <h3 class="font-bold text-xl mb-2">Директни летови</h3>
          <p class="text-gray-500">Чартер летови секој ден во неделата од Скопје</p>
        </div>
        <div class="bg-white rounded-2xl p-6 shadow text-center">
          <div class="text-5xl mb-4">💰</div>
          <h3 class="font-bold text-xl mb-2">Најдобри цени</h3>
          <p class="text-gray-500">Early booking попусти и ексклузивни понуди</p>
        </div>
        <div class="bg-white rounded-2xl p-6 shadow text-center">
          <div class="text-5xl mb-4">🎧</div>
          <h3 class="font-bold text-xl mb-2">24/7 Поддршка</h3>
          <p class="text-gray-500">Директен контакт со агент за продажба</p>
        </div>
      </div>
    </div>

    <div class="bg-orange-500 py-16 px-6 text-white text-center">
      <h2 class="text-4xl font-bold mb-4">Подготвен за следната авантура?</h2>
      <p class="mb-8 text-lg">Изберија твојата следна дестинација и резервирај онлајн.</p>
      <RouterLink
          to="/destinations"
          class="bg-white text-orange-500 font-bold px-8 py-4 rounded-full hover:bg-orange-50 transition"
      >
        Погледни дестинации →
      </RouterLink>
    </div>

  </div>
</template>
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getDestinations } from '../api/destinations'

const route = useRoute()
const router = useRouter()

const destination = ref<any>(null)
const loading = ref(true)
const error = ref('')

onMounted(async () => {
  try {
    const destinations = await getDestinations()
    destination.value = destinations.find((d: any) => String(d.id) === String(route.params.id))

    if (!destination.value) {
      error.value = 'Дестинацијата не е пронајдена.'
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
      <div
        class="relative h-[420px] flex items-center justify-center text-white"
        :style="`background-image: url('${destination.image}'); background-size: cover; background-position: center;`"
      >
        <div class="absolute inset-0 bg-black/50"></div>

        <div class="relative z-10 text-center px-6">
          <p class="text-orange-400 font-semibold uppercase tracking-wider mb-2">
            {{ destination.country }}
          </p>
          <h1 class="text-5xl font-bold mb-4">
            {{ destination.name }}
          </h1>
          <p class="text-xl text-white/90">
            Од €{{ destination.price }} по лице
          </p>
        </div>
      </div>

      <div class="max-w-6xl mx-auto px-6 py-16 grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="md:col-span-2 bg-white rounded-3xl shadow p-8">
          <h2 class="text-3xl font-bold mb-4 text-gray-800">
            За дестинацијата
          </h2>

    <p class="text-gray-600 leading-8 text-lg">
  {{ destination.description }}
</p>

          <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mt-8">
            <div class="bg-gray-50 rounded-2xl p-4 text-center">
              <div class="text-3xl mb-2">🌍</div>
              <p class="text-gray-500 text-sm">Држава</p>
              <p class="font-bold">{{ destination.country }}</p>
            </div>

            <div class="bg-gray-50 rounded-2xl p-4 text-center">
              <div class="text-3xl mb-2">💶</div>
              <p class="text-gray-500 text-sm">Цена</p>
              <p class="font-bold">€{{ destination.price }}</p>
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

        <div class="bg-white rounded-3xl shadow p-8 h-fit">
          <p class="text-orange-500 font-semibold uppercase mb-2">
            Резервација
          </p>

          <h3 class="text-2xl font-bold mb-4">
            Резервирај патување
          </h3>

          <p class="text-gray-500 mb-6">
            Направи онлајн резервација за оваа дестинација.
          </p>

          <div class="border-t border-b py-4 mb-6">
            <div class="flex justify-between mb-2">
              <span class="text-gray-500">Цена по лице</span>
              <span class="font-bold">€{{ destination.price }}</span>
            </div>

            <div class="flex justify-between">
              <span class="text-gray-500">Статус</span>
              <span class="text-green-600 font-bold">Достапно</span>
            </div>
          </div>

          <button
            @click="router.push(`/bookings?destinationId=${destination.id}`)"
            class="w-full bg-orange-500 hover:bg-orange-600 text-white font-bold py-4 rounded-full transition"
          >
            Резервирај сега →
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
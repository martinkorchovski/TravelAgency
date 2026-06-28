<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { getMyBookings } from '../api/bookings'
import { cancelBooking } from '../api/bookings'
const router = useRouter()
const auth = useAuthStore()

const bookings = ref<any[]>([])
const error = ref('')
const loading = ref(true)
const showModal = ref(false)
const pendingCancelId = ref<number | null>(null)

onMounted(async () => {
  if (!auth.isLoggedIn()) {
    router.push('/login')
    return
  }

  try {
   bookings.value = await getMyBookings(auth.token)
  } catch {
    error.value = 'Не може да се вчитаат резервациите.'
  } finally {
    loading.value = false
  }
})

async function cancelReservation(id: number) {
  try {
    await cancelBooking(id, auth.token)
    bookings.value = bookings.value.map((booking) =>
      booking.id === id ? { ...booking, status: 'cancelled' } : booking
    )
  } catch {
    alert('Грешка при откажување.')
  }
}

function confirmCancel(id: number) {
  pendingCancelId.value = id
  showModal.value = true
}

function handleConfirm() {
  if (pendingCancelId.value !== null) {
    cancelReservation(pendingCancelId.value)
  }
  showModal.value = false
  pendingCancelId.value = null
}

function handleClose() {
  showModal.value = false
  pendingCancelId.value = null
}
</script>

<template>
  <div class="bg-gray-50 min-h-screen">
    <div
      class="relative h-64 flex items-center justify-center text-white"
      style="background-image: url('https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=1600'); background-size: cover; background-position: center;"
    >
      <div class="absolute inset-0 bg-black/50"></div>
      <div class="relative z-10 text-center">
        <p class="text-orange-400 font-semibold uppercase tracking-wider mb-2">Мој профил</p>
        <h1 class="text-5xl font-bold">Мои резервации</h1>
      </div>
    </div>

    <div class="max-w-6xl mx-auto px-6 py-16">
      <div v-if="loading" class="text-center text-gray-500 text-xl">
        Се вчитува...
      </div>

      <div v-if="error" class="bg-red-100 text-red-600 p-4 rounded-xl mb-6 text-center">
        {{ error }}
      </div>

      <div v-if="!loading && bookings.length === 0 && !error" class="text-center text-gray-400 text-xl">
        Немате направено резервации.
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div
          v-for="booking in bookings"
          :key="booking.id"
          class="bg-white rounded-2xl shadow-md p-6 hover:shadow-xl transition"
        >
          <div class="text-4xl mb-4">✈️</div>

          <h2 class="text-lg font-semibold text-orange-500 mb-1">{{ booking.destination_name }}</h2>
          <h3 class="text-xl font-bold text-gray-800 mb-2">
            {{ booking.full_name }}
          </h3>

          <p class="text-gray-500 mb-1">
            <strong>Е-маил:</strong> {{ booking.email }}
          </p>

          <p class="text-gray-500 mb-1">
            <strong>Телефон:</strong> {{ booking.phone }}
          </p>

          <p class="text-gray-500 mb-1">
            <strong>Лица:</strong> {{ booking.persons }}
          </p>

          <p class="text-gray-500 mb-1">
            <strong>Патување:</strong> {{ booking.travel_date }}
          </p>

          <p class="text-gray-500 mb-4">
            <strong>Враќање:</strong> {{ booking.return_date }}
          </p>

          <p class="text-gray-500 mb-1">
            <strong>Вкупна цена:</strong>
            <span class="text-orange-500 font-bold">€{{ booking.total_price }}</span>
          </p>

          <div class="mt-4">
            <span
              v-if="booking.status === 'pending'"
              class="bg-yellow-100 text-yellow-600 px-4 py-2 rounded-full font-bold text-sm"
            >
              На чекање
            </span>

            <span
              v-else-if="booking.status === 'confirmed'"
              class="bg-green-100 text-green-600 px-4 py-2 rounded-full font-bold text-sm"
            >
              Потврдено
            </span>

            <span
              v-else
              class="bg-red-100 text-red-600 px-4 py-2 rounded-full font-bold text-sm"
            >
              Откажано
            </span>
          </div>

          <button
            v-if="booking.status !== 'cancelled'"
            @click="confirmCancel(booking.id)"
            class="mt-4 w-full bg-red-500 hover:bg-red-600 text-white py-2 rounded-xl"
          >
            Откажи резервација
          </button>
        </div>
      </div>
    </div>

    <!-- Confirmation Modal -->
    <div
      v-if="showModal"
      class="fixed inset-0 bg-black/50 flex items-center justify-center z-50"
      @click.self="handleClose"
    >
      <div class="bg-white rounded-2xl shadow-xl p-8 max-w-sm w-full mx-4 text-center">
        <div class="text-5xl mb-4">⚠️</div>
        <h2 class="text-xl font-bold text-gray-800 mb-2">Откажи резервација</h2>
        <p class="text-gray-500 mb-6">Дали сте сигурни дека сакате да ја откажете оваа резервација?</p>
        <div class="flex gap-3">
          <button
            @click="handleConfirm"
            class="flex-1 bg-red-500 hover:bg-red-600 text-white py-2 rounded-xl transition"
          >
            Да, откажи
          </button>
          <button
            @click="handleClose"
            class="flex-1 border border-gray-300 text-gray-600 py-2 rounded-xl hover:bg-gray-50 transition"
          >
            Не
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<template>
  <footer class="bg-gray-900 text-white mt-16 py-10 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8">
      
      <div>
        <h2 class="text-2xl font-bold text-orange-500 mb-3">✈️ TravelAgency</h2>
        <p class="text-gray-400"> Најдобрите дестинации, најдобрите цени. Резервирај го патувањето од твоите соништа уште денес.</p>
      </div>

      <div>
        <h3 class="text-lg font-bold mb-3">Брзи линкови</h3>
        <ul class="flex flex-col gap-2 text-gray-400">
          <li><RouterLink to="/" class="hover:text-orange-400">Дома</RouterLink></li>
          <li><RouterLink to="/destinations" class="hover:text-orange-400">Дестинации</RouterLink></li>
          <li><RouterLink to="/bookings" class="hover:text-orange-400">Резервации</RouterLink></li>
          <li><RouterLink to="/contact" class="hover:text-orange-400">Контакт</RouterLink></li>
        </ul>
      </div>

      <div>
        <h3 class="text-lg font-bold mb-3">Контакт</h3>
        <ul class="flex flex-col gap-2 text-gray-400">
          <li>📞 +389 2 323 8083</li>
          <li>✉️ info@travelagency.mk</li>
          <li>📍 Скопје, Македонија</li>
        </ul>
      </div>

    </div>

    <div class="text-center text-gray-500 mt-8 border-t border-gray-700 pt-6">
      © 2026 TravelAgency. All rights reserved.
    </div>
  </footer>
</template>
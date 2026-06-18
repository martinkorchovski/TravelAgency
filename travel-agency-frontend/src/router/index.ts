import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DestinationsView from '../views/DestinationsView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import BookingView from '../views/BookingView.vue'
import ContactView from '../views/ContactView.vue'
import MyBookingsView from '../views/MyBookingsView.vue'
import DestinationDetailsView from '../views/DestinationDetailsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior() {
    return { top: 0 }
  },
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/destinations',
      name: 'destinations',
      component: DestinationsView,
    },
    {
  path: '/login',
  name: 'login',
  component: LoginView,
  },
  {
  path: '/register',
  name: 'register',
  component: RegisterView,
},  
{
  path: '/bookings',
  name: 'bookings',
  component: BookingView,
},
{
  path: '/contact',
  name: 'contact',
  component: ContactView,
},
{
  path: '/my-bookings',
  name: 'my-bookings',
  component: MyBookingsView
},
{
  path: '/destinations/:id',
  name: 'destination-details',
  component: DestinationDetailsView,
},

],
})

export default router
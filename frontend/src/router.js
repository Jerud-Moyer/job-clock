import { createMemoryHistory, createRouter, createWebHistory } from 'vue-router'
import Home from './pages/Home.vue'
import TimeClock from './pages/TimeClock.vue'
import Clients from './pages/Clients.vue'


const routes = [
  { path: '/', component: Home },
  { path: '/time-clock', component: TimeClock },
  { path: '/clients', component: Clients }
]

export default createRouter({
  history: createWebHistory(),
  routes,
})

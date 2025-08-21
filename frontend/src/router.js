import { createMemoryHistory, createRouter, createWebHistory } from 'vue-router'
import TimeClock from './pages/TimeClock.vue'
import Clients from './pages/Clients.vue'
import Jobs from './pages/Jobs.vue'


const routes = [
  { path: '/', component: TimeClock },
  { path: '/jobs', component: Jobs },
  { path: '/clients', component: Clients }
]

export default createRouter({
  history: createWebHistory(),
  routes,
})

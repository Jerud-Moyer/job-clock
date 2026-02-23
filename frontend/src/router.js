import { createMemoryHistory, createRouter, createWebHistory } from 'vue-router'
import TimeClock from './pages/TimeClock.vue'
import Clients from './pages/Clients.vue'
import Jobs from './pages/Jobs.vue'
import Sheets from './pages/Sheets.vue'

const routes = [
  { path: '/', component: TimeClock },
  { path: '/sheets', component: Sheets },
  { path: '/jobs', component: Jobs },
  { path: '/clients', component: Clients }
]

export default createRouter({
  history: createWebHistory(),
  routes,
})

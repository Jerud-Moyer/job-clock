import { createMemoryHistory, createRouter } from 'vue-router'
import Home from './pages/Home.vue'
import TimeClock from './pages/TimeClock.vue'


const routes = [
  { path: '/', component: Home },
  { path: '/time-clock', component: TimeClock },
]

export default createRouter({
  history: createMemoryHistory(),
  routes,
})

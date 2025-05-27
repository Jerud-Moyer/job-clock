import { createApp } from 'vue'
import './style.css'
import './main.css'
import App from './App.vue'
import router from './router'
import Aura from "@primeuix/themes/aura"
import PrimeVue from "primevue/config"

const app = createApp(App)
app.use(router)
app.use(PrimeVue, {
	theme: {
		preset: Aura,
		options: {
			darkModeSelector: ".p-dark",
		},
	},
})

app.mount('#app')

import { createApp } from 'vue'
import './style.css'
import './main.css'
import App from './App.vue'
import router from './router'
import PrimeVue from "primevue/config"
import primeTheme from "./theme.js"
import ToastService from 'primevue/toastservice'

const app = createApp(App)
app.use(router)
app.use(ToastService)
app.use(PrimeVue, {
	
	theme: {
		preset: primeTheme,
		options: {
			darkModeSelector: "system",
			cssLayer: {
				name: "primevue",
				order: "theme, base, primevue",
			} 
		},
	},
})

app.mount('#app')

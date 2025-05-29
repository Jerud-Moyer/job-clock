import { createApp } from 'vue'
import './style.css'
import './main.css'
import App from './App.vue'
import router from './router'
import Aura from "@primeuix/themes/aura"
import PrimeVue from "primevue/config"
import primeTheme from "../theme.js"

const app = createApp(App)
app.use(router)
app.use(PrimeVue, {
    theme: primeTheme,
    // unStyled: true
	// theme: {
	// 	preset: Aura,
	// 	options: {
	// 		darkModeSelector: ".p-dark",
	// 	},
	// },
})

app.mount('#app')

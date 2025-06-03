import { createApp } from 'vue'
import './style.css'
import './main.css'
import App from './App.vue'
import router from './router'
import Aura from "@primeuix/themes/aura"
import PrimeVue from "primevue/config"
import primeTheme from "./theme.js"
import { definePreset } from '@primeuix/themes'
import Material from '@primeuix/themes/material'
import ToastService from 'primevue/toastservice'


const themeWut = definePreset(Material, {
	components: {
		toolbar: {
			borderRadius: '0px'
		},
		button: {
			paddingX: '60px',
			primaryHoverBackground: '{cyan.700}',
		},
		tabs: {
			tabFocusRingColor: 'transparent',
			tabActiveBorderColor: 'green',
			tabBackground: 'blue',
			tabBorderWidth: '4px',
			tabBorderColor: '{slate.600}'
		}
	}
})

const app = createApp(App)
app.use(router)
app.use(ToastService)
app.use(PrimeVue, {
	
	theme: {
		preset: primeTheme,
		options: {
			darkModeSelector: "system",
			// cssLayer: {
			// 	name: "primevue",
			// 	order: "app-styles, primevue, tailwind",
			// }
		},
	},
})

app.mount('#app')

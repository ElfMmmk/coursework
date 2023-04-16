import { createApp } from 'vue'
import './assets/css/reseter.css'
import './assets/css/bootstrap-grid.min.css'
import './assets/scss/style.css'
import App from './App.vue'
import router from './router'
import store from './store'

createApp(App).use(store).use(router).mount('#app')

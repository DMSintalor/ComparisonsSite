import {createApp} from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import router from './router'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import axios from "axios"

const app = createApp(App)

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
app.config.globalProperties.$axios = axios
if (process.env.NODE_ENV === "development") {
    axios.defaults.baseURL = 'http://127.0.0.1:8000/api'
} else {
    axios.defaults.baseURL = ''
}


app.use(ElementPlus)
app.use(router)
app.mount('#app')
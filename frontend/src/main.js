import { createApp } from 'vue'
import App from './App.vue'
import Registration from "@/views/Registration.vue";
import {createRouter, createWebHashHistory} from "vue-router";

const routes = [
    {
        path: '/reg',
        component: Registration
    },
]
const router = createRouter({
    history:createWebHashHistory(),
    routes
})

createApp(App).use(router).mount('#app')

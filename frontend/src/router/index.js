import Registration from "@/views/Registration.vue";
import Home from "@/views/Home.vue";
import Login from "@/views/Login.vue";
import Logout from "@/views/Logout.vue";
import {createRouter, createWebHashHistory} from "vue-router";

const router = createRouter({
    history:createWebHashHistory(),
    routes: [
        {
            path: '/reg',
            component: Registration
        },
        {
            path: '/',
            component: Home
        },
        {
            path: '/login',
            component: Login
        },
        {
            path: '/logout',
            component: Logout
        }
    ]
})
export default router
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Log from '../views/Log.vue'
import Map from '../views/Map.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/log',
        name: 'Log',
        component: Log
    },
    {
        path: '/map',
        name: 'Map',
        component: Map
    }
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router

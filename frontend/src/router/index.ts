import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Log from '../views/Log.vue'
import Map from '../views/Map.vue'
import Graph from '../views/Graph.vue';
import Comparison from '../views/Comparison.vue'


Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Graph
    },
    {
        path: '/log',
        name: 'Log',
        component: Log
    },
    {
        path: '/map',
        name: 'Map',
        component: () => import(/* webpackChunkName: "map" */ '../views/Home.vue')
    },
    {
        path: '/comparison',
        name: 'Grafice de comparatie',
        component: () => import(/* webpackChunkName: "comparison" */ '../views/Comparison.vue')
    },
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router

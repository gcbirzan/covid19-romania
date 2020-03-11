import Vue from 'vue'
import App from './App.vue'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import {LayoutPlugin} from 'bootstrap-vue'

Vue.config.productionTip = false

Vue.use(BootstrapVue);
Vue.use(LayoutPlugin);

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import "leaflet/dist/leaflet.css";
import COVID19 from "./store";

import Vuex from "vuex";

Vue.use(Vuex);

const store = new Vuex.Store({
    modules: {
        covid19: COVID19
    }
});


new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')

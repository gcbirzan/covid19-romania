import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueSync from 'vue-sync';

Vue.config.productionTip = false

// Vue.use(BootstrapVue);
// Vue.use(LayoutPlugin);

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
// @ts-ignore
import COVID19 from './store';

import Vuex from "vuex";

Vue.use(Vuex);
Vue.use(VueSync);

const store = new Vuex.Store({
    modules: {
        covid19: COVID19
    }
});


new Vue({
    router,
    store,
    render: h => h(App),
    created: function () {

        this.$store.dispatch('fetch_data');
        this.$store.dispatch('fetch_log');
        this.$store.dispatch('fetch_chart_data');
        setInterval(() => {
            this.$store.dispatch('fetch_data');
            this.$store.dispatch('fetch_log');
            this.$store.dispatch('fetch_chart_data');
        }, 60 * 1000 );

    }
}).$mount('#app')

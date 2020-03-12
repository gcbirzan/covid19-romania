<template>
    <div id="app">
        <b-navbar toggleable="lg" type="dark" variant="info" :sticky="true">
            <b-navbar-brand to="/">Coronavirus COVID-19 Romania</b-navbar-brand>

            <b-navbar-nav>
<!--                <b-nav-item to="/map">-->
<!--                    Harta cazuri-->
<!--                </b-nav-item>-->
                <b-nav-item to="/log">
                    Schimbari cazuri confirmate
                </b-nav-item>
            </b-navbar-nav>
            <b-navbar-nav :small="true" class="ml-auto">
                <b-nav-text>Date furnizate de <a href="https://insp.gov.ro/">INSP</a>.
                    Update {{ last_update }}.
                </b-nav-text>
            </b-navbar-nav>

        </b-navbar>

        <b-container fluid>
            <b-row>
                <b-col cols="12 ">
                    <router-view></router-view>
                </b-col>
            </b-row>

        </b-container>
    </div>
</template>
<script>
    import {Component, Vue} from "vue-property-decorator";
    import {mapState} from "vuex";

    @Component({
        computed: mapState(['covid19']),
    })
    export default class App extends Vue {
        get last_update() {
            if (this.$store && this.$store.state.covid19.fetched_data) {
                const date = new Date(Math.max.apply(Math, this.$store.state.covid19.data.map(function (o) {
                    return o.EditDate
                })));
                if (date) {
                    return `${date.toLocaleDateString() } ${ date.toLocaleTimeString() }`
                }
            }
        }

    }
</script>
<style lang="scss">
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }

    #nav {
        padding: 30px;

        a {
            font-weight: bold;
            color: #2c3e50;

            &.router-link-exact-active {
                color: #42b983;
            }
        }
    }
</style>

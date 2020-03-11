<template>
    <div class="flex-container">
        <div style="height: 80vh; width: 55vw;" v-if="covid19.fetched_data">
            <l-map  :center="mapCenter" :options="mapOptions">

                <l-choropleth-layer :data="covid19.data" title-key="Judete" id-key="SIRUTA_judet"
                                    :value="value_mapping" geojson-id-key="countyCode"
                                    :geojson="geojson" :colorScale="colorScale" :extra-values="extraValues">
                    <template slot-scope="props">
                        <l-info-control :item="props.currentItem" :unit="props.unit" title="Judet"
                                        placeholder="Mouse over pentru mai multe informatii"/>
                        <l-reference-chart title="Infectii confirmate" :colorScale="colorScale" :min="props.min"
                                           :max="props.max" position="bottomright"/>
                    </template>

                </l-choropleth-layer>
            </l-map>
                <span>Total cazuri confirmate {{ sum = covid19.data.map(o => o.Cazuri_confirmate).reduce((a, c) => { return a + c }) }}.
                Ultimul update {{ last_update.toLocaleDateString() }} {{ last_update.toLocaleTimeString() }}.</span>


        </div>
        <div>
            <b-table :small="true" style="width: 40vw" hover :items="covid19.data" :fields="tableFields" sort-by="Cazuri_confirmate"
                     :sort-desc="true"></b-table>
        </div>
    </div>
</template>

<script>
    import {Component, Prop, Vue} from 'vue-property-decorator';
    import geojson from '../assets/counties.json';
    // import values from '../assets/covid_data_fixed.json';
    import {LMap, LTileLayer} from "vue2-leaflet";
    import {InfoControl, ReferenceChart, ChoroplethLayer} from 'vue-choropleth'
    import {latLng} from "leaflet";
    import {mapState} from "vuex";

    @Component({
        components: {
            LMap, LTileLayer,

            'l-info-control': InfoControl,
            'l-reference-chart': ReferenceChart,
            'l-choropleth-layer': ChoroplethLayer,

        },

        computed: mapState(['covid19']),

    })
    export default class RomaniaMap extends Vue {

        get last_update() {
            if (this.$store && this.$store.state.covid19.fetched_data)
                return new Date(Math.max.apply(Math, this.$store.state.covid19.data.map(function(o) { return o.EditDate})));
        }

        data() {
            return {
                geojson,
                mapCenter: latLng(46, 25),
                colorScale: [
                    "#e0ecf4",
                    "#9ebcda",
                    "#8856a7",
                ],
                mapOptions: {
                    attributionControl: false,
                    zoomControl: false,
                    minZoom: 7,
                    maxZoom: 7,
                    zoom: 7,

                },
                extraValues: [
                    {
                        key: "Persoane_in_carantina",
                        metric: "persoane in carantina"
                    },
                    {
                        key: "Persoane_izolate",
                        metric: "persoane izolate"
                    },
                ],

                value_mapping: {
                    key: 'Cazuri_confirmate',
                    metric: 'infectii confirmate',
                },
                // url: "http://{s}.tile.osm.org/{z}/{x}/{y}.png",
                tableFields: [
                    {
                        'key': 'Judete',
                        'label': 'Judet',
                        'sortable': false,
                    },
                    {
                        'key': 'Cazuri_confirmate',
                        'sortable': true,
                    },
                    {
                        'key': 'Persoane_in_carantina',
                        'sortable': true,
                    },
                    {
                        'key': 'Persoane_izolate',
                        'sortable': true,
                    },
                ]
            }
        }

        mounted() {
            this.$store.dispatch('fetch_data');
            setInterval(() => {
                this.$store.dispatch('fetch_data');
            }, 60000);

        }

    }
</script>

<style>
    .flex-container {
        display: flex;
    }

</style>

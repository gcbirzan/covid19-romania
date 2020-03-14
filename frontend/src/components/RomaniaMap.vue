<template>
    <div class="fixed-map" id="mapdiv">
        <l-map :center="mapCenter" :options="mapOptions" class="map-display" v-if="covid19.fetched_data" ref="map">

            <l-choropleth-layer :data="covid19.data" title-key="Judete" id-key="SIRUTA_judet"
                                :value="value_mapping" geojson-id-key="countyCode"
                                :geojson="geojson" :colorScale="colorScale" :extra-values="extraValues"
                                :key="selected">
                <template slot-scope="props">
                    <l-info-control :item="props.currentItem" :unit="props.unit" title="Judet"
                                    placeholder="Mouse over(sau click) pentru mai multe informatii"/>
                    <l-reference-chart title="Infectii confirmate" :colorScale="colorScale" :min="props.min"
                                       :max="props.max" position="topleft"/>
                </template>

            </l-choropleth-layer>
        </l-map>
        <b-form-select v-model="selected" :options="mapSelectOptions"></b-form-select>
    </div>
</template>

<script>
    import {Component, Prop, Vue, Watch} from 'vue-property-decorator';
    import geojson from '../assets/counties.json';
    import * as _ from "lodash";
    import {LMap, LTileLayer} from "vue2-leaflet";
    import {InfoControl, ReferenceChart, ChoroplethLayer} from 'vue-choropleth'
    import {latLng} from "leaflet";
    import {mapState} from "vuex";
    import {Debounce} from "lodash-decorators";

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
        resize(message, event) {
            if(this.$refs.map){
               this.$refs.map.mapObject.fitBounds([[43.6884447292, 20.2201924985], [48.2208812526, 29.62654341]])
            }
        }

        get fetched() {
            return this.$store.state.covid19.fetched_data;
        }

        @Watch('fetched')
        data_feched() {
            Vue.nextTick(this.resize)
        }
        mounted() {
            Vue.nextTick(this.resize)

        }
        created() {
            window.addEventListener('resize', this.resize);
        }

        get value_mapping() {
            const selected = this.$data.selected;
            return this.$data.all_values.filter(value => value.key === selected)[0]
        }

        get extraValues() {
            const selected = this.$data.selected;
            return this.$data.all_values.filter(value => value.key !== selected)
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
                selected: 'Cazuri_confirmate',
                mapOptions: {
                    attributionControl: false,
                    zoomControl: false,
                    zoomDelta: 0.25,
                    zoomSnap: 0.25,
                    // minZoom: 7,
                    // maxZoom: 7,
                    // fitBounds: 7,

                },
                mapSelectOptions: [
                    {value: "Cazuri_confirmate", text: "Cazuri confirmate"},
                    {value: "Persoane_in_carantina", text: "Persoane in carantina"},
                    {value: "Persoane_izolate", text: "Persoane izolate"},
                    // {value: "Persoane_vindecate", text: "Persoane vindecate"},
                    // {value: "Probe_in_asteptare", text: "Probe in asteptare"},
                    // {value: "Cazuri_infirmate", text: "Cazuri infirmate"},
                    // {value: "Persoane_decedate", text: "Persoane decedate"},
                ],
                all_values: [
                    {
                        key: "Persoane_in_carantina",
                        metric: "persoane in carantina"
                    },
                    {
                        key: "Persoane_izolate",
                        metric: "persoane izolate"
                    },
                    {
                        key: 'Cazuri_confirmate',
                        metric: 'cazuri confirmate',
                    },
                    // {
                    //     key: "Persoane_vindecate",
                    //     metric: "persoane vindecate"
                    // },
                    // {
                    //     key: 'Probe_in_asteptare',
                    //     metric: 'probe in asteptare',
                    // },
                    // {
                    //     key: 'Cazuri_infirmate',
                    //     metric: 'cazuri infirmate',
                    // },
                    // {
                    //     key: 'Persoane_decedate',
                    //     metric: 'persoane_decedate',
                    // },
                ],

                // extraValues: [
                //     {
                //         key: "Persoane_in_carantina",
                //         metric: "persoane in carantina"
                //     },
                //     {
                //         key: "Persoane_izolate",
                //         metric: "persoane izolate"
                //     },
                //     {
                //         key: "Persoane_vindecate",
                //         metric: "persoane vindecate"
                //     },
                // ],
                //
                // value_mapping: {
                //     key: 'Cazuri_confirmate',
                //     metric: 'infectii confirmate',
                // },
                // url: "http://{s}.tile.osm.org/{z}/{x}/{y}.png",
            }
        }

        // mounted() {
        //     this.$store.dispatch('fetch_data');
        //     setInterval(() => {
        //         this.$store.dispatch('fetch_data');
        //     }, 60000);
        //
        // }

    }
</script>

<style scoped>
    .fixed-map { 
        width:100%;
        height:60vh;
    }
    .fixed-map >>> .info.leaflet-control {
        margin:0.5rem;
        font-size:0.8rem; 
    }
    .fixed-map >>> .info.leaflet-control h4 { font-size:0.8rem; }

@media all and (min-width:800px){
    .fixed-map { 
        width:100%;
        height:70vh;
    }
    .fixed-map >>> .info.leaflet-control, .fixed-map >>> .info.leaflet-control h4 { font-size:1.2rem; }
}
</style>

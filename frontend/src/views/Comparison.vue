<template>
    <b-container fluid>
        <b-row>
            <b-col col md="2">
                <b-row>
                    <b-col>
                        <multiselect v-model="countries" :multiple="true" :options="options"
                                     placeholder="Pick countries"></multiselect>

                    </b-col>
                </b-row>
                <b-row>
                    <b-col>
                        <b-form-group align="left" label="Scale">
                            <b-form-radio v-model="scale" name="scale" value="linear">Linear</b-form-radio>
                            <b-form-radio v-model="scale" name="scale" value="logarithmic">Logarithmic
                            </b-form-radio>
                        </b-form-group>

                    </b-col>
                </b-row>
                <b-row>
                    <b-col>
                        <b-form-group align="left" label="Graph data">
                            <b-form-radio v-model="graph_data" name="graph_data" value="cases">Cases</b-form-radio>
                            <b-form-radio v-model="graph_data" name="graph_data" value="deaths">Deaths
                            </b-form-radio>
                        </b-form-group>

                    </b-col>
                </b-row>
                <b-row>
                    <b-col>
                        <b-form-checkbox v-model="delta" name="delta" :value="true" :unchecked-value="false">
                            Display new {{graph_data}}
                        </b-form-checkbox>
                    </b-col>
                </b-row>
                <b-row>
                    <b-col cols="6">
                        <span><label for="sync_at">Sync at </label></span>
                    </b-col>
                    <b-col>
                        <b-form-input type="number" v-model="sync_at" id="sync_at" placeholder="Sync at"></b-form-input>
                    </b-col>
                </b-row>
                <b-row>
                    <b-col>
                        <b-form-checkbox v-model="moving_average" name="moving_average" :value="true"
                                         :unchecked-value="false">
                            Moving average rates
                        </b-form-checkbox>
                    </b-col>
                </b-row>

                <b-row>
                    <b-col>
                        <b-form-group align="left" label="Rate of growth ">
                            <b-form-radio v-model="rate" name="rate" value="rate">Multiplier</b-form-radio>
                            <b-form-radio v-model="rate" name="rate" value="doubling">Doubling time
                            </b-form-radio>
                        </b-form-group>

                    </b-col>
                </b-row>

            </b-col>
            <b-col col md="10">
                <chart :options="chartOptions"></chart>
                <chart :options="chartOptionsSyncd"></chart>
            </b-col>
        </b-row>

    </b-container>
</template>

<script>
    import {Component, Vue} from 'vue-property-decorator';
    import {BCol, BContainer, BRow, BFormGroup, BFormRadio, BFormCheckbox, BFormInput} from "bootstrap-vue";

    import {Chart} from 'highcharts-vue'

    import 'bootstrap/dist/css/bootstrap.css'
    import 'bootstrap-vue/dist/bootstrap-vue.css'

    import countries from '../assets/countries.json';
    import total from '../assets/fixed_total.json';
    import {mapState} from "vuex";
    import {Multiselect} from "vue-multiselect";
    import {ma, ema, sma, wma} from 'moving-averages';

    const data = total.reduce((obj, item) => {
        // debugger;
        if (item['province'] === null) {
            obj[item['country']] = {};
            obj[item['country']]['cases'] = Object.keys(item['timeline']['cases']).map(key => {
                return {x: new Date(key).getTime(), y: item['timeline']['cases'][key]}
            }).filter(obj => {
                return obj['y'] !== 0
            });
            obj[item['country']]['cases_delta'] = Object.keys(item['timeline']['cases']).map((key, index, array) => {
                let prev_key = key;
                if (index > 0) {
                    prev_key = array[index - 1]
                }
                return {
                    x: new Date(key).getTime(),
                    y: item['timeline']['cases'][key] - item['timeline']['cases'][prev_key]
                }
            }).filter(obj => {
                return obj['y'] !== 0
            });
            obj[item['country']]['deaths'] = Object.keys(item['timeline']['deaths']).map(key => {
                return {x: new Date(key).getTime(), y: item['timeline']['deaths'][key]}
            }).filter(obj => {
                return obj['y'] !== 0
            });
            obj[item['country']]['deaths_delta'] = Object.keys(item['timeline']['deaths']).map((key, index, array) => {
                let prev_key = key;
                if (index > 0) {
                    prev_key = array[index - 1]
                }
                return {
                    x: new Date(key).getTime(),
                    y: item['timeline']['deaths'][key] - item['timeline']['deaths'][prev_key]
                }
            }).filter(obj => {
                return obj['y'] !== 0
            })

        }
        return obj
    }, {});

    @Component(
        {
            components: {BContainer, BCol, BRow, BFormGroup, BFormRadio, Chart, Multiselect, BFormCheckbox, BFormInput},
            computed: mapState(['covid19']),
            url: () => {
                return ['countries', 'scale', 'graph_data', 'delta', 'sync_at', 'rate_from', 'moving_average', 'rate'].reduce((obj, v) => {
                    obj[v] = {
                        param: v,
                        noHistory: true
                    }
                    return obj;
                }, {})
            }

        }
    )
    export default class Comparison extends Vue {
        get chartOptions() {
            const graph_title = this.graph_data.charAt(0).toUpperCase() + this.graph_data.slice(1);
            let series = this.countries.map(country => {
                return {
                    name: country,
                    data: data[country][this.graph_data],
                    type: 'line',
                    yAxis: 0,

                }
            });
            if (this.delta) {
                series = this.countries.map(country => {
                    return {
                        name: `${country} new`,
                        data: data[country][`${this.graph_data}_delta`],
                        yAxis: 1,
                        type: 'column',
                    }
                }).concat(series);
            }

            return {
                title: {
                    text: graph_title
                },
                yAxis: [
                    {
                        title: {
                            'text': graph_title
                        },
                        type: this.scale,
                    },
                    {
                        title: {'text': 'Delta'},
                        type: this.scale,
                        opposite: true,
                    },
                ],

                series: series,
                xAxis: {
                    type: 'datetime',

                },
                tooltip: {
                    xDateFormat: '%Y-%m-%d',
                    shared: true,
                },
            }

        }

        get chartOptionsSyncd() {
            const graph_title = this.graph_data.charAt(0).toUpperCase() + this.graph_data.slice(1);
            let series = this.countries.map(country => {
                let sync_data = data[country][this.graph_data].filter(x => x['y'] >= this.sync_at).map((v, idx) => {
                    return {x: idx, y: v['y']}
                });

                return {
                    name: country,
                    data: sync_data,
                    type: 'line',
                    yAxis: 0,
                    tooltip: {
                        valueDecimals: 0,

                    },


                }
            });
            let rate_series = series.map(one_series => {
                let rate_data = one_series['data'].map((v, idx, array) => {

                    if (idx > 0) {
                        let value = v['y'] / array[idx - 1]['y']
                        if (this.rate === 'doubling') {
                            if (value === 1) {
                                value = NaN
                            } else {
                                value = Math.log(2) / Math.log(value)
                            }
                        }

                        return {x: v['x'], y: value}
                    } else {
                        return {x: v['x'], y: NaN}
                    }

                });
                return {
                    name: `${one_series['name']} ${this.rate === 'rate' ? 'rate' : 'doubling time'}`,
                    data: rate_data,
                    type: 'line',
                    yAxis: 1,
                    dashStyle: 'shortdot',
                    tooltip: {
                        valueDecimals: 3,

                    },

                }

            })
            if (this.moving_average) {
                rate_series = rate_series.map(one_series => {
                    const ma_data = ema(one_series['data'].map(v => v['y'] || ''), 5)
                    return {
                        name: `${one_series['name']} moving average`,
                        data: one_series['data'].map((v, idx) => {
                            return {
                                x: v['x'], y: ma_data[idx] || v['y']
                            }
                        }),
                        type: 'line',
                        yAxis: 1,
                        dashStyle: 'shortdot',
                        tooltip: {
                            valueDecimals: 3,

                        },

                    }

                })
            }

            return {
                title: {
                    text: graph_title
                },
                yAxis: [
                    {
                        title: {
                            'text': graph_title
                        },
                        type: this.scale,
                    },
                    {
                        title: {
                            'text': 'Rate'
                        },
                        opposite: true,
                    },
                ],

                series: series.concat(rate_series),
                xAxis: {
                    // type: 'datetime',

                },
                tooltip: {
                    xDateFormat: '%Y-%m-%d',
                    shared: true,

                },
            }

        }

        scale = 'linear';
        graph_data = 'cases';
        countries = ['Italy', 'Romania'];
        delta = false;
        options = countries.map(country => country['country'])
        sync_at = 10;
        moving_average = false;
        rate = 'rate'
    }
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<style scoped lang="scss">

</style>

<template>
    <div class="flex-container" id="containerdiv" v-if="covid19.fetched_chart_data">
        <highcharts :options="options.chartOptionsNewTotal" id="new_total"></highcharts>
        <highcharts :options="options.chartOptionsICU" id="icu"></highcharts>
        <highcharts :options="options.chartOptionsCasesTests" id="cases_tests"></highcharts>
        <highcharts :options="options.chartOptionsNewCasesTests" id="new_cases_tests"></highcharts>
        <highcharts :options="options.chartOptionsTotalType" id="types"></highcharts>
        <highcharts :options="options.chartOptionsRate" id="rate"></highcharts>
        <highcharts :options="options.chartOptionsDeadConfirmed" id="dead_cases"></highcharts>

    </div>
</template>

<script>
    import {Component, Vue} from "vue-property-decorator";
    import {mapState} from "vuex";
    // import chart_data from '../assets/total.json';
    import {Chart} from 'highcharts-vue';

    @Component({
        computed: mapState(['covid19']),
        components: {'highcharts': Chart},

    })
    export default class Graph extends Vue {
        get options() {
            if (!(this.$store && this.$store.state.covid19.fetched_chart_data)) {
                return {}
            }
            const chart_data = this.$store.state.covid19.chart_data;
            return {
                chartOptionsNewTotal: {
                    title: {
                        text: 'Cazuri noi/totale'
                    },
                    yAxis: [
                        {
                            title: {'text': 'Cazuri totale'},
                            opposite: true,
                        },
                        {
                            title: {
                                text: 'Numar infectii noi'
                            },

                        }
                    ],

                    series: [
                        {
                            name: 'Cazuri noi',
                            data: chart_data['delta_cases'],
                            yAxis: 1,
                            type: 'column',

                        },
                        {
                            name: 'Cazuri totale',
                            data: chart_data['cases'],
                            yAxis: 0,
                        },
                        // {
                        //     name: 'Rata cazuri noi',
                        //     data: chart_data['ratio'].map(x => {
                        //         return {x: new Date(x[0]), y: 1 + x[1]}
                        //     }),
                        //     dashStyle: 'shortdot',
                        //     type: 'spline',
                        //
                        //     yAxis: 2,
                        // },
                    ],
                    xAxis: {
                        type: 'datetime',

                    },
                    tooltip: {
                        xDateFormat: '%Y-%m-%d',
                        shared: true
                    },


                },
                chartOptionsTotalType: {
                    title: {
                        text: 'Numar cazuri active, vindecate, decedate, ATI'
                    },
                    yAxis: [
                        {
                            title: {
                                text: 'Numar'
                            },

                        }
                    ],
                    plotOptions: {
                        column: {
                            stacking: 'normal',
                            dataLabels: {
                                enabled: false
                            }
                        }
                    },

                    series: [
                        {
                            name: 'Cazuri active',
                            data: chart_data['active_cases'],
                            type: 'column',

                        },
                        {
                            name: 'Vindecati',
                            data: chart_data['recovered'],
                            type: 'column',

                        },

                        {
                            name: 'Morti',
                            data: chart_data['dead'],
                            type: 'column',

                        },
                        {
                            name: 'ATI',
                            data: chart_data['icu'],
                            type: 'column',

                        },

                        // {
                        //     name: 'Rata cazuri noi',
                        //     data: chart_data['ratio'].map(x => {
                        //         return {x: new Date(x[0]), y: 1 + x[1]}
                        //     }),
                        //     dashStyle: 'shortdot',
                        //     type: 'spline',
                        //
                        //     yAxis: 2,
                        // },
                    ],
                    xAxis: {
                        type: 'datetime',

                    },
                    tooltip: {
                        xDateFormat: '%Y-%m-%d',
                        shared: true
                    },


                },
                chartOptionsICU: {
                    title: {
                        text: 'Terapie intensiva'
                    },
                    yAxis: [
                        {
                            title: {
                                text: 'Pacienti terapie intensiva'
                            },

                        }
                    ],

                    series: [
                        {
                            name: 'Pacienti terapie intensiva',
                            data: chart_data['icu'],
                            yAxis: 0,
                        },
                        // {
                        //     name: 'Rata cazuri noi',
                        //     data: chart_data['ratio'].map(x => {
                        //         return {x: new Date(x[0]), y: 1 + x[1]}
                        //     }),
                        //     dashStyle: 'shortdot',
                        //     type: 'spline',
                        //
                        //     yAxis: 2,
                        // },
                    ],
                    xAxis: {
                        type: 'datetime',

                    },
                    tooltip: {
                        xDateFormat: '%Y-%m-%d',
                        shared: true
                    },


                },
                chartOptionsNewCasesTests: {
                    title: {
                        text: 'Cazuri noi/teste'
                    },
                    yAxis: [
                        {
                            title: {'text': 'Cazuri noi'},
                        },
                        {
                            title: {
                                text: 'Numar teste pe zi'
                            },

                        },
                        {
                            title: {
                                text: 'Rata teste/confirmati',

                            },
                            opposite: true,

                        },
                    ],

                    series: [
                        {
                            name: 'Rata teste/confirmati',
                            data: chart_data['ratio_tests_cases'],
                            type: 'column',
                            yAxis: 2,
                            tooltip: {
                                valueDecimals: 3,

                            },

                        },
                        {
                            name: 'Cazuri noi',
                            data: chart_data['delta_cases'],
                            yAxis: 0,

                        },
                        {
                            name: 'Numar teste pe zi',
                            data: chart_data['delta_tests'],
                            yAxis: 1,
                        },
                    ],
                    xAxis: {
                        type: 'datetime',

                    },
                    tooltip: {
                        xDateFormat: '%Y-%m-%d',
                        shared: true
                    },


                },
                chartOptionsNewCasesTests2: {
                    title: {
                        text: 'Cazuri noi/teste'
                    },
                    yAxis: [
                        {
                            title: {'text': 'Cazuri noi'},
                        },
                        {
                            title: {
                                text: 'Numar teste pe zi'
                            },

                        },
                        {
                            title: {
                                text: 'Rata teste/confirmati',

                            },
                            opposite: true,

                        },
                    ],

                    series: [
                        // {
                        //     name: 'Rata teste/confirmati',
                        //     data: chart_data['ratio_tests_cases'],
                        //     type: 'column',
                        //     yAxis: 2,
                        //     tooltip: {
                        //         valueDecimals: 3,
                        //
                        //     },
                        //
                        // },
                        {
                            name: 'Cazuri noi',
                            data: chart_data['delta_cases'].map(v => ({
                                x: v['x'] + 86400 * 1000, y: v['y']
                            })),
                            yAxis: 0,

                        },
                        {
                            name: 'Numar teste pe zi',
                            data: chart_data['delta_tests'],
                            yAxis: 1,
                        },
                    ],
                    xAxis: {
                        type: 'datetime',

                    },
                    tooltip: {
                        xDateFormat: '%Y-%m-%d',
                        shared: true
                    },


                },
                chartOptionsDeadConfirmed: {
                    title: {
                        text: 'Cazuri confirmate/decedati'
                    },
                    yAxis: [
                        {
                            title: {'text': 'Cazuri totale'},
                            opposite: true,
                        },
                        {
                            title: {
                                text: 'Persoane decedate'
                            },

                        }
                    ],

                    series: [
                        {
                            name: 'Cazuri noi',
                            data: chart_data['cases'],
                            yAxis: 0,

                        },
                        {
                            name: 'Persoane decedate',
                            data: chart_data['dead'],
                            yAxis: 1,
                        },
                    ],
                    xAxis: {
                        type: 'datetime',

                    },
                    tooltip: {
                        xDateFormat: '%Y-%m-%d',
                        shared: true
                    },


                },
                chartOptionsRate: {
                    title: {
                        text: 'Rata noilor infectii'
                    },
                    yAxis: [
                        // {
                        //     title: 'Cazuri totale',
                        //     opposite: true,
                        // },
                        {
                            title: {
                                text: 'Numar infectii noi'
                            },
                            opposite: true,

                        }
                        , {
                            title: {
                                text: 'Rata noilor infectii'
                            },
                            // type: 'logarithmic',
                            max: 0.4,


                        },
                    ],

                    series: [
                        {
                            name: 'Cazuri noi',
                            data: chart_data['delta_cases'],
                            yAxis: 0,
                            type: 'column',

                        },
                        {
                            name: 'Rata cazuri noi',
                            data: chart_data['ratio_cases'],
                            dashStyle: 'shortdot',
                            type: 'spline',
                            tooltip: {
                                valueDecimals: 3,

                            },

                            yAxis: 1,
                        },
                    ],
                    xAxis: {
                        type: 'datetime',

                    },
                    tooltip: {
                        xDateFormat: '%Y-%m-%d',
                        shared: true,


                    },


                },
                chartOptionsCasesTests: {
                    title: {
                        text: 'Cazuri totale/nr teste'
                    },
                    subtitle: {
                        text: 'Sursa datelor <a style="color: blue" href="https://beta.dela0.ro/cat-si-cum-testeaza-romania-am-obtinut-datele-statului-despre-numarul-de-probe-prelucrate-si-stocul-de-teste-din-fiecare-spital/">dela0</a>',
                        useHtml: true,
                    },

                    yAxis: [
                        {
                            title: {'text': 'Cazuri totale'},
                            opposite: true,
                        },
                        {
                            title: {
                                text: 'Numar teste'
                            },

                        },
                        {
                            title: {
                                text: 'Numar persoane testate'
                            },

                        },
                        // , {
                        //     title: {
                        //         text: 'Rata noilor infectii'
                        //     },
                        //
                        // },
                    ],

                    series: [
                        {
                            name: 'Cazuri totale',
                            data: chart_data['cases'],
                            yAxis: 0,
                        },
                        {
                            name: 'Teste efectuate',
                            data: chart_data['tests'],
                            yAxis: 1,
                        },
                        {
                            name: 'Persoane testate',
                            data: chart_data['tested_people'],
                            yAxis: 1,
                        },
                    ],
                    xAxis: {
                        type: 'datetime',

                    },
                    tooltip: {
                        xDateFormat: '%Y-%m-%d',
                        shared: true
                    },


                }
            }
        }

    }
</script>

<style scoped>
</style>

import {Module, VuexModule, Mutation, Action} from 'vuex-module-decorators'
import axios from 'axios';

@Module
export default class COVID19 extends VuexModule {
    data = {};
    fetched_data = false;

    @Action({commit: 'data_fetched'})
    async fetch_data() {
        const result = await axios.get(`https://storage.googleapis.com/covid19-romania/data/latest_data_fixed_new_2.json`);
        return result.data;
    }

    @Mutation
    data_fetched(data) {
        this.data = data;
        this.fetched_data = true;

    }

    log = {};
    fetched_log = false;

    @Action({commit: 'log_fetched'})
    async fetch_log() {
        const result = await axios.get(`https://storage.googleapis.com/covid19-romania/data/latest_log.json`);
        return result.data;
    }

    @Mutation
    log_fetched(log) {
        this.log = log.map(obj => {
            const ts = obj.timestamp;
            delete obj.timestamp;
            let rate;
            if (obj.cazuri_initiale) {
                rate = `${((obj.cazuri_delta / obj.cazuri_initiale) * 100).toFixed(2)}%`
            } else {
                rate = 'N/A'
            }
            return {...obj, rata_crestere: rate, timestamp: ts}
        });
        this.fetched_log = true;

    }

    chart_data = {};
    fetched_chart_data = false;

    @Action({commit: 'chart_data_fetched'})
    async fetch_chart_data() {
        const result = await axios.get(`/api/data/`);
        return result.data;
    }

    @Mutation
    chart_data_fetched(data) {
        data = data.map(obj => {
            return ({...obj, date: new Date(obj.date).getTime()});
        })
        const chart_data = ['cases', 'tests', 'tested_people', 'dead', 'icu', 'critical', 'recovered'].reduce((obj, v) => {
            obj[v] = data.map(o => ({x: o.date, y: o[v]})).filter(o => o['y'])
            return obj
        }, {})
        for (const [k, v] of Object.entries(chart_data)) {
            chart_data[`delta_${k}`] = v.map((value, index, array) => {
                    if (index === 0) {
                        return {x: value['x'], y: NaN}
                    }
                    if (value['x'] - array[index - 1]['x'] > 86400000) {
                        return {x: value['x'], y: NaN}

                    }
                    return {x: value['x'], y: value['y'] - array[index - 1]['y']}


                }
            ).filter(o => o['y'])
            chart_data[`ratio_${k}`] = v.map((value, index, array) => {
                    if (index === 0) {
                        return {x: value['x'], y: NaN}
                    }
                    if (value['x'] - array[index - 1]['x'] > 86400000) {
                        return {x: value['x'], y: NaN}

                    }
                    if (value['y'] < 100) {
                        return {x: value['x'], y: NaN}

                    }
                    return {x: value['x'], y: (value['y'] - array[index - 1]['y']) / (array[index - 1]['y'])}


                }
            ).filter(o => o['y'])
        }
        const test_delta_obj = chart_data['delta_tests'].reduce((obj, v) => {
            obj[v.x] = v.y
            return obj
        }, {})
        chart_data['ratio_tests_cases'] = chart_data['delta_cases'].map(v => {
            if (v['x'] in test_delta_obj) {
                return {x: v['x'], y: v['y'] / test_delta_obj[v['x']]}
            } else {
                return {x: v['x'], y: NaN}
            }

        })
        const recovered = chart_data['recovered'].reduce((obj, v) => {
            obj[v.x] = v.y
            return obj
        }, {})
        const icu = chart_data['icu'].reduce((obj, v) => {
            obj[v.x] = v.y
            return obj
        }, {})
        chart_data['active_cases'] = chart_data['cases'].map(v => {
            if (v['x'] in recovered && v['x'] in icu) {
                return {x: v['x'], y: v['y'] - recovered[v['x']] - icu[v['x']]}
            } else {
                return {x: v['x'], y: NaN}
            }
        })

        this.chart_data = chart_data
        this.fetched_chart_data = true;

    }

}

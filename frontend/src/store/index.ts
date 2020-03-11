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
    data_fetched(data: any) {
        this.data = data;
        this.fetched_data = true;

    }

}

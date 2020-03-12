<template>
    <div v-if="covid19.fetched_data" id="tablediv" style="width: 40vw">
        <b-table :small="true" hover :items="covid19.data" :fields="tableFields"
                 sort-by="Cazuri_confirmate"
                 :sort-desc="true">
            <template v-slot:thead-top="data">
                <b-tr>
                    <b-th></b-th>
                    <b-th v-for="field in totals">
                        {{field}}
                    </b-th>
                </b-tr>
            </template>
        </b-table>
    </div>

</template>

<script>
    import {Component, Vue} from "vue-property-decorator";
    import {mapState} from "vuex";

    @Component({
        computed: mapState(['covid19']),

    })
    export default class RomaniaMap extends Vue {
        get totals() {
            if (this.$store && this.$store.state.covid19.fetched_data) {
                const data = this.$store.state.covid19.data;
                return [
                    data.map(o => o.Cazuri_confirmate).reduce((a, c) => {
                        return a + c
                    }),
                    data.map(o => o.Persoane_in_carantina).reduce((a, c) => {
                        return a + c
                    }),
                    data.map(o => o.Persoane_izolate).reduce((a, c) => {
                        return a + c
                    }),

                ]
            }

        }

        data() {
            return {
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
    }
</script>

<style scoped>

</style>

<template>
    <div v-if="covid19.fetched_data" id="tablediv" class="data-table">
        <b-table :small="true" hover :items="covid19.data" :fields="tableFields"
                 sort-by="Cazuri_confirmate"
                 :sort-desc="true">
            <template v-slot:thead-top="data">
                <b-tr>
                    <b-th></b-th>
                    <b-th v-for="field in totals" v-bind:key="field.id">
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
    .data-table {
        margin-top:5rem;
        flex-basis: 100%;
    }
        .data-table >>> th {
            font-size: 0.8rem;
        }

     @media all and (min-width:800px){
        .data-table {
            flex-basis:45%;
            margin-top:1rem;
        } 
        .data-table >>> th {
                font-size: 1rem;
            }
        
    }
</style>

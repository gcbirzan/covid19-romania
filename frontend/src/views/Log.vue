<template>
  <div v-if="covid19.fetched_log">
            <b-table :small="true" style="width: 40vw" hover :items="covid19.log" sort-by="timestamp"
                     :sort-desc="true">
                <template v-slot:cell(timestamp)="data">
                    {{ new Date(data.value).toLocaleDateString() }} {{ new Date(data.value).toLocaleTimeString() }}.
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
    export default class Log extends Vue {
        mounted() {
            this.$store.dispatch('fetch_log');
            setInterval(() => {
                this.$store.dispatch('fetch_log');
            }, 60000);

        }

    }

</script>

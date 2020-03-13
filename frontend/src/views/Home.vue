<template>
        <div class="flex-container" id="containerdiv">
            <div class="map-size" >

                    <RomaniaMap/>

            </div>
            <CasesTable/>
        </div>
</template>

<script>
    // @ is an alias to /src
    import RomaniaMap from '@/components/RomaniaMap.vue'
    import CasesTable from "@/components/CasesTable";

    export default {
        name: 'Home',
        components: {
            CasesTable,
            RomaniaMap
        }
    }
</script>

<style scoped>
    @media only screen and (min-width: 1000px) {
        .flex-container {
            display: flex;
        }

        .map-size {
            height: 80vh;
            width: 55vw;
        }

        .fixed-map {
            position: fixed
        }
    }

    @media only screen and (max-width: 1000px) {
        .map-size {
            display: none;
        }

    }

</style>

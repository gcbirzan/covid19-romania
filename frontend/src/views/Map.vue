<template>
    <div class="map">
        <div class="flex-container" id="containerdiv">
            <div class="map-size" >
                <div class="map-size fixed-map" id="mapdiv">

                    <RomaniaMap/>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
    // @ is an alias to /src
    import RomaniaMap from '@/components/RomaniaMap.vue'
    import CasesTable from "@/components/CasesTable";

    export default {
        name: 'Map',
        components: {
            CasesTable,
            RomaniaMap
        }
    }
</script>
<style scoped>
    #mapdiv {
        height: 100vh;
        width: 100vh;
        position: absolute !important;
    }

    @media only screen and (min-width: 600px) {
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

    @media only screen and (max-width: 600px) {
        .map-display {
            display: flex;
        }

    }

</style>

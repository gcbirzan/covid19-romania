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
    .flex-container {
        display: flex;
        flex-wrap:wrap;
        justify-content:space-between;
    }

    .map-size {
        height: 40vh;
        flex-basis:90%;
    }

    .fixed-map {
        width:100%;
        height:100%;
    }
    .data-table {
        margin-top:50px;
        flex-basis: 90%;
    }

    @media all and (min-width:800px){
        .map-size {
            height: 70vh;
            flex-basis:50%;
        }

        .data-table {
            flex-basis:45%;
            margin-top:0;
        } 
    }

</style>

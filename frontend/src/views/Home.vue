<template>
        <div class="flex-container" id="containerdiv">
            <div class="home-map-container">
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
        align-items: stretch;
    }

    .home-map-container {
        flex-basis:90%;
    }

    @media all and (min-width:800px){
        .home-map-container {
            height: 70vh;
            flex-basis:50%;
            position:sticky;
            top:10vh;
        }
    }

</style>

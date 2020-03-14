<template>
        <div class="flex-container" id="containerdiv">
            <RomaniaMap/>
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
    .flex-container {
        width:100%;
        height:70vh;
    }

</style>

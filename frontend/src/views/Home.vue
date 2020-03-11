<template>
  <div class="home">
    <RomaniaMap/>
  </div>
</template>

<script>
// @ is an alias to /src
import RomaniaMap from '@/components/RomaniaMap.vue'

export default {
  name: 'Home',
  components: {
    RomaniaMap
  }
}
</script>

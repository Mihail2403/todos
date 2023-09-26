<template>
  <div>
    <router-view/>
  </div>
</template>

<script>
import Registration from "@/views/Registration.vue";

export default {
  components: {Registration}

}
</script>

<style scoped>
  body {
    padding: 0;
    margin: 0;
  }
</style>
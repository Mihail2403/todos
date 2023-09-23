<template>
  <div>
    logout
    <br>
    <button @click.prevent="logout">Выйти</button>
  </div>
</template>

<script>
export default {
  methods: {
    logout(){
      console.log("logout success")
    }
  }
}
</script>

<style scoped>

</style>
<template>
  <div>
    <input v-model="username" placeholder="Username">
    {{username}}
    <br>
    <input v-model="email" placeholder="Email">
    <br>
    <input v-model="password" placeholder="Password">
    <br>
    <input type="submit" value="Send" @click.prevent="submitRegForm">
    {{message}}
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data(){
    return {
      username: "",
      email: "",
      password: "",
      message:""
    }
  },
  methods:{
    submitRegForm(){
      if (this.username && this.password && this.email) {
        axios.post('http://localhost:8000/auth/reg/', {
          "username": this.username,
          "email": this.email,
          "password": this.password
        }, {})
        this.message = ""
        this.email = ""
        this.password = ""
        this.username = ""
      } else {
        this.message = "Ты ишак"
      }
    }
  }
}
</script>

<style scoped>

</style>

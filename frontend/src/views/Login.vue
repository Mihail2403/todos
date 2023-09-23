<template>
  <div>
    <input v-model="username" placeholder="Username">
    <br>
    <input v-model="password" placeholder="Password">
    <br>
    <input type="submit" value="Send" @click.prevent="submitLoginForm">
  </div>
</template>

<script>
import axios from "axios";
import router from "@/router";
export default {
  data(){
    return {
      username: "",
      password: "",
      message:""
    }
  },
  methods:{
    submitLoginForm(){
      if (this.username && this.password) {
        axios.post('http://localhost:8000/auth/token/', {
          "username": this.username,
          "password": this.password
        }, {})
            .then(function (response) {
              console.log(response.data)
              localStorage.setItem('accessToken', response.data.access)
              localStorage.setItem('refreshToken', response.data.refresh)
              router.push('/')
        })

      } else {
        this.message = "Ты ишак"
      }
    }
  }
}
</script>

<style scoped>

</style>
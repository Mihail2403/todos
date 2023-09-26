<template>
  <div class="main-reg">
    <input class="form-text" v-model="username" placeholder="Username">
    {{username}}
    <br>
    <input class="form-text" v-model="email" placeholder="Email">
    <br>
    <input class="form-text" v-model="password" placeholder="Password">
    <br>
    <input class="butt" type="submit" value="Send" @click.prevent="submitRegForm">
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
        location.assign('/login')
      } else {
        this.message = "Ты ишак"
      }
    }
  }
}
</script>

<style scoped>
.main-reg {
  display: flex;
  flex-direction: column;
  justify-content: center;
  justify-items: center;
  height: 100%;
  margin-top: 20%;
}
.form-text {
  width: 300px;
  margin-left: auto;
  margin-right: auto;
}
</style>

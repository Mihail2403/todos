<template>
  <div id="main-login">
    <input class="form-text" v-model="username" placeholder="Username">
    <br>
    <input class="form-text" v-model="password" placeholder="Password">
    <br>
    <input class="butt" type="submit" value="Send" @click.prevent="submitLoginForm">
    <div v-if="this.message !== ``">
      {{message}}
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data(){
    return {
      username: "",
      password: "",
      message: ""
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
              location.assign('/')
        })
            .catch(
                function(e){
                  try {
                    if (e.response.data.detail === "No active account found with the given credentials") {
                      var el = document.getElementById('main-login')
                      el.style.background = 'crimson'
                    }
                  }catch (err) {
                    console.log(err)
                  }
            })

      } else {
        this.message = "Ты ишак"
      }
    }
  }
}
</script>

<style scoped>
  #main-login {
    display: flex;
    flex-direction: column;
    justify-content: center;
    justify-items: center;
    height: 100%;
    margin-top: 20%;
    padding:20px;
    border-radius: 20px;

  }
  .form-text {
    width: 300px;
    margin-left: auto;
    margin-right: auto;
  }
</style>
<template>
  <div>
    home n
  </div>
</template>

<script>
import axios from "axios";
import router from "@/router";
function refresh(refresh){
  axios.post('http://localhost:8000/auth/token/refresh/',
      {
        "refresh": refresh
      }).then(
          function (response) {
            localStorage.setItem('accessToken', response.data.access)
            localStorage.setItem('refreshToken', response.data.refresh)
            location.reload()
  }).catch(
      function (e) {
        if (e.response.data.code === "token_not_valid") {
          router.push('/login')
        }
  })
}
export default {
  mounted() {
    axios.get('http://localhost:8000/api/v1/',
        {
          headers:
              {
                "Authorization":`Bearer ${localStorage.getItem('accessToken')}`
              }
        })
        .then(
            function (response) {
              console.log(response.data)
            }).catch(
        function (e) {
          // если токен не валиден
          if (e.response.data.code === "token_not_valid") {
            refresh(localStorage.getItem('refreshToken'))
          }
        })
  }
}
</script>

<style scoped>

</style>
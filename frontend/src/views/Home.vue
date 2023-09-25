<template>
  <div class="main-home-block">
    <div class="form-add-task">
      <div>Добавить задачу</div>
      <input class="add-text" type="text" placeholder="Текст" maxlength="50">
      <button class="del">Создать</button>
    </div>
    <div v-for="task in tasks" class="tasks-list">
      <task :task="task"/>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import router from "@/router";
import Task from "@/components/Task.vue";
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
  components: {Task},
  data(){
    return {
      tasks: [],
    }
  },
  mounted() {
    axios.get('http://localhost:8000/api/v1/',
        {
          headers:
              {
                "Authorization":`Bearer ${localStorage.getItem('accessToken')}`
              }
        })
        .then(
            response => {
              this.tasks = [...response.data]
            })
        .catch(
            function (e) {
              console.log(e)
              // если токен не валиден
              if (e.response.data.code === "token_not_valid") {
                refresh(localStorage.getItem('refreshToken'))
              }
        })
  }
}
</script>

<style scoped>
 .main-home-block {
    margin-left: auto;
    margin-right: auto;
    width: 380px;
  }
 .form-add-task {
   width: 100%;
   display: flex;
   flex-direction: column;
   justify-content: center;
 }
 .add-text {
   width: 100%;
   border: black solid 2px;
   border-radius: 10px;
   padding-left: 3px;
   padding-right: 3px;
   height: 30px;
 }
</style>
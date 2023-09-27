<template>
  <div class="main-home-block">
    <div class="form-add-task">
      <div>Добавить задачу</div>
      <input class="form-text" id="text" type="text" placeholder="Текст" maxlength="50">
      <button class="butt" @click.prevent="addTask">Создать</button>
    </div>
    <div v-if="tasks.length > 0">
      <div v-for="task in tasks" :key="tasks.indexOf(task)" class="tasks-list">
        <task :task="task" @deleteTask="deleteTask"/>
      </div>
    </div>
    <div v-else>
      <task :task="{text:`Добавить новую задачу`}"/>
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
        try{
          console.log(e)
          if (e.response.data.code === "token_not_valid") {
            router.push('/login')
          } else if (e.response.data.refresh[0] === "This field may not be null.") {
            router.push('/login')
          }
        } catch (e) {
          console.log(e)
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
  methods: {
    addTask(){
      var text = document.getElementById('text')
      var task = this.tasks.push({text:text.value, id:Math.random()})
      console.log(task)
      axios.post('http://localhost:8000/api/v1/',
          {
            'text': text.value
          },
          {
            headers:
                {
                  "Authorization":`Bearer ${localStorage.getItem('accessToken')}`
                }
          }
          )
          .then(
              function (response) {
                if(response.data['status'] === 'bad'){
                  console.log("trouble")
                }
      })
      text.value = ""
    },
    deleteTask(task){
      this.tasks = this.tasks.filter(arr_task => arr_task.id !== task.id)
      axios.post('http://localhost:8000/api/v1/delete/',
          {
            'text':task.text
          },
          {
            headers:
                {
                  "Authorization":`Bearer ${localStorage.getItem('accessToken')}`
                }
          }
      )
          .then(
              function (response) {
                if(response.data['status'] === 'bad'){
                  console.log("trouble")
                }
              })
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

<style>
 .main-home-block {
    margin-left: auto;
    margin-right: auto;
    width: 370px;
  }
 .form-add-task {
   width: 100%;
   display: flex;
   flex-direction: column;
   justify-content: center;
 }
 .form-text {
   width: 98%;
   border: black solid 2px;
   border-radius: 10px;
   padding-left: 3px;
   padding-right: 3px;
   height: 30px;
   margin: 5px 0;
 }
</style>
<template>
  <div class="task-body">
    <div class="text">{{task.text}}</div>
    <button class="butt" @click="deleteTask">Удалить</button>
  </div>
</template>

<script>
export default {
  props: {
    task: {
      type: Object,
      required: true
    }
  },
  methods: {
    deleteTask(){
      this.$emit('deleteTask', this.task)
    }
  }
}
</script>

<style>
.task-body {
  margin-top: 20px;
  text-align: center;
  color: black;
  font-size: 20px;
  border: black solid 2px;
  min-height: 100px;
  padding: 5px;
  background: aliceblue;
  border-radius: 15px;
}
.butt {
  width: 100px;
  margin-left: auto;
  margin-right: auto;
  background: black;
  color: aliceblue;
  border-radius: 5px;
}
.butt:hover {
  background: aliceblue;
  color: black;
}
</style>
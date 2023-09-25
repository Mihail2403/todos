<template>
  <div class="task-body">
    <div class="text">{{task.text}}</div>
    <button class="del">Удалить</button>
  </div>
</template>

<script>
export default {
  props: {
    task: {
      type: Object,
      required: true
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
.del {
  width: 100px;
  margin-left: auto;
  margin-right: auto;
  background: black;
  color: aliceblue;
  border-radius: 5px;
}
.del:hover {
  background: aliceblue;
  color: black;
}
</style>
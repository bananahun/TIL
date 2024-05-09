<template>
  <div class="child-box">
    <h3>자식 페이지</h3>
    <p>자식 이름: {{ child.name }}</p>
  </div>
</template>

<script setup>
defineProps({
  child: Object
})
</script>

<style scoped>
.child-box {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 20px;
  background-color: #ffffff;
}
</style>
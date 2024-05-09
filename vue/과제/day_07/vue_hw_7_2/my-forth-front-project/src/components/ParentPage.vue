<template>
  <div class="box">
    <h2>부모 컴포넌트</h2>
    <p>아버지: {{ family.father }}</p>
    <p>어머니: {{ family.mother }}</p>
    <ChildPage 
    v-for="(child, index) in family.children" 
    :key="index" 
    :child="child" 
    />
  </div>
</template>

<script setup>
import ChildPage from'@/components/ChildPage.vue'

defineProps({
  family: Object
})
</script>

<style scoped>
.box {
  border: 1px solid #F9F9F9;
  padding: 10px;
  margin-bottom: 20px;
  background-color: #F9F9F9;
}
</style>
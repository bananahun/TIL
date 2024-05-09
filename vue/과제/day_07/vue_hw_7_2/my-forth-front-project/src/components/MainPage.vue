<template>
  <div>
    <h1>pinia 연습하기</h1>
    <div class="asdasd">
      <ParentPage 
      v-for="(family, index) in familyInfo" 
      :key="index" 
      :family="family" 
      />
    </div>
  </div>
</template>

<script setup>
import { useFamilyStore } from '@/stores/family'
import ParentPage from '@/components/ParentPage.vue'

const { familyInfo } = useFamilyStore()
console.log(familyInfo)
</script>

<style scoped>
.asdasd {
  text-align: center;
}
</style>
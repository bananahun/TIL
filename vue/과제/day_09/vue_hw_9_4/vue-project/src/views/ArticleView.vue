<template>
  <div>
    <h1>게시글 목록 페이지</h1>
    <RouterLink :to="{ name: 'CreateView' }">
      게시글 생성
    </RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useCounterStore()

onMounted(() => {
  store.getArticles()
})

</script>

<style>

</style>

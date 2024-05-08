<template>
  <div>
    <RouterLink :to="{ name: 'user-profile' }"> Profile</RouterLink>
    <RouterLink :to="{ name: 'user-posts' }"> Posts</RouterLink>
    <h1>UserView</h1>
    <h2>{{ $route.params.id }}번 User 페이지</h2>
    <h2>{{ userId }}번 User 페이지</h2>
    <button @click="goHome">홈으로!</button>
    <hr>
    <RouterView/>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router';

const route = useRoute()
const userId = ref(route.params.id)

const router = useRouter()
const goHome = function () {
  // router.push({name: 'home' })
  router.replace({name: 'home' })
}
</script>

<style scoped>

</style>
<template>
  <header>
    <div class="wrapper">
      <nav v-if="store.isLogin">
        <RouterLink :to="{ name: 'ArticleView' }">Home</RouterLink> |
      </nav>
      <nav v-else> 
        <RouterLink :to="{ name: 'ArticleView' }">Home</RouterLink> |
        <RouterLink :to="{ name: 'SignUpView' }">SignUp</RouterLink> |
        <RouterLink :to="{ name: 'LogInView' }">LogIn</RouterLink>
      </nav>
    <RouterView />
    </div>
  </header>
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { useCounterStore } from './stores/counter';

const store = useCounterStore()
</script>

<style scoped>
</style>

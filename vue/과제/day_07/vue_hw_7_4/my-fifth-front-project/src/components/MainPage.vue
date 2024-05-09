<template>
  <div
  v-for="(balance, index) in balances"
  :key="index"
  :balance="balance">
    <p>이름:{{ balance.name }}</p>
    <p>잔고:{{ balance.balance }}</p>
    <button @click="updateBalance(balance.name)">updateBalance</button>
    <hr>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useBalanceStore } from '@/stores/balance'

const router = useRouter()
const { balances } = useBalanceStore()

const updateBalance = (name) => {
  router.push({ name: 'update', params: { name: name}})
}
</script>
  
<style scoped>

</style>
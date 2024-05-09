<template>
  <div>
    <h1>데이터 수정 페이지</h1>
    <p>이름: {{ name }}</p>
    <p>잔고: {{ balances[balanceIndex].balance }}</p>
    <button @click="increase">+</button>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { useBalanceStore } from '@/stores/balance'

const route = useRoute()
const name = route.params.name

// balance 데이터를 가져옴
const { balances, updateBalance } = useBalanceStore()

// name을 기준으로 해당 balance를 찾음
const balanceIndex = balances.findIndex(item => item.name === name)
const balance = balanceIndex !== -1 ? balances[balanceIndex].balance : 0

const increase = function(){
  balances[balanceIndex].balance += 1000
  updateBalance(balances[balanceIndex]) 
  console.log(balances[balanceIndex].balance)
}

</script>

<style scoped>

</style>

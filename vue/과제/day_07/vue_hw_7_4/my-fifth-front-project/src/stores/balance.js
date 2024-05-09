import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('balance', () => {
  const balances  = [
    {
      name: '김하나',
      balance: 100000
      },
      {
      name: '김두리',
      balance: 10000
      },
      {
      name: '김서이',
      balance: 100
      },
  ] 
  const updateBalance = (updatedBalance) => {
    const index = balances.findIndex(balance => balance.name === updatedBalance.name)
    if (index !== -1) {
      balances[index].balance = updatedBalance.balance
    }
  }

  return { 
    balances,
    updateBalance,
    // getNames
  };
});

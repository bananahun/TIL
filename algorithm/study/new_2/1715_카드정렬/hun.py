import sys

input = sys.stdin.readline

n = int(input())

cards = []
for _ in range(n):
    cards.append(int(input()))

cards.sort()

total_sum = 0
cumulative_sum = 0

for i in range(n):
    cumulative_sum += cards[i]
    total_sum += cumulative_sum

print(total_sum)

'''
10 20 40 60

30
70
130

40 60 80 60 
'''

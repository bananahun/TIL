import sys
from itertools import combinations
sys.stdin = open('input.txt')
N, S = map(int, input().split())
lst = list(map(int, input().split()))
result = 0
for i in range(1, N+1):
    cnt = 0
    for num in combinations(lst, i):
        if sum(num) == S:
            result +=1
print(result)

    


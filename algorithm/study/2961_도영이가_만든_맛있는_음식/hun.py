import sys
import math
from itertools import combinations

sys.stdin = open('input.txt')

N = int(input())
taste = []
for _ in range(N):
    s, b = map(int, input().split())
    taste.append([s,b])
case = []
for k in range(1, N+1):
    case.append(combinations(taste, k))

result = []
for _ in range(len(case)+1):
    sss = 0
    bbb = 1
    for i in range(len(case)):
        sss += taste[i][0]
        bbb = bbb*taste[i][1]
        if len(result) == i:
            yummy = abs(sss-bbb)
            result.append(yummy)

print(min(result))





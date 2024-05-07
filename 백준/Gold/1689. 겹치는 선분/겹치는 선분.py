import sys

input = sys.stdin.readline

N = int(input())

lst = []

for _ in range(N):
    start, end = map(int, input().split())
    lst.append((start, 1))  
    lst.append((end, -1))

lst.sort()

check = 0
result = 0

for a,b in lst:
    check += b
    result = max(result, check)

print(result)
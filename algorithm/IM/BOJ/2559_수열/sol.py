import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
lst = list(map(int, input().split()))
max = -100 * N
for i in range(0, N-K):
    cnt = 0
    for idx in range(i, i+K):
        for i in range()
    if max < cnt:
        max = cnt
print(max)

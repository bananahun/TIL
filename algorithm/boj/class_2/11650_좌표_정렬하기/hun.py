import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
lst = []
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    lst.append([a,b])
lst.sort(key = lambda x : (x[0], x[1]) )
for num in lst:
    print(*num)

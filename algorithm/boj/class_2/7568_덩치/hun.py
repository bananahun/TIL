import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append([x, y, 0])
# print(lst)
result = []
for check in range(N):
    cnt = 1
    for all in range(N):
        if lst[check][0] < lst[all][0] and lst[check][1] < lst[all][1]:
            cnt += 1
    result.append(cnt)
print(*result)

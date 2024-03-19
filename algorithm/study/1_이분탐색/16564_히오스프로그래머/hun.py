import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
N, level = map(int, input().split())
lst = []
for _ in range(N):
    a = int(input())
    lst.append(a)
lst.sort()
s = lst[0]
e = lst[N-1]+level

def check(lst, k):
    cnt = 0
    for num in lst:
        if num < k:
            cnt = cnt + k - num
    return cnt
cnt = 0
while s <= e:
    mid = (s+e)//2
    if check(lst, mid) <= level:
        s = mid + 1
    else:
        e = mid - 1
print(s-1)
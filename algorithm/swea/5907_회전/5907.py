import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    num, times = map(int, input().split())
    lst = list(map(int, input().split()))
    dq = deque(lst)
    for _ in range(times):
        dq.append(dq.popleft())
    print(f'#{tc} {dq.popleft()}')





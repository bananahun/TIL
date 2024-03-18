import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    # 노드의 수, 입력 받을 간선의 양쪽 노드 번호 줄 수
    n, v = map(int, input().split())
    lst = [[]for _ in range(n+1)]
    visited = [0] * (n+1)
    # 입력 받을 줄 수 만큼
    for _ in range(v):
        # 시작 번호와 끝 번호를 입력 받아서
        a, b = map(int, input().split())
        # 큐에 넣어 둔다
        lst[a].append(b)
        lst[b].append(a)
    # print(lst)
    # 출발 노드와 도착 노드를 입력 받는다
    s, e = map(int, input().split())
    dq = deque()
    dq.append(s)
    cnt = 0
    while dq:
        ck = dq.popleft()
        if ck == e:
            cnt = 1
        for num in lst[ck]:
            if visited[num] == 0:
                dq.append(num)
                visited[num] = visited[ck] + 1
    print(f'#{tc} {visited[e]}')
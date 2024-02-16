import sys

sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    miro = [list(map(int, input())) for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[0] * n for _ in range(n)]

    dq = deque()
    # 시작점 찾기
    for i in range(n):
        for j in range(n):
            if miro[i][j] == 2:
                sx = j
                sy = i
    # 도착지점 찾기
    for i in range(n):
        for j in range(n):
            if miro[i][j] == 3:
                ex = j
                ey = i
    # 큐에 시작지점 넣기
    dq.append((sx, sy))
    visited[sy][sx] = 1
    # 체크 기본값 0으로 시작
    ck = 0
    while dq:
        cx, cy = dq.popleft()
        # 도착한다면 체크 값을 1로 바꾸기
        if miro[cy][cx] == 3:
            ck = 1
            break
        # 델타 탐색 4방향으로 진행
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            # x, y범위 안에 들어오고 visited 가 0이고 벽을 안만난다면
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0 and miro[ny][nx] != 1:
                # 큐에 넣어주기
                dq.append((nx, ny))
                # 이동거리를 확인 해주기 위해 visited 값을 1씩 증가 시키기
                # visited 는 0일때만 가는것이기 때문에 값이 1이든 아니든 상관 없음
                visited[ny][nx] = visited[cy][cx] + 1
    # 도착했을 때만 (ck=1)
    if ck == 1:
        # 시작점과 도착점에도 visited 가 1씩 올라가므로 2를 빼줌
        print(f'#{tc} {visited[ey][ex]-2}')
    # 도착 못하는 경우는 무조건 0 출력
    else:
        print(f'#{tc} 0')


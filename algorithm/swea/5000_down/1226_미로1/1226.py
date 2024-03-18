import sys
sys.stdin = open('input.txt')

from collections import deque

try:
    while True:
        T = int(input())

        miro = [list(map(int, input()))for _ in range(16)]

        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        for i in range(16):
            for j in range(16):
                if miro[i][j] == 2:
                    sx = j
                    sy = i

        dq = deque([(sx, sy)])

        cnt = 0

        visited = [[0]*16 for _ in range(16)]

        while dq:
            cx, cy = dq.popleft()
            if miro[cy][cx] == 3:
                cnt = 1
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0 <= nx < 16 and 0 <= ny < 16 and visited[ny][nx] == 0 and miro[ny][nx] != 1:
                    visited[ny][nx] = 1
                    dq.append((nx, ny))
        print(f'#{T} {cnt}')
except EOFError:
    pass


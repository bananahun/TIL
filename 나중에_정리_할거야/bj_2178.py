import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    visit[y][x] = 1
    
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visit[ny][nx] and miro[ny][nx]:
                visit[ny][nx] = visit[y][x] + 1
                queue.append((ny, nx))
    

N, M = map(int, input().split())
miro = [list(map(int, list(input().strip()))) for _ in range(N)]

visit = [[0]*M for _ in range(N)]
bfs(0, 0)

print(visit[N-1][M-1])
\\
//

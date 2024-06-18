from collections import deque

# 나이트가 움직이는 경우를 모두 정해 보겠습니다. 
dx = [1, 1, -1, -1 ,2, 2, -2, -2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]

def bfs(sx, sy, ex, ey, size):
    visited = [[0]*size for _ in range(size)]
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 1
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            return visited[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < size and 0 <= ny < size:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))  

T = int(input())
for _ in range(T):
    size = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    print(bfs(sx, sy, ex, ey, size))

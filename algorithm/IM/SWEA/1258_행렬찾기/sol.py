import sys

sys.stdin = open('input.txt')

from collections import deque


def dfs(i, j):
    global visited
    dq = deque([(i, j)])
    while dq:
        x, y = dq.pop()
        visited[x][y] = 1
        for num in range(4):
            dx = [0, 0, -1, 1]
            dy = [-1, 1, 0, 0]
            x += dx[num]
            y += dy[num]
            if lst[x][y] and 0 <= x < n and 0 <= y < n and visited[x][y] != 0:
                visited[x][y] = 1
                return dfs(x, y)
            else:
                x -= dx[num]
                y -= dx[num]
                break


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    # print(lst)
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if lst[i][j] != 0 and visited[i][j] == 0:
                dfs(i, j)
                cnt += 1
    print(cnt)

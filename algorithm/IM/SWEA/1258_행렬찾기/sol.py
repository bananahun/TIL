import sys

sys.stdin = open('input.txt')


def bomb(sibal):
    cnt = 0
    dx = [0, 1, 0, -1] # 오른쪽 아래 왼쪽 위
    dy = [1, 0, -1, 0] # 우 하 좌 상
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and sibal[i][j] != 0:
                cnt += 1

                stack = [(i, j)]
                stackkk = [(i, j)]
                visited[i][j] = 1
                while stack:
                    nx, ny = stack.pop()
                    for k in range(4):
                        cx = nx + dx[k]
                        cy = ny + dy[k]

                        if 0 <= cx < N and 0 <= cy < N and visited[cx][cy] == 0 and sibal[cx][cy] != 0:
                            stack.append((cx, cy))
                            stackkk.append((cx, cy))
                            visited[cx][cy] = 1
                stackkk.sort()
                check = [0]
                garo = 1
                for a, b in stackkk:
                    check.append(b)
                try:
                    if check.pop() == check.pop():
                        garo += 1
                except IndexError:
                    garo = 1
                print('넓이다임마', len(stackkk))
                print('가로', garo)

    return cnt


T = int(input())
for tc in range(1, 11):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    # print(visited)
    print(bomb(lst))

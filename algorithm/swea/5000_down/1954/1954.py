import sys
sys.stdin = open('input.txt')

T = int(input())  # test case 받기

dy = [0, 1, 0, -1]  # 우 하 좌 상
dx = [1, 0, -1, 0]


for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]  # 정답을 기록할 배열 생성

    x = 0  # 현재 위치
    y = 0  # 현재 위치
    z = 0  # 이동 방향

    for n in range(1, N*N + 1):
        arr[y][x] = n
        x += dx[z]
        y += dy[z]

        if x not in range(N) or y not in range(N) or arr[y][x] != 0:
            x -= dx[z]
            y -= dy[z]
            z = (z + 1) % 4
            x += dx[z]
            y += dy[z]
    print(f'#{tc}')
    for x in arr:
        print(*x)
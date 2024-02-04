import sys
sys.stdin = open('input.txt')

dx = [0, 0, -1]  # 이동 방향 정의
dy = [-1, 1, 0]

for _ in range(10):
    tc = int(input())  # 테스트 케이스 번호 입력
    arr = [list(map(int, input().split())) for _ in range(100)]  # 100x100 크기의 사다리 맵 입력

    x = arr[99].index(2)  # 마지막 행에서 2가 있는 열

    y = 99  # 시작점(y) 초기화: 맨 아래 행



    while y > 0:
        for i in range(3):
            nx = x + dx[i]  # 다음 위치 계산
            ny = y + dy[i]

            if 0 <= nx < 100 and 0 <= ny < 100 and arr[ny][nx] == 1:
                arr[ny][nx] = 0
                x = nx  # x 위치 업데이트
                break  # 한 번에 한 칸씩만 이동하므로 한 번 이동 후 break

        y -= 1  # 다음 행으로 이동

    if y == 0:
        print(f'#{tc} {x}')
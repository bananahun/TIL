import sys

sys.stdin = open('1210.txt')


for test in range(1,11):
    tc = int(input())  # 테스트 케이스 번호 입력
    arr = [list(map(int, input().split())) for _ in range(100)]  # 100x100 크기의 사다리 맵 입력

    x = arr[99].index(2)  # 마지막 행에서 2가 있는 열

    y = 99  # 시작점(y) 초기화: 맨 아래 행

    while y != 0:

        if 0 < x <= 99 and arr[y][x-1] == 1:
            arr[y][x] = 0
            x = x - 1
        elif 0 <= x < 99 and arr[y][x+1] == 1:
            arr[y][x] = 0
            x = x + 1
        elif arr[y-1][x] == 1:
            y = y - 1
            if y == 0:
                print(f'{test} {x}')

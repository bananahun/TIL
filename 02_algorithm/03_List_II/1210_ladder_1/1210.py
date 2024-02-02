# import sys
# sys.stdin = open('input.txt')
#
#
# for tc in range(10):
#     T = int(input())
#     arr = [list(map(int,input().split())) for _ in range(100)]
#     delta_row = [-1, 1, 0, 0]
#     delta_col = [0, 0, -1, 1]


# def find_value(matrix, target):
#     for row in range(len(matrix)):
#         for col in range(len(matrix[0])):
#             if matrix[row][col] == target:
#                 return (row, col)
#     return (None, None)
#
#
# matrix_1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(find_value(matrix_1, 5))








# def move_in_matrix(matrix, start_row, start_col, direction):
#     # 이동 위치 설정
#     delta = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
#
#     # 이동 후의 위치
#     new_row = start_row + delta[direction][0]
#     new_col = start_col + delta[direction][1]
#
#     # 이동 가능한지 확인하고 리턴
#     if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
#         return new_row, new_col
#     else:
#         return start_row, start_col
#
#
# matrix_2 = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]
# start_row, start_col = 2, 2
# direction = 'up'
# result = move_in_matrix(matrix_2, start_row, start_col, direction)
# print(f"시작 위치: ({start_row}, {start_col}), 이동 방향: {direction}, 결과 위치: {result}")

    # 좌  우  상
dx = [0, 0, -1]
dy = [-1, 1, 0]


for _ in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split()))for _ in range(100)]
    x = arr[99].index(2)
    y = 99
    k = 0
    while y > 0:
        for i in range(3):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 100 and 0 <= ny < 100 and arr[nx][ny] == 1:
                x = nx, y = ny
                

            elif ny == 1:
                print(f'#{T}', y)


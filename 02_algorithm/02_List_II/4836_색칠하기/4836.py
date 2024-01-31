import sys
sys.stdin = open('input.txt')

T = int(input())

# for tc in range(T):
#     line = int(input())
#     for l in range(line):
#         color = list(map(int, input().split()))
#         x_1 = color[0]
#         x_2 = color[2]
#         y_1 = color[1]
#         y_2 = color[3]
#         c_code = color[4]
#         x_range_red = range(0, 1e9)
#         y_range_red = range()
#         x_range_blue = range()
#         y_range_blue = range()
#
#         if c_code == 1:
#             x_range_red = range(x_1, x_2 + 1)
#             y_range_red = range(y_1, y_2 + 1)
#             intersection_range = range(max(x_range_red.start, x_range_blue.start), min(y_range_blue.stop, y_range_red.stop))
#
#         elif c_code == 2:
#             x_range_blue = range(x_1, x_2 + 1)
#             y_range_blue = range(y_1, y_2 + 1)
#             intersection_range = range(max(x_range_red.start, x_range_blue.start), min(y_range_blue.stop, y_range_red.stop))
#     print(intersection_range)
import sys
sys.stdin = open('input.txt')

T = int(input())

for test in range(1, T+1):   # test case만큼 반복
    grid = [[0 for _ in range(10)] for _ in range(10)]
    N = int(input())    # 몇 개의 영역을 칠할지
    purple = 0  # 겹쳐서 보라색이 되는 칸의 수
    for i in range(N):  # 영역 개수만큼 반복
        x1, y1, x2, y2, color = map(int, input().split())
        # [x1, y1]부터 [x2, y2]까지 color로 칠한다
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] += color # color의 값을 더해줌

    for row in range(len(grid)):
        for col in grid[row]:
            if col == 3:
                purple += 1

    print(f'#{test} {purple}')
import sys
sys.stdin = open('input.txt')

# y, x = map(int, input().split())
# num = int(input())
# x -= 1
# y -= 1
# #우 하 좌 상
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
# nx = 1
# ny = 1
# cnt = 0
# for _ in range(1,8):
#     if nx < 1 or nx > x or ny < 1 or ny > y:
#         cnt += 1
#     if cnt % 4 == 0:
#         nx += dx[0]
#         ny += dy[0]
#     elif cnt % 4 == 1:
#         nx += dx[1]
#         ny += dy[1]
#     elif cnt % 4 == 2:
#         nx += dx[2]
#         ny += dy[2]
#     elif cnt % 4 == 3:
#         nx += dx[3]
#         ny += dy[3]
# print(ny, nx)

y, x = map(int, input().split())
num = int(input())
x -= 1
y -= 1
# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
nx = 0
ny = 0
cnt = 0
for _ in range(1, num + 1):
    if nx < 0 or nx >= x or ny < 0 or ny >= y:
        cnt = (cnt + 1) % 4
    nx += dx[cnt]
    ny += dy[cnt]
print(ny + 1, nx + 1)

'''
훈아 자리 배정하는 곳 인덱스를 뚫어지게 잘 봐봐
오른쪽으로 90도 돌리면
1,1  1,2  1,3
2,1  2,2
3,1  ...
이렇게 이어지잖아
그럼 x, y 받을 때만 반대로 받아주면
x-1, y-1로 바꿔서 그냥 신경 안쓰고 풀 수 있지 않을까?
'''
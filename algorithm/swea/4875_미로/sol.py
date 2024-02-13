import sys
sys.stdin = open('input.txt')

# T = int(input())
#
# for tc in range(1, T+1):
#     num = int(input())
#     lst = [list(map(int, input()))for _ in range(num)] # 이중 리스트로 받기
#     print(lst)
#     dx = [0, 0, -1, 1] # 상 하 좌 우
#     dy = [-1, 1, 0, 0]
#     for y in range(num):
#         for x in range(num):
#             if lst[y][x] == 2:
#                 sy = y
#                 sx = x
#     stack = [(sy, sx)]
#     visited = [[0] * num for _ in range(num)]
#     visited[sy][sx] = 1
#     cnt = 0
#     while stack:
#         sy, sx = stack.pop()
#         if lst[sy][sx] == 3:
#             cnt = 1
#             break
#         for i in range(4):
#             ny = sy + dy[i]
#             nx = sx + dx[i]
#             if 0 <= ny < num and 0 <= nx < num and lst[ny][nx] !=1 and visited[ny][nx] == 0:
#                 stack.append((ny, nx))
#                 visited[ny][nx] = 1
#                 print(stack)
#                 break
#         else:
#             stack.pop()
#     print(stack)
#     print(cnt)

'''
    stack = [(sy, sx)]
    print(stack)
    visited = [[0]*num for _ in range(num)]
    cnt = 0
    while stack:
        v = stack.pop()
        sy, sx = v
        visited[sy][sx] = 1
        if lst[sy][sx] == 3:
            cnt = 1
            break
        for i in range(4):
            ny = sy + dy[i]
            nx = sx + dx[i]
            if 0 <= ny < num and 0 <= nx < num and lst[ny][nx] != 1 and visited[ny][nx] == 0:
                stack.append((ny, nx))
                
    print(stack)
    print(cnt)
'''

T = int(input())

for tc in range(1, T+1):
    num = int(input())
    lst = [list(map(int, input()))for _ in range(num)] # 이중 리스트로 받기
    dx = [0, 0, -1, 1] # 상 하 좌 우
    dy = [-1, 1, 0, 0]
    for y in range(num):
        for x in range(num):
            if lst[y][x] == 2:
                sy = y
                sx = x
    stack = [(sy, sx)]
    # print(stack)
    visited = [[0] * num for _ in range(num)]
    visited[sy][sx] = 1
    cnt = 0
    while stack:
        cy, cx = stack.pop()  # 스택에서 현재 위치를 가져옴
        if lst[cy][cx] == 3:  # 현재 위치가 도착점인지 확인
            cnt = 1
            # print(stack)
            break
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < num and 0 <= nx < num and lst[ny][nx] != 1 and visited[ny][nx] == 0:
                stack.append((ny, nx))
                visited[ny][nx] = 1
                # print(stack)
    print(f'#{tc} {cnt}')
















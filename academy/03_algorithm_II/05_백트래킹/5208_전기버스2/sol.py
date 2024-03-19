# import sys
#
# sys.stdin = open('input.txt')
#

def move(cnt, idx):
    global min_cnt
    if cnt >= min_cnt:
        return
    if idx >= goal:
        if cnt <= min_cnt:
            min_cnt = cnt
            return
    for i in range(1, lst[idx]+1):
        move(cnt + 1, idx + i)


T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    goal = lst.pop(0) - 1
    # print(goal)
    # print(lst)
    min_cnt = 100
    move(-1, 0)
    print(f'#{tc} {min_cnt}')

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    goal = lst.pop(0) - 1
    min_cnt = 100
    stack = [(-1, 0)]  # 스택에 초기값 추가

    while stack:
        cnt, idx = stack.pop()  # 스택에서 값을 꺼냄
        if cnt >= min_cnt:
            continue
        if idx >= goal:
            if cnt <= min_cnt:
                min_cnt = cnt
                continue
        for i in range(1, lst[idx] + 1):
            stack.append((cnt + 1, idx + i))  # 다음 이동 가능한 위치를 스택에 추가

    print(f'#{tc} {min_cnt}')

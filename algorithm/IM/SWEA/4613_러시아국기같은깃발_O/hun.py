import sys

sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     lst = [list(map(str, input())) for _ in range(N)]
#     # print(lst)
#     cnt = lst[0].count('R') + lst[0].count('B') + lst[-1].count('W') + lst[-1].count('B')
#     print(cnt)
#     check_1 = 0
#     check_2 = 0
#     where = []
#     for i in range(1, N - 1):
#         ww = lst[i].count('W')
#         bb = lst[i].count('B')
#         rr = lst[i].count('R')
#         if ww >= bb and check_1 == 0 and check_2 == 0:       # 흰색이냐
#             cnt = cnt + bb + rr
#         elif bb >= rr and check_2 == 0:                      # 파란색이냐
#             cnt = cnt + rr + ww
#             check_1 += 1
#         else:                                               # 빨간색이냐
#             cnt = cnt + ww + bb
#             where.append(i)
#             check_2 += 1
#
#     if check_1 == 0:
#         if len(where) > 0:
#             idx = where.pop()
#             if lst[idx-1].count('B') > lst[idx].count('B'):
#                 cnt = cnt - lst[idx-1].count('B') + lst[idx - 1].count('W')
#             else:
#                 cnt = cnt - lst[idx].count('B') + lst[idx].count('R')
#         else:
#             cnt = cnt - lst[-2].count('B') + lst[-2].count('W')
#     print(cnt)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(input()) for _ in range(N)]
    new_lst = []
    for ccc in lst:
        w = M - ccc.count('W')      # 허연거 바꿀때 몇개
        b = M - ccc.count('B')      # 퍼런거 바꿀때 몇개
        r = M - ccc.count('R')      # 뻘건거 바꿀때 몇개
        new_lst.append([w, b, r])   # 각 줄의 흰, 파, 빨

    answer = 1e9

    print(new_lst)

    for w in range(0, N - 2):           # 흰색오는 경우
        for b in range(1, N - w - 1):   # 파란색 오는 경우
            r = N - w - b - 2           # 빨간색 오는 경우

            cnt = 0
            for i in range(w):
                cnt += new_lst[1:-1][i][0]
            for j in range(w, w + b):
                cnt += new_lst[1:-1][j][1]
            for k in range(w + b, w + b + r):
                cnt += new_lst[1:-1][k][2]

            answer = min(answer, cnt)

    answer += new_lst[0][0] + new_lst[-1][2]
    print(f'#{tc} {answer}')

'''
import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    min_cnt = N*M

    for first_bar in range(1, N-1):
        for second_bar in range(first_bar+1, N):
            cnt = 0
            for i in range(first_bar):
                for j in range(M):
                    if board[i][j] != 'W':
                        cnt += 1
            for i in range(first_bar, second_bar):
                for j in range(M):
                    if board[i][j] != 'B':
                        cnt += 1
            for i in range(second_bar, N):
                for j in range(M):
                    if board[i][j] != 'R':
                        cnt += 1
            if min_cnt > cnt:
                min_cnt = cnt

    print(f'#{test_case} {min_cnt}')
    '''
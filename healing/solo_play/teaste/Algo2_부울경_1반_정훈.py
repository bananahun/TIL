# import sys
#
# sys.stdin = open('algo2_sample_in.txt')

# def shot(i, N, max_num):
#
#     sum_num = 0
#     visited = [0]*N
#     if i == N:
#         new_lst.append(sum_num)
#     if i != N:
#         for j in range(N):
#             sum_num += lst[i][j]
#             visited[j] = 0
#
#         return shot(i + 1, N, max_num)
#     else:
#         new_lst.append(sum_num)
#     visited = [0] * N

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    # 결과 값을 담아줄 빈 리스트 만들기
    new_lst = []
    # 완전 탐색
    for a in range(N):
        for b in range(N):
            for c in range(N):
                # x값이 전부다 다를때 하나씩 넣어주기
                if a != b and c != a and b != c and lst[0][a] >= 0 and lst[1][b] >= 0 and lst[2][c] >= 0:
                    # 모두 더해주기
                    max_num = lst[0][a] + lst[1][b] + lst[2][c]
                    # 새로운 리스트에 넣어주기
                    new_lst.append(max_num)
    # 결과 값 출력
    print(f'#{tc}', max(new_lst))





# import sys
#
# sys.stdin = open('algo1_sample_in.txt')


# 1번 작업 함수
def work_1(lst, i, j):
    for num in range(i, i + j):
        # 인덱스 범위 확인
        if 0 <= num < N and 0 <= num < N:
            lst[num] = abs(lst[num] - 1)
    return lst


# 2번 작업 함수
def work_2(lst, i, j):
    for num in range(i, i + j):
        # 인덱스 범위 확인
        if 0 <= num < N and 0 <= num < N:
            lst[num] = lst[i]


# 3번 작업 함수
def work_3(lst, i, j):
    for num in range(1, j + 1):
        # 인덱스 범위 확인
        if 0 <= i - num < N and 0 <= i + num < N:
            # 두개가 같다면 뒤집는다
            # 다르다면 안뒤집으므로 따로 구현 X
            if lst[i - num] == lst[i + num]:
                lst[i - num] = abs(lst[i - num] - 1)
                lst[i + num] = abs(lst[i + num] - 1)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))  # 흰색 0 검은색 1
    for _ in range(M):
        i, j, w = map(int, input().split())
        # 문제에서 i는 실제 인덱스 번호와 다르므로 맞춰주기 위해 -1
        # 1번 작업일경우
        if w == 1:
            work_1(lst, i - 1, j)
        # 2번 작업일 경우
        elif w == 2:
            work_2(lst, i - 1, j)
        # 3번 작업일 경우
        elif w == 3:
            work_3(lst, i - 1, j)
    # 문제에서 원하는 형태로 출력
    print(f'#{tc}', *lst)

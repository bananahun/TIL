import sys

sys.stdin = open('input.txt')

T = int(input())


def combination(N):
    comb_lst = []
    for a in range(N):
        start_1 = a + 1
        for b in range(start_1, N):
            comb_lst.append((a, b))
    return comb_lst


def change(N):
    comb_lst = combination(N)
    for _ in range(comb_lst):
        pass
# for tc in range(1, T + 1):
#     num, time = map(str, input().split())
#     lst = list(map(int, num))
#     check_lst = lst.sort(reverse=True)
#     print(lst, time)
#     cnt = 0


# while True:
#     new_lst = []
#     for i in range(6):
#         lst[lst.index(max(lst))], lst[0] = lst[0], lst[lst.index(max(lst))]
#         new_lst.append(lst[0])
#
#
#     if cnt == time or lst == check_lst:
#         False

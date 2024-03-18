import sys

sys.stdin = open('16546.txt')


# def triplet(lst, idx):
#     if lst[idx] == lst[idx + 1] == lst[idx + 2]:
#         return True
#
#
# def rrun(lst, idx):
#     if lst[idx] + 2 == lst[idx + 1] + 1 == lst[idx + 2]:
#         return True
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     lst = list(map(int, input()))
#     lst.sort()
#
#     if rrun(lst, 0) and rrun(lst, 3) is True:
#         print(f'#{tc} true')
#     elif rrun(lst, 0) and triplet(lst, 3) is True:
#         print(f'#{tc} true')
#     elif triplet(lst, 0) and rrun(lst, 3) is True:
#         print(f'#{tc} true')
#     elif triplet(lst, 0) and triplet(lst, 3) is True:
#         print(f'#{tc} true')
#     elif lst[0] + 2 == lst[2] + 1 == lst[4] and lst[1] + 2 == lst[3] + 1 == lst[5]:
#         print(f'#{tc} true')
#     else:
#         print(f'#{tc} false')


# def has_triplet(lst, idx):
#     return lst[idx] == lst[idx + 1] == lst[idx + 2]
#
# def has_run(lst, idx):
#     return lst[idx] + 2 == lst[idx + 1] + 1 == lst[idx + 2]
#
# def main():
#     T = int(input())
#
#     for tc in range(1, T + 1):
#         lst = list(map(int, input()))
#         lst.sort()
#
#         if (has_run(lst, 0) and has_run(lst, 3)) or (has_run(lst, 0) and has_triplet(lst, 3)) or \
#            (has_triplet(lst, 0) and has_run(lst, 3)) or (has_triplet(lst, 0) and has_triplet(lst, 3)):
#             print(f'#{tc} true')
#         elif lst[0] + 2 == lst[2] + 1 == lst[4] and lst[1] + 2 == lst[3] + 1 == lst[5]:
#             print(f'#{tc} true')
#         else:
#             print(f'#{tc} false')
#
# if __name__ == "__main__":
#     main()

T = int(input())
for tc in range(T):
    lst = list(map(int, input()))
    new_lst = [0] * 10

    for number in lst:
        new_lst[number] += 1

    baby_gin = 0

    for _ in range(2):
        for i in range(10):
            if new_lst[i] >= 3:
                baby_gin += 1
                new_lst[i] -= 3

        for j in range(8):
            if new_lst[j] > 0 and new_lst[j] == new_lst[j+1] == new_lst[j+2]:
                baby_gin += 1
                new_lst[j] -= 1
                new_lst[j+1] -= 1
                new_lst[j+2] -= 1

    if baby_gin == 2:
        print(f'#{tc+1} true')
    else:
        print(f'#{tc+1} false')




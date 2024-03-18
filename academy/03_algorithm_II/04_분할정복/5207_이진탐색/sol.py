import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline


def binary_search(s, e, x, lst_y, lrlr):
    m = (s + e) // 2
    if x == lst_y[m]:
        return True
    if x < lst_y[m]:
        if lrlr == 0:
            lrlr = 1
            return binary_search(s, m - 1, x, lst_y, lrlr)
        else:
            return False

    elif x > lst_y[m]:
        if lrlr == 1:
            lrlr = 0
            return binary_search(m + 1, e, x, lst_y, lrlr)
        else:
            return False
    return idx


T = int(input())
for tc in range(1, T + 1):
    num_a, num_b = map(int, input().split())
    lst_a = list(map(int, input().split()))
    lst_b = list(map(int, input().split()))
    lst_a.sort()
    result = 0
    s = 0
    e = len(lst_a) - 1
    for b in lst_b:
        if b < lst_a[(0 + len(lst_a) - 1) // 2]:
            check = 0
        else:
            check = 1
        if binary_search(0, len(lst_a) - 1, b, lst_a, check):
            # print(binary_search(0, len(lst_a) - 1, b, lst_a, check))
            result += 1
    print(f'#{tc} {result}')
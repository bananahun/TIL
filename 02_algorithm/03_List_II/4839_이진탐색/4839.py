import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    p, a, b = map(int, input().split())
    lst = list(range(1, p + 1))

    start = 0
    end = p - 1
    temp = []
    for i in [a, b]:

        cnt = 0
        while start <= end:
            middle = int((start + end) / 2)
            cnt += 1
            if lst[middle] == i:
                break
            elif lst[middle] > i:
                end = middle
            else:
                start = middle


        temp.append(cnt)
    print(temp)
    #
    # if temp[0] < temp[1]:
    #     print(f'#{tc} A ')
    # elif temp[0] > temp[1]:
    #     print(f'#{tc} B ')
    # else:
    #     print(f'#{tc} 0')

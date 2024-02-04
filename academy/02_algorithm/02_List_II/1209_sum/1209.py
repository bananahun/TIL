import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    lst = []
    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += arr[i][j]
        lst.append(tmp)
    for j in range(100):
        tmp = 0
        for i in range(100):
            tmp += arr[i][j]
        lst.append(tmp)

    tmp = 0
    for i in range(100):
        tmp += arr[i][i]
    lst.append(tmp)

    tmp = 0
    for i in range(100):
        tmp += arr[99-i][i]
    lst.append(tmp)
    print(f'#{T} {max(lst)} ')




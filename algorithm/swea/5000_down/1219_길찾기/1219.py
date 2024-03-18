import sys

sys.stdin = open('input.txt')

for _ in range(10):
    tc, num = map(int, input().split())
    arr = list(map(int,input().split()))
    lst_1 = []
    lst_2 = []
    for idx in range(len(arr)):
        if idx % 2 == 0:
            lst_1.append(arr[idx])
        else:
            lst_2.append(arr[idx])
    # print(lst_1)
    # print(lst_2)
    











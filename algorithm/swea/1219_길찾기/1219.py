import sys

sys.stdin = open('input (10).txt')

for _ in range(10):
    T, number = input().split()
    # print(T)
    # print(number)
    arr = list(map(int,input().split()))
    print(arr)
    new_arr_1 = [-1]*100
    new_arr_2 = [-1]*100
    for i in range(int(number*2)):
        if i % 2 == 0:
            start = arr[i]
            if new_arr_1[start] == -1:
                new_arr_1[start] == arr[i + 1]
            else:
                new_arr_2[start] == arr[i + 1]
        print(new_arr_1)
        print(new_arr_2)








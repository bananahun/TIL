import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(100)]
    new_list = []
    for i in range(100):
        sum_list = []
        for j in range(100):
            sum_list.append(arr[i][j])
        new_list.append(sum_list)
    print(max(new_list))

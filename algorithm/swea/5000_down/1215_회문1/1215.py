import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    line = int(input())
    arr = [list(map(str,input())) for _ in range(8)]
    count = 0
    for i in range(8):
        for j in range(8):
            new_arr = arr[i][j:j+line]
            if new_arr == new_arr[::-1] and len(new_arr) == line:
                count +=1

    lst = []
    for j in range(8):
        for i in range(8-line+1):
            for k in range(line):
                new_arr = arr[i+k][j]
                lst.append(new_arr)
            if lst == lst[::-1]:

                count += 1
                lst = []
            else:
                lst = []
    print(f'#{tc} {count}')


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    lst = []
    for i in range(0, len(arr)):
        lst.append(arr[i])
        if len(lst) > 1 and lst[-1] == lst[-2]:
            lst.pop()
            lst.pop()

    print(f'#{tc} {len(lst)}')




import sys
sys.stdin = open('input.txt')
from collections import deque

while True:
    try:
        T = int(input())
        lst = list(map(int, input().split()))
        dq = deque(lst)
        cnt = 0
        while cnt == 0:
            for i in range(1, 6):
                a = dq.popleft() - i
                if a > 0:
                    dq.append(a)
                    continue
                elif a <= 0:
                    a = 0
                    dq.append(a)
                    cnt -= 1
                    break
        result = list(dq)
        print(f'#{T}', *result)
    except EOFError:
        break


    # 6 2 2 9 4 1 3 0
    # 9 7 9 5 4 3 8 0
    # 8 7 1 6 4 3 5 0
    # 7 5 8 4 8 1 3 0
    # 3 8 7 4 4 7 4 0
    # 6 7 5 9 6 8 5 0
    # 7 6 8 3 2 5 6 0
    # 9 2 1 7 3 6 3 0
    # 4 7 8 1 2 8 4 0
    # 6 8 9 5 8 5 2 0

import sys
sys.stdin = open('input.txt')

M, N = map(int, input().split())
lst = [list(map(str, input()))for _ in range(M)]
result = 64
for i in range(0, M-7):
    for j in range(0, N-7):
        cnt = 0
        for y in range(i, i+8):
            for x in range(j, j+8):
                if (x+y) % 2 == 0:
                    if lst[y][x] == 'B':
                        cnt += 1
                else:
                    if lst[y][x] == 'W':
                        cnt += 1
        if cnt >= 32:
            cnt = 64 - cnt
        result = min(result, cnt)
       
print(result)
        

        
                
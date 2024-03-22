import sys
sys.stdin = open('input.txt')

def check(x,y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    cnt = 0
    for k in range(4):
        cx = x + dx[k]
        cy = y + dy[k]
        if 0 <= cx < C and 0 <= cy < R:
            if c_lst[cy][cx] == '.':
                cnt += 1
                if cnt == 3 or cnt == 4:
                    c_lst[y][x] = '.'
    

R, C = map(int, input().split())
lst = [list(map(str, input())) for _ in range(R)]
c_lst = lst
# print(lst)
result = 0
for i in range(R):
    for j in range(C):
        if lst[i][j] == 'X':
            check(j, i)
print(lst)
            
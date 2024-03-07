T = int(input())
for tc in range(T):
    k = int(input()) # 몇 층
    n = int(input()) # 몇 호
    room = [list([0]*15)for _ in range(k+1)]
    room[0][0:n+1] = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    for i in range(1, k+1):
        for j in range(1, n+1):
            room[i][j] = sum(room[i - 1][0:j+1])
    print(room[k][n])
'''

a 3a+b
a 2a+b
a a+b a+b+c a+b+c+d
a b c d e f g
'''

import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
for i in range(0, K):
    cnt += lst[i]
    maxx = cnt
for j in range(1, N-K+1):
    cnt = cnt - lst[j-1]
    cnt = cnt + lst[j+K-1]
    maxx = max(maxx, cnt)
print(maxx)
    

    


'''
0 1 2 3 4 5 6 7 8 9
0 1 2 3 
1 2 3 4
.
.
.
4 5 6 7
5 6 7 8
6 7 8 9
'''
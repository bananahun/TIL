import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(input().split())for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr = str(arr[i][j:j + M])
            print(str(reversed(new_arr)))









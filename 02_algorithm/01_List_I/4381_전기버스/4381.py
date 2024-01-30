import sys
sys.stdin=open('input.txt')

T = int(input())
for tc in range(1,T+1):
    K,N,M = map(int,input().split())
    bs_list = list(map(int,input().split()))
    charge = 0
    start = 0
    while start + K < N:
        for stop in range(K,0,-1):
            if start + stop in bs_list:
                start = start + stop
                charge = charge + 1
                break
            elif stop == 1:
                charge = 0
                start = N
    print(f'#{tc} {charge}')

'''    
T = int(input())
for tc in range(1,T+1):
    K,N,M = map(int,input().split())
    bs_list = list(map(int,input().split()))
    charge = 0
    start = 0    
    while start + K < N:
        for stop in range(K,0,-1):
            if start + stop in bs_list:
                start = start + stop
                charge = charge + 1
                break
        else:
            count = 0
            break
    print(f'#{tc} {charge}')
'''
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

'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):

        
    k, n, m  = map(int, input().split())
    charges = list(map(int, input().split()))

    stations = [0] * n

    # 충전기 있는자리 1 넣기
    for charge in charges :
        stations[charge] = 1

    # 그리디 : 매번 최선의 선택하면 최종적으로 최선의 정답
    # 최선의 선택 : 현 버스 위치에서 가장 먼 충전소 가기
    #(단, 다음 장소로 이동해야해서 갈수 있는 충전소 가는게 중요)
        
    # 버스 현재위치 pos
    pos = 0
    # 버스 충전횟수  cnt
    cnt = 0

    # 최선의 선택을 현재버스위치에서 k까지 갔을 때 N위치 넘는 경우(조건 -> while)

    while pos + k < n :
        # k 거리 내에서 가장 먼 충전소 찾아 위치이동
        # pos + K, pos + K-1, pos +k-2 ..., pos+1 탐색 순회
        for nxt in range(pos+k, pos-1, -1):
            # 다음 위치는 nxt
            # 다음 위치 nxt에서 충전소가 있다며 이동
            if stations[nxt] == 1 :
                pos = nxt
                cnt += 1
                break    # 중요!!!
        
        # 이 반복문이 끝나도 충전소 없는 경우(이동하지 않은 경우)
        if nxt == pos + 1:
            cnt = 0
            break

    print(f'#{test_case} {cnt}')





import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):

        
    k, n, m  = map(int, input().split())
    charges = list(map(int, input().split()))

    stations = [0] * n

    # 충전기 있는자리 1 넣기
    for charge in charges :
        stations[charge] = 1

    # 그리디 : 매번 최선의 선택하면 최종적으로 최선의 정답
    # 최선의 선택 : 현 버스 위치에서 가장 먼 충전소 가기
    #(단, 다음 장소로 이동해야해서 갈수 있는 충전소 가는게 중요)
        
    # 버스 현재위치 pos
    pos = 0
    # 버스 충전횟수  cnt
    cnt = 0

    # 최선의 선택을 현재버스위치에서 k까지 갔을 때 N위치 넘는 경우(조건 -> while)

    while pos + k < n :
        # k 거리 내에서 가장 먼 충전소 찾아 위치이동
        # pos + K, pos + K-1, pos +k-2 ..., pos+1 탐색 순회
        for nxt in range(pos+k, pos-1, -1):
            # 다음 위치는 nxt
            # 다음 위치 nxt에서 충전소가 있다며 이동
            if stations[nxt] == 1 :
                pos = nxt
                cnt += 1
                break    # 중요!!!
        
        # 이 반복문이 끝나도 충전소 없는 경우(이동하지 않은 경우)
        else :
            cnt = 0
            break

    print(f'#{test_case} {cnt}')
    '''
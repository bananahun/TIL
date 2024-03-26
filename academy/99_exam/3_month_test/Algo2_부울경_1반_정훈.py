# import sys
#
# sys.stdin = open('algo2_sample_in.txt')

'''
from itertools import combinations

T = int(input())
for tc in range(1, T + 1):
    n, s = map(int, input().split())
    lst = list(map(int, input().split()))
    result = s
    cnt = 0
    for i in range(n, 0, -1):  # 다리를 많이 놔야하니까 위에서 부터 확인
        temp = 0  # 비용
        cnt = 0  # 다리 수
        for j in combinations(lst, i):
            if sum(j) < s:  # 가진 비용보다 작게 들면
                if sum(j) < result:  # 똑같은 다리 갯수지만 비용이 작으면
                    result = sum(j)  # 결과값 갱신
                    cnt = i  # 다리 개수 저장
        if cnt != 0:  # 위에서 부터 확인하니 다리 개수가 나와지면 밑에건 더이상 확인 할 필요 없음
            break  # 종료
    print(f'#{tc}', cnt, result)
    '''


    # import sys
    # sys.stdin = open('algo2_sample_in.txt')
from itertools import combinations

    # 예산을 초과하지 않는 범위에서 최대한 많은 다리
    # 건설할 수 있는 최대 다리 수와 이때의 건설비용 출력
    # 건설할 수 있는 최대 다리 개수가 같은 경우 건설 비용이 적은 쪽 선택

T = int(input())
for test in range(1, T + 1):
    N, V = map(int, input().split())  # N: 섬의 개수, V: 예산
    cost_lst = list(map(int, input().split()))  # 다리 건설 비용 (섬의 개수만큼 받음)
    min_cost = int(1e9)  # 최소 건설 비용 초기값은 일단 큰 값으로 설정
    max_bridge = 0  # 건설 가능한 최대 다리 개수는 일단 작은 값으로 설정
    for i in range(1, N + 1):
        for bridge_comb in combinations(cost_lst, i):  # 1 ~ N개만큼 다리를 건설하는 조합을 만든다
            sum_cost = sum(bridge_comb)  # 해당 조합의 건설 비용
            if sum_cost > V or i < max_bridge:  # 건설 비용이 예산을 넘어가거나, 해당 다리 개수가 max_bridge보다 작다면 continue
                continue
            elif i > max_bridge:
                min_cost = sum_cost
                max_bridge = i
            else:  # 건설할 수 있는 최대 다리 개수가 같은 경우
                min_cost = min(min_cost, sum_cost)  # 건설 비용이 적은 것으로 min_cost 갱신

    print(f'#{test} {max_bridge} {min_cost}')
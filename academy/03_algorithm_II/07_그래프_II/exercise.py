import sys
sys.stdin = open("input.txt")

# 우선순위큐를 활용
from heapq import heappush, heappop


def prim(start):
    pq = []
    MST = [0] * V

    # 최소 비용
    sum_weight = 0

    # 시작점 추가
    #  [기존 BFS] 노드 번호만 관리
    # [PRIM] 가중치가 낮으면 먼저 나와야 한다
    #           1. class 로 만들기
    #           2. (가중치, 노드번호)
    heappush(pq, (0, start)) 

    while pq:
        weight, now = heappop(pq)

        if MST[now]:
            continue

        # 방문 처리
        MST[now] = 1
        sum_weight += weight

        # 갈 수 있는 노드들을 보면서
        for to in range(V):
            # 갈 수 없거나 이미 방문 했다면 pass
            if graph[now][to] == 0 or MST[to]:
                continue
            
            heappush(pq, (graph[now][to], to))
    print(f'최소비용 : {sum_weight}')



V, E = map(int,input().split())
# 인접 행렬로 저장
# - [실습] 인접 리스트로 저장
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    s, e, w = map(int, input().split())
    # [가중치 그래프] 3 -> 4로 가는데 31이라는 비용이 든다.
    # graph[3][4] = 31
    graph[s][e] = w
    # 무방향 그래프
    graph[e][s] = w
    
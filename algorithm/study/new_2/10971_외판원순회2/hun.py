import sys

# 입력 받기
N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

# dp 배열 초기화
dp = [[0] * (1 << N) for _ in range(N)]

# 비트마스크를 사용하여 방문한 도시들을 표시하고, 출발 도시는 0번으로 가정
def tsp(start, visited):
    # 모든 도시를 방문한 경우 출발 도시로 돌아가는 비용 반환
    if visited == (1 << N) - 1:
        return costs[start][0] if costs[start][0] > 0 else float('inf')
    
    # 이미 계산한 값이 있는 경우 반환
    if dp[start][visited] != 0:
        return dp[start][visited]
    
    min_cost = float('inf')
    
    # 다음 방문할 도시들을 탐색하며 최소 비용 계산
    for next_city in range(N):
        if visited & (1 << next_city) == 0 and costs[start][next_city] > 0:
            cost = costs[start][next_city] + tsp(next_city, visited | (1 << next_city))
            min_cost = min(min_cost, cost)
    
    # 계산된 최소 비용을 dp 배열에 저장하고 반환
    dp[start][visited] = min_cost
    return min_cost

# 출발 도시는 0번으로 가정
print(tsp(0, 1))
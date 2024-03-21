import sys
sys.stdin = open('input.txt')

from heapq import *
dr = [(0,1),(1,0),(0,-1),(-1,0)]  # 우, 하, 좌, 상 방향을 나타내는 상대 좌표 리스트

def dijkstra(x, y):
    heap = []
    dist[x][y] = 0  # 시작 지점의 최단 거리를 0으로 설정
    heappush(heap, (0, x, y))  # 시작 지점을 heap에 추가
    while heap:
        weight, x, y = heappop(heap)  # heap에서 가장 가까운 지점을 pop
        for dx, dy in dr:  # 상하좌우 이웃한 지점에 대해 반복
            nx, ny = x + dx, y + dy  # 이웃 지점의 좌표 계산
            if 0 <= nx < N and 0 <= ny < N:  # 이웃 지점이 유효한 범위 내에 있는지 확인
                new_weight = weight + max(0, arr[nx][ny] - arr[x][y]) + 1  # 새로운 지점까지의 거리 계산
                if dist[nx][ny] > new_weight:  # 기존에 저장된 최단 거리보다 더 짧은 거리를 발견한 경우
                    dist[nx][ny] = new_weight  # 최단 거리 갱신
                    heappush(heap, (new_weight, nx, ny))  # 새로운 지점을 heap에 추가

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dist = [[2001] * N for _ in range(N)]
    dijkstra(0, 0)  # 다익스트라 알고리즘 수행
    print(f'#{tc} {dist[-1][-1]}')  
'''
import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

home, road_num = map(int, input().split())
# road = [[] for _ in range(home)]
road = {}
for _ in range(road_num):
    x, y, z = map(int, input().split())
    road[x] = [y,z]
print(road)
result = 0
for _ in range(road_num):
  pass

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  
    distances[start] = 0  
    queue = []
    heapq.heappush(queue, [distances[start], start])  

    while queue:  
        current_distance, current_destination = heapq.heappop(queue)  

        if distances[current_destination] < current_distance:  
            continue
    
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance  
            if distance < distances[new_destination]:  
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])  
        return distances
'''
#간단한 다익스트라 알고리즘 코드
#단계마다 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인(순차탐색)한다.
 
INF = int(1e9) #무한을 의미하는 값으로 10억을 설정
 
#노드의 개수, 간선의 개수를 입력받기
n,m = map(int, input().split())
#시작 노드 번호를 입력 받기
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보를 담를 리스트 만들기
graph = [[] for i in range(n+1)]
#방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False]*(n+1)
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF]*(n+1)
 
#모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    #a노드에서 b노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))
 
#방문하지 않은 노드 중에서 가장 최단거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value=INF
    index = 0 #가장 최단 거리가 짦은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index=i
    return index
 
def dijkstra(start):
    #시작 노드에 대해서 초기화
    distance[start]=0
    visited[start]=True
    for j in graph[start]:
        distance[j[0]]=j[1]
    #시작 노드를 제외한 전체 n-1개의 노드에 대한 반복
    for i in range(n-1):
        #현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        #현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now]+ j[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]]=cost
 
#다익스트라 알고리즘 수행
dijkstra(start)
 
#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    #도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i]==INF:
        print("INFINITY")
    #도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
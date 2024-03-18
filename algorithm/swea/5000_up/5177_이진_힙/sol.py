import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = int(input().split())
    tree = [[0, 0] for _ in range(N + 1)]

    for i in range(0, N):
        if lst[i] ==


'''

V = int(input())
edge = list(map(int,input().split()))
print(edge)
E = len(edge)

## tree[현재 노드 번호][0] => 현재 노드 번호의 왼쪽 자식 노드 번호
tree = [[0,0] for _ in range(V+1)]
for idx in range(E//2):
    # 특정 위치에 값을 할당하는 것.
    if tree[edge[idx*2]][0] == 0: # 왼쪽 자식의 정보가 아직 없다면
        # 왼쪽 자식에 자식 정보 삽입
        tree[edge[idx*2]][0] = edge[idx*2+1]
    else:
        # 왼쪽 자식이 이미 있다면 오른쪽에 자식 정보 삽입
        tree[edge[idx * 2]][1] = edge[idx*2+1]

'''
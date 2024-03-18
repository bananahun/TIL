import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
arr = list(map(int, input().split()))

# print(len(arr))

adj = [[] for _ in range(V + 1)]
for i in range(V+1):
    print(adj[i])
for idx in range(0, E * 2, 2):
    # print(idx, idx+1)
    # print(arr[idx], arr[idx+1])
    from_node = arr[idx]
    to_node = arr[idx+1]
    # 무방향 그래프니까 반대로도 넣기
    adj[from_node].append(to_node)
    adj[to_node].append(from_node)
print(adj)

print(3 + 1e2)
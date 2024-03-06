N, M = map(int, input().split())
lst = list(map(int, input().split()))
result = []
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and j!=k and i!=k:
                aaa = lst[i] + lst[j] + lst[k]
                if aaa <= M:
                    result.append(aaa)
print(max(result))
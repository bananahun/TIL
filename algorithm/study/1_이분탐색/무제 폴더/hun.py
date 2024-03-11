N = int(input())
apt = []
for _ in range(N):
    dist, num = map(int, input().split())
    apt.append((dist, num))
min_num = 10000000000
result = 0
for i in range(N):
    total = 0
    for j in range(N):
        total += abs(apt[i][0] - apt[j][0]) * apt[j][1]
    if total <= min_num:
        min_num = total
        if result <= i+1:
            result = i + 1
print(result)






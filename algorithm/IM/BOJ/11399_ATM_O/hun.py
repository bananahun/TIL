N = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0
for i in range(N):
    cnt += arr[i]*(N-i)
print(cnt)
    
import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N, people = map(int, input().split())
lst = []
for _ in range(N):
    bottle = int(input())
    lst.append(bottle)
start = 1
end = max(lst)
while start <= end:
    mid = (start+end) // 2
    # print(start, end, mid)
    cnt = 0
    for k in lst:
        cnt += k // mid
    if cnt >= people:
        start = mid + 1
    else:
        end = mid - 1
print(start-1)


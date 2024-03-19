import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))
s = max(lst)
e = sum(lst)

while s <= e:
    num_sum = 0
    cnt= 1
    mid = (s+e)//2
    # print(mid)
    for i in lst:
        num_sum += i
        if num_sum > mid:
            cnt += 1
            num_sum = i
    
    if cnt > M:
        s = mid+1
    else:
        e = mid-1
if N == M :
    print(max(lst))
else:
    print(int(s))

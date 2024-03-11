import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.sort()
    result = 0
    for num in A:
        s = 0
        end = m-1
        while s <= end:
            mid = (s+end) // 2
            if num > B[mid]:
                s = mid + 1
            else:
                end = mid - 1
        result = result + s
    print(result)







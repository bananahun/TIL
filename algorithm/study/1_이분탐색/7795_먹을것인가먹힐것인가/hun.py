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

# x,y = map(int,input().split())

# original = y*100//x

# start = 1
# end = x
# result = 1000000001

# while True:
#     middle = (start+end)//2
#     z = (y+middle)*100//(x+middle)
#     if start == end:
#         if end == x:
#             result = -1
#         break
#     if z == original:
#         start = middle + 1
#     elif z > original:
#         result = middle
#         end = middle - 1
# print(result)





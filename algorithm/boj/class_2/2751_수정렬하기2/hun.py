import sys
input = sys.stdin.readline
N = int(input())
# lst = list([False]*2000001)
# for _ in range(N):
#     num = int(input())
#     lst[num] = 1
# for check in range(len(lst)):
#     if lst[check]:
#         if check <= 1000000:
#             print(check)
#         else:
#             print(check-2000001)
lst = []
for _ in range(N):
    num = int(input())
    lst.append(num)
lst.sort()
for a in lst:
    print(a)


import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
# M = int(input())
# lst = [False]*21
# # print(lst)lst
# for _ in range(M):
#     cal = list(map(str, input().split()))
#     if cal[0] == 'add':
#         lst[int(cal[1])] = True
#     elif cal[0] == 'remove':
#         lst[int(cal[1])] = 0
#     elif cal[0] == 'check':
#         if lst[int(cal[1])] is True:
#             print(1)
#         else:
#             print(0)
#     elif cal[0] == 'toggle':
#         if lst[int(cal[1])] is True:
#             lst[int(cal[1])] = False
#         else:
#             lst[int(cal[1])] = True
#     elif cal[0] == 'all':
#         lst = [True]*21
#     elif cal[0] == 'empty':
#         lst = [False]*21

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    temp = sys.stdin.readline().strip().split()

    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()

    else:
        func, x = temp[0], temp[1]
        x = int(x)

        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)



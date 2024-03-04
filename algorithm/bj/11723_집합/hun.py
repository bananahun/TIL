import sys
sys.stdin = open('input.txt')

M = int(input())
lst = [False]*21
# print(lst)lst
for k in range(M):
    cal = list(map(str, input().split()))
    if cal[0] == 'add':
        lst[int(cal[1])] = True
    elif cal[0] == 'remove':
        lst[int(cal[1])] = 0
    elif cal[0] == 'check':
        if lst[int(cal[1])] is True:
            print(1)
        else:
            print(0)
    elif cal[0] == 'toggle':
        if lst[int(cal[1])] is True:
            lst[int(cal[1])] = False
        else:
            lst[int(cal[1])] = True
    elif cal[0] == 'all':
        lst = [True]*21
    elif cal[0] == 'empty':
        lst = [False]*21




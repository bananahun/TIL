n, m, t = map(int, input().split())

arr = [list(input())for _ in range(n)]
print(n, m, t)
print(arr)
lst = []
if t % 2 == 0:
    lst = list([O]*n for _ in range(m))
    print(lst)
elif t % 4 == 1:
    print(arr)
elif t % 4 == 3:
    for n in range(n):
        for m in range(m):
            if arr[n][m] == 'O':
                lst.append((n.m))
            else:
                arr[n][m] = 'O'
    print(arr)



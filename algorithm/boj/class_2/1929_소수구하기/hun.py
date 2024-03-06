import sys

input = sys.stdin.readline

m, n = map(int, input().split())

for k in range(m, n+1):
    if k == 1:
        continue
    for check in range(2, int(k**(0.5))+1):
        if k % check == 0:
            break
    else:
        print(k)

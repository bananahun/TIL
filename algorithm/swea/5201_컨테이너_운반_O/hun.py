import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = []
    for _ in range(N):
        s, e = map(int, input().split())
        lst.append((s, e))
    lst.sort(key=lambda x: (x[1], x[0]))
    # print(lst)
    ss, ee = lst.pop(0)
    stack = [(ss, ee)]
    cnt = 1
    while True:
        if len(lst) == 0:
            break
        ns, ne = stack.pop(0)
        cs, ce = lst.pop(0)
        if ne <= cs:
            ns, ne = cs, ce
            cnt += 1
        stack.append((ns, ne))
    print(f'#{tc}', cnt)
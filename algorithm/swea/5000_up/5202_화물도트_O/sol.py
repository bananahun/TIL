import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # 트럭, 컨테이너
    lst_w = list(map(int, input().split()))
    lst_t = list(map(int, input().split()))
    lst_w.sort()
    lst_t.sort()
    # print(lst_w)
    # print(lst_t)
    total = 0
    for _ in range(N):
        check_w = lst_w.pop()
        for _ in range(M):
            if len(lst_t) > 0:
                check_t = lst_t.pop()
                if check_t >= check_w:
                    total += check_w
                    break
                else:
                    lst_t.append(check_t)
                    break
    print(f'#{tc} {total}')








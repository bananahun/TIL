import sys

sys.stdin = open('input.txt')

def who_win(fst, snd):
    if lst[fst] == lst[snd]:
        return fst
    elif lst[fst] == 1:
        if lst[snd] == 2:
            return snd
        elif lst[snd] == 3:
            return fst
    elif lst[fst] == 2:
        if lst[snd] == 1:
            return fst
        elif lst[snd] == 3:
            return snd
    elif lst[fst] == 3:
        if lst[snd] == 1:
            return snd
        elif lst[snd] == 2:
            return fst
def div(n):
    if


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    # print(lst)
    a = 0
    b = n-1
    print(who_win(a,b))









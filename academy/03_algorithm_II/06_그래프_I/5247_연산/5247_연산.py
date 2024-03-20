import sys
sys.stdin = open('input.txt')

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    new_lst = []
    for _ in range(M):
        a = lst.pop()
        b = lst.pop()
        new_lst.append([a, b])
    print(new_lst)
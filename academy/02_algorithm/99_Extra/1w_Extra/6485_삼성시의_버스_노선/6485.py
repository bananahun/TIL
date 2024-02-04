import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    counts = [0] * 5001
    for _ in range(n):
        a, b = map(int, (input().split()))
    p = int(input())
    for _ in range(p):
        c = int(input())


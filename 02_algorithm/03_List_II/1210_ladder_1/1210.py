import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    ladders = [list(map(int,input().split())) for _ in range(100)]
    for a in range(0, 100):
        if ladders[99][a] == 2:
            start_y = a
            start = ladders[99]


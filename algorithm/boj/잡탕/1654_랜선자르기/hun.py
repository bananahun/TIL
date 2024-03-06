import sys
sys.stdin = open('input.txt')


def check(num):
    while True:
        answer = []
        result = 0
        start = 0
        end = lst[0]
        for i in range(N):
            result += lst[i] // num
        if result < K:
            num = result +
        elif result >= K:
            num = result +


N, K = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()




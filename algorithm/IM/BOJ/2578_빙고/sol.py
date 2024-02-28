import sys

sys.stdin = open('input.txt')

# def bingo(pan):
#     for x in range():

pan = [list(map(int, input().split())) for _ in range(5)]
answer = []
for _ in range(5):
    a1, a2, a3, a4, a5 = map(int, input().split())
    answer.append(a1)
    answer.append(a2)
    answer.append(a3)
    answer.append(a4)
    answer.append(a5)



import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
check = list([False]*10001)
for _ in range(N):
    num = int(input())
    check[num] += 1
for num in range(len(check)):
    if check[num]:
        for _ in range(check[num]):
            print(num)


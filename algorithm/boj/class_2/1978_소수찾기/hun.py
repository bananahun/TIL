import sys
sys.stdin = open('input.txt')

N = int(input())
cnt = N
lst = list(map(int, input().split()))
for num in lst:
    if num == 1:
        cnt -= 1
    else:
        for k in range(2, num):
            if num % k == 0:
                cnt -= 1
                break
print(cnt)

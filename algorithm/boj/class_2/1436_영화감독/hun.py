N = int(input())
cnt = 0
for num in range(666, 10000000):
    num = str(num)
    if '666' in num:
        cnt += 1
        if cnt == N:
            print(num)
            break
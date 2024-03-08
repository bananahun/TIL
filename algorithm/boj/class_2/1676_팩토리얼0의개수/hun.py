import math
num = math.factorial(int(input()))
cnt = 0
for check in str(num)[::-1]:
    if check == '0':
        cnt += 1
    else:
        print(cnt)
        break

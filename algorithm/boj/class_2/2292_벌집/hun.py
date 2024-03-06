N = int(input())
'''
1, 1+6, 1+6+12, 
'''
result = 1
cnt = 1
while result < N:
    for k in range(100000):
        result = result + 6 * cnt
        cnt += 1
        break
print(cnt)


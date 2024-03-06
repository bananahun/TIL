N = int(input())

lst = list(map(str, input()))

# print(lst)

# print((ord('a')))
result = 0
for k in range(N):
    result += (ord(lst[k]) - 96) * 31**k
print(result % 1234567891)

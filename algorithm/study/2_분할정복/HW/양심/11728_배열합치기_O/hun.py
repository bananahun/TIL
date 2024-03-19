a, b = map(int, input().split())
lst_a = list(map(int,input().split()))
lst_b = list(map(int,input().split()))
result = lst_a + lst_b
result.sort()
print(*result)
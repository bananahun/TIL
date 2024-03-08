import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
lst = list([] for _ in range(201))
# print(lst)
for _ in range(N):
    age, name = map(str, input().split())
    lst[int(age)].append(name)
# print(lst)
for a in range(201):
    if lst[a]:
        if len(lst[a]) == 1:
            print(a, *lst[a])
        else:
            for k in range(len(lst[a])):
                print(a, lst[a][k])

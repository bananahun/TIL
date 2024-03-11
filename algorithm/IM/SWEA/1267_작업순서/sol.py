import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
lst = list(map(int, input().split()))
lst_s = [0]*(V+1)
lst_e = [0]*(V+1)
for K in range(E):
    lst_s.append(K*2)
    lst_e.append(K*2 + 1)
print(lst_s)
print(lst_e)



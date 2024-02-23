import sys
sys.stdin = open('input.txt')

number = int(input())
lst = []
for n in range(number):
    l, h = map(int, input().split())
    lst.append((l, h))
    lst.sort()
    lst_l = []
    lst_h = []
    for l, h in lst:
        lst_l.append(l)
        lst_h.append(h)
print(lst_l)
print(lst_h)
for i in lst_l:




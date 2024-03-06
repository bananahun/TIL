import sys
sys.stdin = open('input.txt')

N = int(input())
lst_2 = []
for _ in range(N):
    word = input()
    lst_2.append(word)
lst_2.sort()
new_lst = set(lst_2)
new_lst = list(new_lst)
new_lst.sort()
new_lst.sort(key=lambda x: (len(x), x))
for i in range(len(new_lst)):
    print(new_lst[i])

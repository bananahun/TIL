# import sys
# sys.stdin = open('input.txt')

lst = []
for _ in range(9):
    key = int(input())
    lst.append(key)
for num_1 in range(9):
    for num_2 in range(9):
        if len(lst) == 9:
            if num_1 != num_2 and sum(lst) - lst[num_1] - lst[num_2] == 100:
                lst.remove(lst[num_1])
                lst.remove(lst[num_2])
        else:
            pass
lst.sort()
for num in lst:
    print(num)
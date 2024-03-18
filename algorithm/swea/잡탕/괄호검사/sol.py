import sys

sys.stdin = open('input.txt')


# def push(n):
#     global top
#     top += 1
#     if top == size:
#         print('overflow!')
#     else:
#         stack[top] = n
#
#
# def pop():
#     if len(stack) == 0:
#         return
#     else:
#         return stack.pop()
T = int(input())
for tc in range(T):
    arr = input()
    lst = [0] * len(arr)
    for i in range(len(arr)):
        if arr[i] == '(':
            lst.append('(')
        elif arr[i] == ')':
            lst.pop()

    if lst[-1] == 0 and len(lst) == len(arr):
        print('True')
    else:
        print('False')





# T = int(input())
# for tc in range(T):
#     arr = input()
#     lst = []
#     for i in range(len(arr)):
#         if arr[i] == '(':
#             lst.append('(')
#         elif arr[i] == ')':
#             if lst:
#                 lst.pop()
#     if lst == []:
#         print('True')
#     else:
#         print('False')


class Stack:

import sys
sys.stdin = open('input.txt')

# T = int(input())
#
# for tc in range(1, T+1):
#     lst = list(input().split())
#     lst.pop()
#     stack = []
#     for i in range(len(lst)):
#         stack.append(lst[i])
#         if lst[i] == '-':
#             try:
#                 stack.pop()
#                 a = int(stack.pop())
#                 b = int(stack.pop())
#                 stack.append(b-a)
#             except IndexError:
#                 break
#         elif lst[i] == '+':
#             try:
#                 stack.pop()
#                 a = int(stack.pop())
#                 b = int(stack.pop())
#                 stack.append(b+a)
#             except IndexError:
#                 break
#         elif lst[i] == '*':
#             try:
#                 stack.pop()
#                 a = int(stack.pop())
#                 b = int((stack.pop()))
#                 stack.append(b*a)
#             except IndexError:
#                 break
#         elif lst[i] == '/':
#             try:
#                 lst.pop()
#                 a = int((stack.pop()))
#                 b = int((stack.pop()))
#                 stack.append(b/a)
#             except IndexError:
#                 break
#     if stack:
#         print(f'#{tc} {stack[-1]}')
#     else:
#         print(f'#{tc} error')

T = int(input())

for tc in range(1, T+1):
    lst = list(input().split())
    lst.pop()
    stack = []
    for i in range(len(lst)):
        stack.append(lst[i])
        if lst[i] == '-':
            try:
                stack.pop()
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b-a)
            except IndexError or TypeError:
                break
        elif lst[i] == '+':
            try:
                stack.pop()
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b+a)
            except IndexError or TypeError:
                break
        elif lst[i] == '*':
            try:
                stack.pop()
                a = int(stack.pop())
                b = int((stack.pop()))
                stack.append(b*a)
            except IndexError or TypeError:
                break
        elif lst[i] == '/':
            try:
                stack.pop()
                a = int((stack.pop()))
                b = int((stack.pop()))
                stack.append(b/a)
            except IndexError or TypeError:
                break
    if len(stack) == 1:
        print(f'#{tc} {int(stack[-1])}')
    else:
        print(f'#{tc} error')

# T = int(input())
#
# for tc in range(1, T+1):
#     lst = list(input().split())
#     lst.pop()
#     stack = []
#     try:
#         for i in range(len(lst)):
#             stack.append(lst[i])
#             if lst[i] == '-':
#                 stack.pop()
#                 a = int(stack.pop())
#                 b = int(stack.pop())
#                 stack.append(b-a)
#
#             elif lst[i] == '+':
#                 stack.pop()
#                 a = int(stack.pop())
#                 b = int(stack.pop())
#                 stack.append(b+a)
#
#             elif lst[i] == '*':
#                 stack.pop()
#                 a = int(stack.pop())
#                 b = int((stack.pop()))
#                 stack.append(b*a)
#
#             elif lst[i] == '/':
#                 stack.pop()
#                 a = int((stack.pop()))
#                 b = int((stack.pop()))
#                 stack.append(b/a)
#     except IndexError or TypeError:
#         pass
#
#     if len(stack) == 1:
#         print(f'#{tc} {stack[-1]}')
#     elif len(stack) != 1:
#         print(f'#{tc} error')
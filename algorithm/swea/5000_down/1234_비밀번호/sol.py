import sys
sys.stdin = open('input.txt')

# class Stack:
#     # stack을 생성 할 때 필요한 값이 있는데,
#     # stack의 크기를 지정해야한다.
#     def __init__(self, size):
#         self.size = size
#         # 자료구조 stack을 list를 활용해서 구현
#         self.data = [None] * size   # 값이 없음을 나타내는 None
#         self.top = -1   # 초기 값이 없으므로, top의 위치는 -1
#
#     def push(self, item):     # stack에 값 삽입 -> 삽입할 대상 item을 인자로 받는다.
#         # 받아온 item을 내 data에 top 번째 위치에 삽입한다.
#         self.top += 1      # top위치 1 증가
#         self.data[self.top] = item
#
#     def get(self):      # top번째 있는 요소를 출력할 수 있는 방법
#         return self.data[self.top]
#
#     def __str__(self):  # instance print했을 때, stack안의 data를 바로 출력
#         return f'{self.data}'
#
#     def pop(self):
#         # top_value = self.data[self.top]
#         # self.data[self.top] = None
#         self.top -= 1
#         # return top_value
#         return self.data[self.top + 1]
#
#
# for tc in range(1,11):
#     n, arr = input().split()
#     stack = Stack(int(n))
#     for m in range(int(n)):
#         print(stack.get())
#         if stack.get() == arr[m]:
#             stack.pop()
#             continue
#         else:
#             stack.push(arr[m])
#             continue
#     print(stack)


'''
stack 정의 안하고 내가 그냥 푼거
for tc in range(1, 11):
    n, arr = input().split()
    lst = []
    for i in range(0, len(arr)):
        lst.append(arr[i])
        if len(lst) > 1 and lst[-1] == lst[-2]:
            lst.pop()
            lst.pop()

    print(f'#{tc} ' + ''.join(lst))
'''
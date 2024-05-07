import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

# n = int(input())
# dq_in = deque()
# dq_out = deque()
#
# for _ in range(n):
#     dq_in.append(input())
# for _ in range(n):
#     dq_out.append(input())
#
#
# def check_func(lst_in, lst_out):
#     global cnt
#     check = lst_in.popleft()
#
#     while True:
#
#         if not lst_out:
#             break
#
#         if check not in lst_out:
#             break
#         elif check != lst_out[0]:
#             lst_out.popleft()
#             cnt += 1
#         else:
#             lst_out.popleft()
#             break
#
#
# cnt = 0
# check_func(dq_in, dq_out)

#입력
# n = int(input())
# in_list = []
# out_list = []
# # 들어온 순서
# for _ in range(n):
#     in_list.append(input())
# # 나간 순서
# for _ in range(n):
#     out_list.append(input())
#
# # 유죄 차량
# guilty_list =[]
# # 들어온 차량 리스트 인덱스
# right = 0
# # 나간 차량 인덱스
# left = 0
# while right < n and left <n:
#     # 만약 유죄차량 번호이면 해당 인데스를 스킵
#     if in_list[right] in guilty_list:
#         right+=1
#         continue
#     # 만약 나간차량 순서와 들어간 차량 순서가 맞지 않으면 유죄차량으로 지정
#     if in_list[right] !=  out_list[left]:
#         guilty_list.append(out_list[left])
#         left+=1
#         continue
#     right+=1
#     left+=1
# print(len(guilty_list))

n = int(input())


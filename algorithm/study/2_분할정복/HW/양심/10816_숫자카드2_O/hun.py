## 이진탐색

# import sys
# sys.stdin = open('input.txt')
# input_ = sys.stdin.readline
#
# def binary_search(cards, target):
#     cnt = 0
#     s, e = 0, len(cards) - 1
#
#     while s <= e:
#         m = (s + e) // 2
#         if cards[m] == target:
#             cnt += 1
#             i, j = 1, 1
#             while m - i >= s and cards[m - i] == target:
#                 i += 1
#             while m + j <= e and cards[m + j] == target:
#                 j += 1
#             return i + j - 1
#         elif cards[m] < target:
#             s = m + 1
#         else:
#             e = m - 1
#
#     return cnt
#
# nn = int(input_())
# N = sorted(list(map(int, input_().split())))
# mm = int(input_())
# M = list(map(int, input_().split()))
#
# for mmm in M:
#     print(binary_search(N, mmm), end=' ')

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())    # 가지고 있는 숫자 카드 개수
n_lst = list(map(int, input().split()))
M = int(input())    # 주어진 숫자카드 개수
m_lst = list(map(int, input().split()))

cnt_dict = {}
result = []

for i in m_lst:
    cnt_dict[i] = 0

for num in n_lst:
    if num in cnt_dict:
        cnt_dict[num] += 1

for num in m_lst:
    result.append(cnt_dict[num])

print(*result)


# def binary_search(arr, target, cnt_idx):
#     global cnt_list
#     start = 0
#     end = len(arr) - 1
#     while start <= end :
#         mid = (start + end) // 2
#         if arr[mid] == target:  # 찾았으면
#             cnt_list[cnt_idx] += 1
#             arr.remove(arr[mid])
#             binary_search(n_list, m_list[0], cnt_idx + 1)
#             return
#         elif arr[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return
#
#
# N = int(input())    # 가지고 있는 숫자 카드 개수
# n_list = list(map(int, input().split()))
# n_list.sort()
# M = int(input())    # 주어진 숫자카드 개수
# m_list = list(map(int, input().split()))
# cnt_list = [0] * M
# while n_list:
#     binary_search(n_list, m_list[0], 0)
#     # 중복되는 값은 어떻게 처리해줄 건지!
# print(*cnt_list)



import sys
input = sys.stdin.readline

N = int(input())    # 가지고 있는 숫자 카드 개수
n_list = list(map(int, input().split()))    # 여긴 중복된 숫자 카드가 있음
M = int(input())    # 주어진 숫자카드 개수
m_list = list(map(int, input().split()))

cnt_dict = {num: 0 for num in m_list}   # 컴프리헨션 함 써봄ㅎ
result = []

for key in n_list:      # 내가 갖고 있는 숫자카드 순회하면서
    if key in m_list:       # 혹시 이거 거기도 있니?
        cnt_dict[key] += 1  # 있으면 value값 올려주렴

for i in m_list:
    result.append(cnt_dict[i])
# print(*cnt_dict.values())
print(*result)
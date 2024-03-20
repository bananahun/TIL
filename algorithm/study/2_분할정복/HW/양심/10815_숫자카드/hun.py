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
        cnt_dict[num] = 1

for num in m_lst:
    result.append(cnt_dict[num])

print(*result)
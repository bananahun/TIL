# 10 진수를 n 진수로
'''
def change(num, n):
    result = ''
    while num > 0:
        result += str(num%n)
        num = num // n
    return result[::-1]

a = int(input('진수 입력'))
b = int(input('숫자 입력')) 
print(change(b,a))
'''

# 2진수에서 10진수로
'''
N = str(input())
result = 0
cnt = 0
for i in N[::-1]:
    if i == '1':
        result += 2**cnt
    cnt += 1
print(result)
'''



# 10에서 16
'''
def check(number_10):
    check_str = '0123456789abcdef'
    number_16 =  ''
    while number_10 > 0:
        number_16 += str(check_str[number_10 % 16])
        number_10 = number_10 // 16
    return number_16[::-1]
num = int(input())
print(hex(num)[2:])
print(check(num))
'''




'''
import sys
sys.stdin = open('input.txt')

def change(num):
    result = ''
    while num > 0:
        result += str(num%2)
        num = num // 2
    return result[::-1]


# check_str = '0123456789abcdef'
T = int(input())
for tc in range(1, T+1):
    length, strr = input().split()
    # print(str)
    num_10 = int(strr, 16)
    need_0 = 4*int(length) - len(change(num_10))
    # print(change(num_10))
    # print(change(num_10))
    # print(num_10)

    print(f'#{tc}','0'*need_0 + change(int(num_10)))
'''


# 장훈이의 선반
'''
import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, check = map(int, input().split())
    n_lst = list(map(int, input().split()))
    result = int(1e9)
    for i in range(1<<N):
        tem = 0
        for j in range(N):
            if i & (1<<j):
                tem += n_lst[j]
                if tem >= check and check >= result:
                    break
        if tem >= check:
            result = min(result,tem)
    print(f'#{tc} {result-check}')
'''

import sys
from itertools import combinations

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, check = map(int, input().split())
    n_lst = list(map(int, input().split()))
    result = int(1e9)
    
    for i in range(1, N+1):
        for j in combinations(n_lst, i):
            if sum(j) >= check:
                result = min(result, sum(j))
    
    print(f'#{tc} {result-check}')



'''
'''


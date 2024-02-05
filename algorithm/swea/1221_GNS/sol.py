import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    a, b = input().split()
    lst = input().split()

    word = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}

    print(f'#{tc}')
    print(*sorted(lst, key=lambda x: word[x]))











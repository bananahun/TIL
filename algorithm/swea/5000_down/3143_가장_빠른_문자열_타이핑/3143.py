import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    A,B = input().split()
    count = A.count(B)
    count = count + len(A.replace(B,''))
    print(f'#{tc} {count}')



import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = []
    for _ in range(M):
        a, b = map(int, input().split())
        tree.append([a, b])
    print(tree)


'''
          
'''

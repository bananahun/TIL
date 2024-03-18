import sys
sys.stdin = open('input.txt')
open = sys.stdin.readline

num = int(input())
lst = [list(map(int, input().split())) for _ in range(num)]
visited = [[False]*num for _ in range(num)]




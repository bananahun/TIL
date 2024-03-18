import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

a, b = map(int, input().split())
lst_a = list(map(int, input().split()))
lst_b = list(map(int, input().split()))
print(lst_a)
print(lst_b)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
tree = {}
for _ in range(N):
    parent, left, right = input().split()
    tree[parent] = [left, right]

# print(tree)

def pre_order(root):
    if root != '.':
        print(root, end='')
        pre_order(tree[root][0])
        pre_order(tree[root][1])
pre_order('A')
print('')
def mid_order(root):
    if root != '.':
        mid_order(tree[root][0])
        print(root, end='')
        mid_order(tree[root][1])
mid_order('A')
print('')
def huwe_order(root):
    if root != '.':
        huwe_order(tree[root][0])
        huwe_order(tree[root][1])
        print(root, end='')
huwe_order('A')
import sys
from collections import deque

sys.stdin = open('input.txt')


def inorder(tree, start):
    result = []

    left = start * 2
    right = start * 2 + 1

    if left < len(tree):
        inorder(tree, left)

    result.append(tree[start])

    if right < len(tree):
        inorder(tree, right)

    return result


for tc in range(1, 11):
    N = int(input())
    tree = [0 for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]
    for _ in range(N):
        info = list(map(str, input().split()))
        node = int(info[0])
        word = info[1]
        tree[node] = word
    print(tree)
    print(inorder(1, N))

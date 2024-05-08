'''
import sys
input = sys.stdin.readline

n = int(input())
lst = input()


def calculate(num1, cal, num2):
    if cal == '+':
        return num1 + num2
    if cal == '-':
        return num1 - num2
    if cal == '*':
        return num1 * num2

result = -1e9

def dfs(idx, value):
    global result
    if idx == n - 1:
        result = max(result, value)    
        return result
    if idx + 2 < n:
        dfs(idx + 2, calculate(value, lst[idx + 1], int(lst[idx + 2])))
    if idx + 4 < n:
        dfs(idx + 4, calculate(value, lst[idx + 1], calculate(int(lst[idx + 2]), lst[idx + 3], int(lst[idx + 4]))))

print(dfs(0, int(lst[0])))

'''

import sys

n = int(input())
arr = input()
result = -int(1e9)

def calculate(num1, oper, num2):
    if oper == '+':
        return num1 + num2
    if oper == '-':
        return num1 - num2
    if oper == '*':
        return num1 * num2

def dfs(idx, value):
    global result

    if idx >= n:
        result = max(result, value)
        return

    if idx + 2 < n:
        dfs(idx + 2, calculate(value, arr[idx + 1], int(arr[idx + 2])))

    if idx + 4 < n:
        dfs(idx + 4, calculate(value, arr[idx + 1], calculate(int(arr[idx + 2]), arr[idx + 3], int(arr[idx + 4]))))

dfs(0, int(arr[0]))
print(result)
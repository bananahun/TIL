import sys
input = sys.stdin.readline

n = int(input())
s = input()
result = -1000000


def calculate(num1, cal, num2):
    if cal == '+':
        return num1 + num2
    if cal == '-':
        return num1 - num2
    if cal == '*':
        return num1 * num2


def dfs(idx, value):
    global result

    if idx == n - 1:
        result = max(result, value);
        return

    if idx + 2 < n:
        dfs(idx + 2, calculate(value, s[idx + 1], int(s[idx + 2])))

    if idx + 4 < n:
        dfs(idx + 4, calculate(value, s[idx + 1], calculate(int(s[idx + 2]), s[idx + 3], int(s[idx + 4]))))


dfs(0, int(s[0]))
print(result)

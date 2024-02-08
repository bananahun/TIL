import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = list([]for _ in range(n))

    for i in range(0, n):
        for j in range(0, i+1):
            if i == 0 or j == 0 or j == i:
                lst[i].append(1)
            else:
                lst[i].append(lst[i-1][j-1] + lst[i-1][j])

    print(f'#{tc}')
    for k in lst[0:]:
        print(*k)



'''
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def ncr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def pascal(n):
    for i in range(1, n+1):
        for j in i:
'''



'''
[[1]]   1
[[1], [1]]  1c0 +1c1
[[1], [2], [1]] 2c0 + 2c1 + 2c2
[[1], [3], [3], [1]]
[[1], [4], [6], [4], [1]]
[[1], [5], [10], [10], [5], [1]]
[[1], [6], [15], [20], [15], [6], [1]]
[[1], [7], [21], [35], [35], [21], [7], [1]]
[[], [], [], [], [], [], [28], [8], [1]]
[[], [], [], [], [], [], [], [], [], []]
'''

'''
5

[1] #1 arr[0]
[1, 1] #2 arr[1]
[1 2 1] #3 arr[2]
[1 3 3 1] #4 arr[3]
[1 4 6 4 1 #5 arr[4]
1 5 10 10 5 1 #6 arr[5]
1 6 15 20 15 6 1 #7 arr[6]
1 7 21 35 35 21 7 1 # 8 arr[7]

가면 갈수록 리스트의 길이가 1씩 증가한다. 
스택??
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

lst = 
arr = [1] for _ in range(T)
def pas(T):
    for i in range(T):
        for j in range(i)
           
'''


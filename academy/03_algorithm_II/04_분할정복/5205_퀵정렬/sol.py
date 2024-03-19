import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

def quick(arr):
    if len(arr) <= 1:  
        return arr
    pivot = arr[len(arr) // 2]  # 피벗 선택
    less, equal, greater = [], [], []  # 작은거, 같은거, 큰거 만들기
    for num in arr:
        if num < pivot:  # 현재 값이 피벗보다 작으면 less 리스트에 추가합니다.
            less.append(num)
        elif num == pivot:  # 현재 값이 피벗과 같으면 equal 리스트에 추가합니다.
            equal.append(num)
        elif num > pivot:  # 현재 값이 피벗보다 크면 greater 리스트에 추가합니다.
            greater.append(num)
    # 돌려
    return quick(less) + equal + quick(greater)

for tc in range(1, int(input()) + 1):
    N = int(input()) 
    arr = list(map(int, input().split()))  
    print(f'#{tc} {quick(arr)[N // 2]}')  
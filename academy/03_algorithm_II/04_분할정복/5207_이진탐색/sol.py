import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline


def binary_search(s, e, x, lst_y, lrlr):
    m = (s + e) // 2  # 리스트의 중간 인덱스
    if x == lst_y[m]:  # 찾으려는 값(x)이 중간 값(lst_y[m])과 일치하면 True
        return True  
    if x < lst_y[m]:  # 왼쪽을 탐색하려면
        if lrlr == 0:  # 오른쪽에서 왔어야지
            lrlr = 1 
            return binary_search(s, m - 1, x, lst_y, lrlr)  # 왼쪽 부분 탐색 ㄱ
        else:  # 왼쪽에서 왔다면
            return False  
    elif x > lst_y[m]:  # 오른쪽을 탐색하려면
        if lrlr == 1:  # 왼쪽에서 왔어야지
            lrlr = 0  
            return binary_search(m + 1, e, x, lst_y, lrlr)  # 오른쪽 부분 탐색 ㄱ
        else:  # 오른쪽에서 왔다면
            return False  


T = int(input())  
for tc in range(1, T + 1):  
    num_a, num_b = map(int, input().split())  
    lst_a = list(map(int, input().split())) 
    lst_b = list(map(int, input().split()))  
    lst_a.sort()  # 리스트 A만 정렬(이진탐색은 정렬이 되어 있어야죠)
    result = 0  
    s = 0  # start 인덱스를 설정합니다.
    e = len(lst_a) - 1  # end 인덱스를 설정합니다.
    for b in lst_b:  # b라는 값을 lst_a에서 찾습니다.
        if b < lst_a[(0 + len(lst_a) - 1) // 2]:  # 리스트 B의 요소가 리스트 A의 중간 값보다 작은 경우
            check = 0  # 왼쪽으로 가야제
        else:  
            check = 1  # 오른쪽으로 가야제
        if binary_search(0, len(lst_a) - 1, b, lst_a, check):  # 함수가 True 라면
            result += 1  # 결과를 1 증가시킵니다.
    print(f'#{tc} {result}')  

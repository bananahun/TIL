import sys

sys.stdin = open('input.txt')  # 표준 입력을 파일로 변경하여 입력을 받습니다.

def dfs(product):
    global total, Sum

    if product == N:
        if total > Sum:  # 최솟값 갱신
            total = Sum  
        return

    if total <= Sum:  # 이미 넘어가면 더이상 확인 하지 마십쇼
        return

    for i in range(N):  # 모든 제품에 대해 반복합니다.
        if visited[i] == 0:  # 아직 선택되지 않은 제품이라면,
            visited[i] = 1  # 제품 체크
            Sum += lst[product][i]  # 비용 더하기
            dfs(product + 1)  # 다음 제품으로 탐색을 진행합니다.
            visited[i] = 0  # 제품 체크 풀기
            Sum -= lst[product][i]  # 비용 빼기

T = int(input())  

for test_case in range(1, T + 1): 
    N = int(input())  
    lst = [list(map(int, input().split())) for _ in range(N)]  
    visited = [0] * N  
    Sum = 0 
    total = 999999999  # 최소 비용을 저장하는 변수를 초기화합니다.

    dfs(0)
    print(f'#{test_case} {total}') 

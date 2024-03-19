# 백트래킹
# 완전 탐색 + 가지 치기
# 가능성이 없는(볼 필요 없는) 경우의 수를 제거하는 기법

# 중복된 순열
# 1 ~ 3 까지 숫자 배열이 있을 때
# 111, 112, 113, 121, 122, 123 ... 332, 333

arr = [i for i in range(1, 4)]
path = [0] * 3

def dfs(level):
    # 기저 조건
    # 이 문제에서는 3개를 뽑았을 때 까지 반복
    if level == 3:
        return

    # 들어가기 전
    # 다음 재귀 호출
    #   - 다음에 갈 수 있는 곳들은 어디인가?
    #   - 이 문제에서는 1, 2, 3 세가지(arr길이 만큼) 경우의 수가 존재
    path[level] = arr[0]
    dfs(level + 1)
    path[level] = arr[1]
    dfs(level + 1)
    path[level] = arr[2]
    dfs(level + 1)

    print(*path)    
    # 갔다와서 할 로직


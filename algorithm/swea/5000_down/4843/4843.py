import sys

sys.stdin = open('input.txt')
# 테스트 케이스의 개수를 입력받음
T = int(input())

# 각 테스트 케이스에 대한 반복문
for tc in range(1, T + 1):
    # 리스트의 길이를 입력받음
    number = int(input())

    # 리스트를 입력받음
    lst = list(map(int, input().split()))

    # 선택 정렬 알고리즘 수행
    for i in range(10):
        idx = i
        # 홀수 번째 인덱스일 때
        if idx % 2 == 1:
            # 현재 인덱스 이후의 원소들과 비교하여 최솟값을 가지는 원소의 인덱스를 찾음
            for k in range(i + 1, number):
                if lst[idx] > lst[k]:
                    idx = k
        else:
            # 짝수 번째 인덱스일 때
            # 현재 인덱스 이후의 원소들과 비교하여 최댓값을 가지는 원소의 인덱스를 찾음
            for k in range(i + 1, number):
                if lst[idx] < lst[k]:
                    idx = k
        # 최솟값 또는 최댓값을 찾은 후 현재 인덱스와 교환
        lst[i], lst[idx] = lst[idx], lst[i]

    # 결과 출력
    print(f'#{tc}', *lst[0:10])
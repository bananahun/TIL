import sys
sys.stdin = open('input.txt')

T = int(input())  # 테스트 케이스의 개수를 입력 받음
for tc in range(1, T + 1):  # 각 테스트 케이스에 대해 반복
    N, M = map(int, input().split())  # 행과 열의 개수를 입력 받음
    arr = [list(map(str, input())) for _ in range(N)]  # 문자열을 2차원 배열로 입력 받음
    # print(arr)
    for j in range(N):  # 각 행에 대해 반복
        for i in range(0, N - M + 1):  # 각 행의 부분 문자열에 대해 반복
            new_arr = arr[j][i:i + M]  # 부분 문자열 생성
            if new_arr == new_arr[::-1]:  # 부분 문자열이 회문인지 확인
                print(f'#{tc} ' + ''.join(new_arr))  # 회문인 경우 출력

    lst = []  # 열에 대한 부분 문자열을 저장할 리스트 초기화
    for j in range(N):  # 각 열에 대해 반복
        for i in range(0, N - M + 1):  # 각 열의 부분 문자열에 대해 반복
            for k in range(M):  # 부분 문자열을 만들기 위해 행을 이동하면서 문자 추가
                lst.append(arr[i + k][j])  # 부분 문자열 생성
            # print(lst)
            if lst == lst[::-1]:  # 부분 문자열이 회문인지 확인
                print(f'#{tc} ' + ''.join(lst))  # 회문인 경우 출력
            else:
                lst = []  # 부분 문자열 초기화



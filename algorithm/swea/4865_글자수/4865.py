import sys
sys.stdin = open('input.txt')

T = int(input())  # 테스트 케이스의 개수를 입력 받음
for tc in range(1, T + 1):  # 각 테스트 케이스에 대해 반복
    arr_1 = input()  # 첫 번째 문자열을 입력 받음
    arr_2 = list(input())  # 두 번째 문자열을 입력 받고, 리스트로 변환
    new_arr_1 = list(set(arr_1))  # 첫 번째 문자열의 중복을 제거한 문자 리스트 생성
    lst = []  # 각 문자의 개수를 저장할 리스트 초기화
    for string_new_arr_1 in new_arr_1:  # 중복을 제거한 문자 리스트를 순회
        cnt = 0  # 각 문자의 개수를 세기 위한 카운터 초기화
        for string_arr_2 in arr_2:  # 두 번째 문자열을 순회
            if string_new_arr_1 == string_arr_2:  # 첫 번째 문자열의 문자가 두 번째 문자열에 존재하는 경우
                cnt += 1  # 개수 카운트 증가
        lst.append(cnt)  # 개수를 리스트에 추가
    print(f'#{tc} {max(lst)}')  # 각 테스트 케이스마다 가장 많이 등장한 문자의 개수 출력



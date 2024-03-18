import sys
sys.stdin = open('input.txt')

T = int(input())  # 테스트 케이스의 개수를 입력 받음
for tc in range(1, T + 1):  # 각 테스트 케이스에 대해 반복
    a, b = input().split()  # 문자열을 입력 받음
    lst = input().split()  # 문자열 리스트를 입력 받음

    word = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}  # 단어에 대응하는 숫자를 가지는 딕셔너리

    print(f'#{tc}')  # 테스트 케이스 번호 출력
    print(*sorted(lst, key=lambda x: word[x]))  # 주어진 단어 순서대로 정렬하여 출력
















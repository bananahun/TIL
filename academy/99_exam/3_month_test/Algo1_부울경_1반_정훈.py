# import sys
#
# sys.stdin = open('algo1_sample_in.txt')


def change_2_16(num_2):  # 2진수를 16진수로 바꿔봅시다
    num_10 = int(num_2, 2)  # 2진수를 10진수로
    check_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']  # 인덱스 번호생각해서 0추가
    result = ''  # 결과값은 문자열로 -> 16진수는 문자가 들어가니까
    while num_10 > 0:  # 10진수를 계속해서 16으로 나누겠습니다.
        result += str(check_lst[(num_10 % 16)])  # 나머지를 추가
        num_10 //= 16  # 몫은 계속 해서 나늡니다.
    return result[::-1]  # 밑에서 부터니까 거꾸로 나열


def change_16_2(num_16):  # 16 진수를 2진수로 바꿔봅시다
    num_10 = int(num_16, 16)  # 16진수를 10진수로
    num_2 = bin(num_10)  # 10진수를 2진수로
    num_2 = num_2[2:]  # 앞에 문자두개가 붙으니까 빼줍니다.
    need_0 = 24 - len(num_2)  # 필요한 0의 갯수 구하기
    return '0' * need_0 + num_2  # 필요한 0갯수 더하기 우리가 구한 2진수


T = int(input())
for tc in range(1, T + 1):
    a, number = input().split()
    if a == '6':
        print(f'#{tc}', change_16_2(number))
    else:
        print(f'#{tc}', change_2_16(number))

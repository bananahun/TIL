import sys
sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1,T+1):
#     arr = input()
#     lst = [None] * len(arr)
#
#     for i in range(len(arr)):
#         if '{' == arr[i] and lst[-1] == '(':
#             lst.append('{')
#         elif '}' == arr[i] and lst[-1] == '{':
#             lst.pop()
#         elif '}' == arr[i] and lst[-1] != '{':
#             print(f'#{tc} 0')
#             break
#         elif '(' == arr[i]:
#             lst.append('(')
#         elif ')' == arr[i] and lst[-1] == '(':
#             lst.pop()
#         elif ')' == arr[i] and lst[-1] != '(':
#             print(f'#{tc} 0')
#             break
#
#     if len(lst) == len(arr):
#         print(f'#{tc} 1')
#     else:
#         print(f'#{tc} 0')

# T = int(input())
# for tc in range(1, T + 1):
#     arr = input()
#     lst = [None] * len(arr)
#
#     for i in range(len(arr)):
#         if '{' == arr[i]:
#             lst.append('{')
#         elif '}' == arr[i]:
#             if lst:
#                 lst.pop()
#         elif '(' == arr[i]:
#             lst.append('(')
#         elif ')' == arr[i]:
#             if lst:
#                 lst.pop()
#
# T = int(input())
# for tc in range(1,T+1):
#     arr = input()
#     lst = [None] * len(arr)
#
#     for i in range(len(arr)):
#         if '{' == arr[i]:
#             lst.append('{')
#         elif '}' == arr[i] and lst[-1] == '{':
#             lst.pop()
#         elif '}' == arr[i] and lst[-1] != '{':
#             lst.append('0')
#             break
#         elif '(' == arr[i]:
#             lst.append('(')
#         elif ')' == arr[i] and lst[-1] == '(':
#             lst.pop()
#         elif ')' == arr[i] and lst[-1] != '(':
#             lst.append('0')
#             break
#     if len(lst) == len(arr):
#         print(f'#{tc} 1')
#     else:
#         print(f'#{tc} 0')





T = int(input())  # 테스트 케이스의 개수를 입력받습니다.
for tc in range(1, T + 1):  # 각 테스트 케이스에 대해 반복합니다.
    arr = input()  # 문자열을 입력받습니다.
    lst = []  # 빈 리스트를 생성하여 괄호를 담을 준비를 합니다.
    result = 1  # 결과를 1로 초기화합니다. (올바른 괄호인 경우 1, 그렇지 않은 경우 0)

    # 문자열을 한 글자씩 반복하며 괄호의 쌍이 올바르게 맞춰져 있는지 확인합니다.
    for i in range(len(arr)):
        if '{' == arr[i]:  # 여는 중괄호인 경우
            lst.append('{')  # 리스트에 추가합니다.
        elif '(' == arr[i]:  # 여는 소괄호인 경우
            lst.append('(')  # 리스트에 추가합니다.
        elif '}' == arr[i]:  # 닫는 중괄호인 경우
            if lst and lst[-1] == '{':  # 리스트가 비어있지 않고, 마지막 요소가 여는 중괄호인 경우
                lst.pop()  # 리스트에서 마지막 요소를 제거합니다. (괄호 쌍이 맞는 경우)
            else:
                result = 0  # 그렇지 않으면 올바르지 않은 괄호이므로 결과를 0으로 설정하고 반복문을 탈출합니다.
                break
        elif ')' == arr[i]:  # 닫는 소괄호인 경우
            if lst and lst[-1] == '(':  # 리스트가 비어있지 않고, 마지막 요소가 여는 소괄호인 경우
                lst.pop()  # 리스트에서 마지막 요소를 제거합니다. (괄호 쌍이 맞는 경우)
            else:
                result = 0  # 그렇지 않으면 올바르지 않은 괄호이므로 결과를 0으로 설정하고 반복문을 탈출합니다.
                break

    # 반복문이 종료된 후에도 리스트에 요소가 남아있다면, 괄호 쌍이 맞지 않는 것입니다.
    else:
        if lst != []:
            result = 0

    # 각 테스트 케이스에 대한 결과를 출력합니다.
    print(f'#{tc} {result}')




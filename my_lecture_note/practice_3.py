items = ['apple', 'banana', 'coconut']
    
for item in items:
    print(item)

number = int(input('양의 정수를 입력해주세요.: '))

while number <= 0:
    """
    종료 조건과 break
    """
    if number == -9999: 
        print('프로그램을 종료합니다.')
        break

    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')

    number = int(input('양의 정수를 입력해주세요.: '))

print('잘했습니다!')


while True:
    try:
        number = int(input("숫자를 입력하세요: "))
        if number < 0:
            print("음수를 입력하셨습니다. 양수를 입력할 때까지 계속 입력하세요.")
            continue
        else:
            break  # 양수를 입력받으면 반복문 탈출
    except ValueError:
        print("유효한 숫자를 입력하세요.")

if number % 2 == 0:
    print(f"{number}은(는) 짝수입니다.")
else:
    print(f"{number}은(는) 홀수입니다.")

print(0o1414)
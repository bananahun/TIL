def greet(name):
    '''함수 앞에 함수를 설명해주는 함수 설명서
    Docstring'''
    message = 'Hello, ' + name
    return message

result = greet('Arsenal')
print(result)

dust = 480

if dust > 150:
    print('매우 나쁨')
    """
    중첩 조건문
    """
    if dust > 300:
        print('위험해요! 나가지 마세요!')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')


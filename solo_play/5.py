# 1번 문제 
def calculate_area(r):
    pi = 3.14159
    return r**2*pi


# 2번 문제
def is_prime(num):
    if num < 2:
        print('1입니다.')

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print('짝수입니다.')  
        else:
            print('소수입니다.')
is_prime(1)


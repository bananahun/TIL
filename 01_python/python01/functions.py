#리스트를 다루는 연습
#수업시간에 다루지 않은 매서드 라는 개념

def some_func(parm1,parm2):
    # 함수가 하는 일을 작성하는 영역
    result = parm1 + parm2

# 함수를 호출한다.
some_func('가', '나')
# 함수를 호출한 결과를 어떤 변수에 할당해보자. 
answer = some_func(1,2)#return 값이 없다. 
# -> 파이썬이 알아서 값이 없음을 나타내는 None을 반환한다. 
print(answer) # None -> 값이 없음을 나타내기 위한 데이터 타입

#리스트란, 시퀀스 형태의 데이터다. 
#순서가 없는 값이고, 정렬 되어 없음을 보장하지는 않는다. 
#내부요소를 오름차순으로 정렬하고 있다. 
numbers = [4, 3, 2, 1]
# 메서드 : 누군가가 가지고 있는 함수 
#리스트가 가지고 있는 sort 메서드 (함수)
result = numbers.sort() # 사용 방법은 함수와 완전히 동일하다. 
print(result)
print(numbers)

# 내장함수 : 파이썬이 기본적으로 가지고 있는 함수
numbers =[4, 3, 2, 1]
# sorted 함수와 sort매서드의 차이
# list.sort() 매서드는 정렬 대상인 주어(리스트)가 정해져있따. 
# 반면 sorted 함수는 '누구를''정렬'할 것인지 정해 줘야한다. -> 인자를 남긴다. 
result = sorted(numbers)
print(result)
print(numbers)
def some_func(parm1,parm2):
    # 함수가 하는 일을 작성하는 영역
    result = parm1 + parm2
    return result

answer = some_func('가', '나')
print(answer)

def other_func(parm1,parm2):
    result = parm1 * parm2
    print(result,'함수 내부에서 실행')
    return result
answer = other_func(2, 3)
print(answer, '함수 외부에서 실행')

'''
def sorted (literable, key=None , reverse = False):
    pass
sorted(list, reverse = True)
'''

answer = sorted(numbers, reverse = True)
print(answer)

'''
def some_fuc(name, age)
    pass
    
some_func(age = 3, name = 홍)
'''

def other_func(*args, name):
    pass

# other_func(1, 2, 3, 4, 5, 6, 7) 
other_func(1, 2, 3, 4, 5, 6, 7, name = '홍')

# LEGB

a = 1
b = 2
def enclosed():
    a = 10
    c = 3
    def local(c):
        print(a, b, c)     # 10 2 500
    local(500)
    print(a, b, c)     # 10 2 3

enclosed()
print(a, b)     # 1 2 

'''
Q. 함수는 왜 만들어야 함?
A. 다시 쓰지 말자 -> 똑같은 코드를

Q. 똑같은 코드 다시 안쓰는거 for문 아닌가?
A. 단순히 반복되는 경우 말고, input에 따라서 같은 일을 하는데,
   output이 달라지는 모든 경우에 대입하기 위해서.
    
알고리즘이란걸 왜 하는데? -> 특정 상황에 대한 문제 해결 능력
'''

# 글로벌 함수 정의 
global_var = 100
my_list = [1, 2, 3]
# 함수 정의
def local():
    # 글로벌 스코프의 변수 함수 내에서 출력
    # print(global_var)
    # 글로벌 변수의 값을 로컬에서 변경 할 수 없다.
    # global_var = 3 # 로컬에서 재정의
    my_list[0] = 100
    # print(global_var)
    print(my_list)
# 함수호출
local()

# 함수로 글로벌 스코프에 정의된 변수의 값을 바꾸는 법
global_var = 100
def local(parm):
    parm += 3
    return parm
global_var = local(global_var)
print(global_var)

# global 키워드만 사용X
global_var = 100
def local():
    global global_var
    global_var +=3
local()
print(global_var)


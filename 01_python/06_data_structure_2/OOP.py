def some():
    return False
a = 1
b = '가'
c = [1, 2, 3]
d = range(1,10)
e = map(int,'123')
f = set()
g = dict()
h = some()
i = map(some, {1, 2, 3})

def other(arg):
    print(arg)

def some(func,arg):
    func(arg)
    return None

some(other,'안녕하세요')

a= [1, 2]
b = ['a', 'b']
c = ['ㄱ', 'ㄴ']
d = list('가')

a.append(30)
b.append('c')
c.append('d')
d.append('나')

class Person:
    def breath(self):
        print('습-하')

p1 = Person()
p2 = Person()
p1.breath()
p2.breath()
p1.name = '정훈'
print(p1.name)
p2.name = '훈정'
print(p2.name)
print(type(p1))
print(isinstance(p1,Person))

# 함수도 객체다. 인자로 넘겨 줄수 있다. ex) map
# 파이썬에 변수로 할당 할수 있는 모든 것은 객체다. 
# 그렇다면 모든 것이 객체다. 고민X -> 전부 다 객체다. 

# OOP(객체지향프로그래밍)
# -> class 를 사용 
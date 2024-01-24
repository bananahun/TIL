import random
# 금기해제
class 푸키먼:
    # 세상의 모든 포켓몬은 고유 번호를 가진다.
    # 각 인스턴스의 고유번호가 x
    # 피카츄 라는 종은 모두 n번의 고유번호를 가진다.
    # 클래스 변수로 설정
    고유번호 = '세상의 모든 포켓몬은 고유 번호를 가진다.'
    현재_발견된_총_푸키먼_수 = 0
    푸키먼_종류 = {}

    # 매직 매서드 : 생성자
    # 인스턴스 매서드군?
    def __init__(self , 종, 타입, 속도, 스킬1='몸통박치기', 체력=100, 레벨=1):
        self.종 = 종
        self.타입 = 타입
        self.속도 = 속도
        self.스킬1 = 스킬1
        self.체력 = 체력
        self.레벨 = 레벨
        푸키먼.새로운_포켓몬이_탄생했다(종)
        self.고유번호 = 푸키먼.푸키먼_종류[종][0]

    # 인스턴스 매서드 : 해당 클래스의 모든 인스턴스들이 공통적으로 하는일
    # 함수임.
    def 스킬1사용(self):
        # 단순 문구 출력
        print(f'{self.종}은 {self.스킬1}을 사용하였다.')
        # 추가 조건에 따른 서로 다른 경우 출력
        # 무작위 정수를 하나 뽑아서
        # 그정수의 값에 따라 서로 다른 결과 출력
        주사위 = random.randint(1, 6)
        if 주사위 == 6:
            print('효과는 굉장했다.')
        elif 주사위 >= 3:
            print('적에게 적중했다.')
        else:
            print('그러나 아무일도 일어나지 않았다.')

    # 클래스의 변수를 변경시키거나, 혹은, 클래스와 관련도니 어떠한 속성을 행위를 실행하는 함수
    # 함수임.
    @classmethod
    def 새로운_포켓몬이_탄생했다(cls, 종):
        # 호출 된 순간이 인스턴스 생성된 순간에만 쓰일것이라고 우리끼리 약속
        cls.현재_발견된_총_푸키먼_수 += 1
        # 만약, 처음 발견한 종이라면,
        if 종 not in cls.푸키먼_종류:
            print('한번도 본 적 없던 푸키먼이다!')
            # 종의 고유 번호 => 푸키먼_종류 딕셔너리의 총 길이 + 1
            #  [종의 고유번호, 종의 개체수]
            cls.푸키먼_종류[종] = [len(cls.푸키먼_종류)+1, 1]
            print(f'{종}! 앞으로 너의 고유 번호는 {cls.푸키먼_종류[종][0]}번 이야!') 
        #아니라면, 
        else:
            print(f'{종}의 개체수가 1 증가하였다.')
            cls.푸키먼_종류[종][1] += 1
            print(f'{종}의 총 개체수는 {cls.푸키먼_종류[종][1]}')
        
    


# 푸키먼 클래스의 인스턴스를 생성후 피카츄 변수에 할당
피카츄1 = 푸키먼(종='피카츄',타입='전기',속도='100')
피카츄2 = 푸키먼('피카츄','전기',110)
파이리 = 푸키먼('파이리','불', 60)
print(푸키먼.현재_발견된_총_푸키먼_수)
print(푸키먼.푸키먼_종류)
print('-'*30)
print(피카츄1.고유번호)
print(피카츄2.고유번호)
print(파이리.고유번호)
print(푸키먼.고유번호)
# 피카츄 변수에 할당된 인스턴스의 속성 고유번호를 출력
print(피카츄1.고유번호)
print(피카츄2.고유번호)
# 같은 값을 넣으면 같은 값이 나옴
print(피카츄1.종)
print(피카츄2.종)
# 다른 값을 넣으면 다른 값이 나옴
print(피카츄1.속도)
print(피카츄2.속도)
# 클래스가 클래스 변수 출력
print(푸키먼.고유번호)
# 클래스에도 없는 변수를?
# print(피카츄1.없는변수)
# global에 있는 변수를 찾도록 하면요?
# 글로벌_변수 = '반성문을 영어로하면 글로벌'
# print(피카츄1.글로벌_변수)

# 각 인스턴스로 인스턴스 메서드 호출
피카츄1.스킬1사용()
피카츄2.스킬1사용()

피카츄1.고유번호 = 1
print(피카츄1.고유번호)
print(피카츄2.고유번호)
print(푸키먼.고유번호)

















# 원사용법
print('hello'.upper())
# # 위 코드 실행시 내부 동작 방식
# print('hello'.upper('hello'))
# # 내부 동작 방식을 내가 직접 작성했을 때, 실제로 이뤄지는 방식
# print('hello'.upper('hello','hello'))


##python tutor 돌려봐라
'''
class Person:
    count = 0
    
    def __init__(self):
        Person.count += 1
        
p1 = Person()
p2 = Person()

print(p1, p2)
print(p1.count)
print(Person.count)
'''

number_of_people = 0
def increase_user(nop):
    nop += 1
    return nop
number_of_people = increase_user(number_of_people)
print('현재 가입 된 유저 수:', number_of_people)

name_list = []
def create_user(name_1,age_1,address_1):
    for i in range(len(name_1)):
        print(f'{name_1[i]}님 환영합니다 !')
    for i in range(len(name_1)):  
        name_dict = {'name':name_1[i],'age':age_1[i],'address':address_1[i]}
        name_list.append(name_dict)
    print(name_list)


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

create_user(name,age,address)

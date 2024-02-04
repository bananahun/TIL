# number_of_people = 0
# def increase_user(nop):
#     nop += 1
#     return nop
# number_of_people = increase_user(number_of_people)
# print('현재 가입 된 유저 수:', number_of_people)


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


name_list = []
def create_user(name_1,age_1,address_1):
    for i in range(len(name_1)):
        print(f'{name_1[i]}님 환영합니다 !')
    for i in range(len(name_1)):  
        name_dict = {'name':name_1[i],'age':age_1[i],'address':address_1[i]}
        name_list.append(name_dict)

create_user(name,age,address)

many_user = name_list

for ii in range(len(name)):
    info = {name[ii]:age[ii]}

def rental_book(name,age):
    
    book_num = 100
    for ii in range(len(name)): 
        print(f'남은 책의 권수 : {book_num - age[ii]//10}')
        book_num = book_num - age[ii]//10 
        print(f'{name[ii]}님이 {age[ii]//10}권의 책을 대여하였습니다.')
          
rental_book(name,age)
number_of_people = 0
print('현재 가입 된 유저 수: ',number_of_people)

def increase_user(nop):
    nop += 1
    return nop

def create_user(name_info,age_info,address_info):
    user_info = {'name':name_info, 'age':int(age_info), 'address': address_info}
    return user_info
user_info = create_user('홍길동',30,'서울')
print(f'{user_info["name"]}님 환영합니다!')
print(user_info)
print('현재 가입 된 유저 수 :',increase_user(number_of_people))
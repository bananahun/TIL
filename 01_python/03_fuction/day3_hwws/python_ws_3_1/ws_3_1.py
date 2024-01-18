number_of_people = 0
def increase_user(nop):
    nop += 1
    return nop
number_of_people = increase_user(number_of_people)
print('현재 가입 된 유저 수:', number_of_people)
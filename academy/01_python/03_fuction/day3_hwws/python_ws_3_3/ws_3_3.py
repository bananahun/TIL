def rental_book(num_book):
    print(f'남은 책의 권수 : {number_of_book - num_book}')

number_of_book = 100

def decrease_book(name_person,num_book):
    print(f'{name_person}님이 {num_book}권의 책을 대여하였습니다.')

rental_book(3)
decrease_book('홍길동',3)
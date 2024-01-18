list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_list = [
    '장생전',
    '원생몽유록',
    '이생규장전',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]
# check = False
# for rental in rental_list:
#     book_found = False
#     for book in list_of_book:
#         print(book,rental)
#         if book == rental:
#             book_found = True
#             break
#     if book == False:
#         check = False
#         print(f'{rental} 은/는 보유하고 있지 않음')
#         break
# if check == True:
#     print('모든 도서가 대여 가능한 상태입니다.')


check = True
for rental in rental_list:
    if rental not in list_of_book:
        print(f'{rental}은 보유하고 있지 않습니다.')
        break
if check == False:
    print('모든 도서가 대여 가능한 상태입니다.')

# check = True
# for rental in rental_list:
#     if rental not in list_of_book:
#         print(f'{rental}은 보유하고 있지 않습니다.')
#         break

# else:
#     print('모든 도서가 대여 가능한 상태입니다.')


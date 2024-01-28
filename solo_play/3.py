# 이중 for 문 확인

# list_1 = [1,2,3,4]
# list_2 = [5,6,7,8]
# for num_1 in list_1:
#     for num_2 in list_2:
#         print(num_1,num_2)

# 딕셔너리 키 밸류 아이템 함수 확인
# dict_1 = {'a' :1, 'b':2, 'c':3, 'd':4}
# print(dict_1.keys())
# print(dict_1.values())
# print(dict_1.items())
# print(type(dict_1.items()))

my_dict = {'a': 1, 'b': 2, 'c': 3}

print(list(my_dict.keys()))
print(list(my_dict.values()))
print(list(my_dict.items()))

# items() 함수를 사용하여 딕셔너리의 키-값 쌍 뷰(view) 객체 생성
items_view = my_dict.items()

# 뷰(view) 객체를 리스트로 변환하여 출력
items_list = list(items_view)
print("items() 함수로 생성된 뷰(view) 객체:", items_list)

# 뷰(view) 객체를 순회하여 각 키-값 쌍 출력
print("키-값 쌍 순회:")
for key, value in items_view:
    print(f"키: {key}, 값: {value}")

# 딕셔너리의 키-값 쌍 수정
my_dict['a'] = 10
my_dict['b'] = 20

# 뷰(view) 객체를 다시 순회하여 변경된 키-값 쌍 출력
print("변경된 키-값 쌍 순회:")
for key, value in items_view:
    print(f"키: {key}, 값: {value}")
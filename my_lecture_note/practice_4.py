# print(type('1'))

# print(help(str))

# print(help(list))

def append():
    pass

append() # 함수호출 

print('banana'.find('a'))
print('banana'.find('z'))

# my_list = [1, 2, 3]
# index = my_list.index()
# print(index)

# 할당
original_lsit=[1,2,3]
copy_list=original_lsit

copy_list[0] = 'hello'
print(original_lsit)

# 얕은 복사
a = [1,2,3]
b = a[:]

b[0] = 100
print(a)

import copy

original_list = [1, 2, [1,2]]
deep_copy_list = copy.deepcopy(original_list)

deep_copy_list[2][0] = 999
print(original_list)
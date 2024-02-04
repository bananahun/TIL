# 아래 함수를 수정하시오.

def get_keys_from_dict(new_dict):
    new_list = []
    for k in new_dict.keys():
        new_list.append(k)
    return new_list


my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']

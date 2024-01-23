# 아래 함수를 수정하시오.
def add_item_to_dict(new_dict,new_key,new_value):
    new_dict = my_dict.setdefault(new_key,new_value)
    return my_dict


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)

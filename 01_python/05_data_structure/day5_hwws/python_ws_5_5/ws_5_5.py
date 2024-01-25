# 아래 함수를 수정하시오.

# def even_elements(my_list):
#     for element in my_list:
#         if element % 2 == 0:
#             pass
#         else:
#             my_list.remove(element)
#     return my_list


def even_elements(my_list):
    elements = []
    elements.extend(element for element in my_list if element %2 == 0)
    return elements

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)

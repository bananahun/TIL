# 아래 함수를 수정하시오.
def sort_tuple(old_tuple):
    old_list = []
    for i in range(len(old_tuple)):
        old_list.append(old_tuple[i])
        old_list.sort()

    return tuple(old_list)
      
result = sort_tuple((5, 2, 8, 1, 3))
print(result)

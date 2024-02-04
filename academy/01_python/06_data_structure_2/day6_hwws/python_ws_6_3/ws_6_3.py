# 아래 함수를 수정하시오.
def intersection_sets(set_1,set_2):
    new_set = set_1.intersection(set_2)
    return new_set


result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result)

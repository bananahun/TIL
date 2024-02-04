# 아래 함수를 수정하시오.
def remove_duplicates_to_set(my_list):
    new_set = set(my_list)
    return new_set

def remove_duplicates_to_set(arr):
    for num in arr:
        count_dict = {i :0 for i in range(1,10)}
        for num in arr:
            count_dict[num] +=1
        result = [key for key, item in count_dict.items() if item >= 1]
        return set(result)
    



result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)

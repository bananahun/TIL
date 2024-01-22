# 아래 함수를 수정하시오.
def even_elements(arr):
    for num in arr:
        if num % 2 == 1:
            arr.pop(num)
        else:
            pass
    return arr

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)

# 리스트 안의 최솟값 구하기
def min_func(my_list):
    min_num = my_list[0]
    for num in my_list:
        if min_num > num:
            min_num = num
        else:
            pass
    return min_num
sample = [5, 3, 2, -1, 0, -3, 7]
print(min_func(sample))


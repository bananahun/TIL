# n = int(input())
# arr_n = list(map(int,input().split()))
# m = int(input())
# arr_m = list(map(int,input().split()))
# lst = [0] * m

# for i in range(m):
#     for j in range(n):
#         if arr_m[i] == arr_n[j]:
#             lst[i] += 1
# print(*lst)



n = int(input())
arr_n = list(map(int,input().split()))
m = int(input())
arr_m = list(map(int,input().split()))
dic = {}
for i in range(m):
    dic[arr_m[i]] = 0
key_lst = list(dic.keys())
for number in arr_m:
    for keys in key_lst:
    
    
    
        




# my_dict = {1:'a', 2:'b', 3:'c'}
# print(list(my_dict.keys()))
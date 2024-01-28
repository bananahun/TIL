lst = list(map(int, input().split()))
ans = [lst.pop()]

a = 0
while lst:
    tmp = lst.pop()
    i = 0
    
    while i < len(ans):
        if tmp >= ans[i]:
            i += 1

        elif tmp < ans[i]:
            ans.insert(i, tmp)
            break

        if i == len(ans):
            ans.append(tmp)
            break

print(ans)





# new_list = []
# def arr_func(sample_list):
#     for n in range(len(sample_list)):
#         for m in range(len(sample_list)):

        
#     return new_list      
# print(arr_func(my_list))

# # 리스트 안의 숫자들에 1을 더한 리스트를 출력
# my_list = [num+1 for num in my_list]
# print(my_list)

# # 리스트 안의 숫자들을 순서대로 배열하는 함수 만들어보기
# def arr(sample_list):
#     return sorted(sample_list)
# print(arr(my_list))

# my_dict = {'jeong': 123 , 'hun': 456 , 'good': 789 , 'boy': 100}

# # 다음 딕셔너리의 숫자들을 뽑아내서 리스트로 만드는 함수를 만들어라
# def make_num(sample_dict):
#     num_list = []
#     for num_value in sample_dict:
#         num_list.append(sample_dict[num_value])
#     return sorted(num_list)
# print(make_num(my_dict))


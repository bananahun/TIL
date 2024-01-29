############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count()를 사용하지 않습니다.
def find_solo(number_list):
    
    # 여기에 코드를 작성하여 함수를 완성합니다.
    return sum(list(set(number_list)))*2 - sum(number_list)
    # set을 이용해 숫자를 하나씩만 만들어 주고 set의 합에 2를 곱한다. 
    # 그리고 set의 합에서 list의 합을 빼주면 쌍이 없는 숫자만 남게 된다.




# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
number_list1 = [64, 27, 71, 27, 64]
print(find_solo(number_list1))  # 71
number_list2 = [4, 14, 60, 14, 49, 49, 78, 60, 78]
print(find_solo(number_list2))  # 4
#####################################################

############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 min 함수를 사용하지 않습니다.
def min_cost(cost_list):
    
    # 여기에 코드를 작성하여 함수를 완성합니다.
    min_value = cost_list[0] # 리스트의 첫 번째 값을 최솟값으로 가정
    for value in cost_list:
        if min_value > value: # 새로운 최솟값이 나오면 변경
            min_value = value # 새로운 최솟값이 나오면 변경
        else:
            pass
    return min_value


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(min_cost([25, 40, 50, 55]))  # 25
print(min_cost([60, 70, 90, 80, 100, 35])) # 35
#####################################################

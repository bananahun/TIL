############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_position_safe(N, M, current):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # if current[0] and current[1] >0:
    #     return True
    # else:
    #     if current[0] == 0:
    #         if M == 0:
    #             return False
    #         else:
    #             pass
    #     elif current[0] == N-1:
    #         if M == 1:
    #             return False
    #         else:
    #             pass
    #     elif current[1] == 0:
    #         if M == 2:
    #             return False
    #         else:
    #             pass
    #     elif current[1] == N-1:
    #         if M == 3:
    #             return False
    #         else:
    #             pass
    #     else:
    #         return True



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(is_position_safe(3, 1, (0, 0))) # True
print(is_position_safe(3, 0, (0, 0))) # False
#####################################################

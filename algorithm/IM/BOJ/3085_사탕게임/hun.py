import sys
sys.stdin = open('input.txt')

# # print(lst)
# def check(lst, N):
#     max = 1
#     for i in range(N):
#         cnt = 1
#         for j in range(N-1):
#             if lst[i][j] == lst[i][j+1]:
#                 cnt += 1
#             else:
#                 cnt = 1
#             if max < cnt:
#                 max = cnt
        
#         cnt = 1
#         for j in range(N-1):    
#             if lst[j][i] == lst[j+1][i]:
#                 cnt += 1
#             else:
#                 cnt = 1
#             if max < cnt:
#                 max = cnt
#     return max


           
# N = int(input())
# lst = [list(map(str, input()))for _ in range(N)]    
# result = 1
# for i in range(0, N):
#     for j in range(0, N-1):
#         if lst[i][j] != lst[i][j+1]:
#             lst[i][j], lst[i][j+1] = lst[i][j+1], lst[i][j]
#             if result < check(lst, N):
#                 result = check(lst, N)
#             lst[i][j], lst[i][j+1] = lst[i][j+1], lst[i][j]
                
#         if lst[j][i] != lst[j+1][i]:
#             lst[j][i], lst[j+1][i] = lst[j+1][i], lst[j][i]
#             if result < check(lst, N):
#                 result = check(lst ,N)
#             lst[j][i], lst[j+1][i] = lst[j+1][i], lst[j][i]
# print(result)

N = int(input())
candy = [list(input()) for _ in range(N)]
# 사탕의 개수를 셀 수 있는 함수
def candy_count(area):
    result = 1
    for i in range(N):
        answer = 1
        for j in range(N-1):
            if area[i][j] == area[i][j+1]:
                answer += 1
                result = max(result, answer)
            else:
                answer = 1
        answer = 1
        for j in range(N-1):
            if area[j][i] == area[j+1][i]:
                answer += 1
                result = max(result, answer)
            else:
                answer = 1
        
    return result

total = 0
for i in range(N):
    for j in range(N-1):
        if candy[i][j] != candy[i][j+1]:
            candy[i][j] , candy[i][j+1] = candy[i][j+1], candy[i][j]
            total = max(total, candy_count(candy))
            candy[i][j] , candy[i][j+1] = candy[i][j+1], candy[i][j]
    for j in range(N-1):
        if candy[j][i] != candy[j+1][i]:
            candy[j][i] , candy[j+1][i] = candy[j+1][i], candy[j][i]
            total = max(total, candy_count(candy))
            candy[j][i] , candy[j+1][i] = candy[j+1][i], candy[j][i]
print(total)


            



            
        
            
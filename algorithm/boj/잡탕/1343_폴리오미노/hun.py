# import sys
# # sys.stdin = open('input.txt')
# input = sys.stdin.readline

# str = str(input())
# # print(str[1])
# n = len(str)
# # print(str)
# cnt_x = 0
# cnt_point = 0
# result = []
# for i in range(n):
#     if str[i] == 'X':
#         cnt_x += 1
#         if cnt_point != 0:
#             for _ in range(cnt_point):
#                 result.append('.')
#             cnt_point = 0
#     elif str[i] == '.':
#         cnt_point += 1
#         if cnt_x != 0:
#             if cnt_x // 4 == 0:
#                 for _ in range((cnt_x//4) * 4):
#                     result.append('A')
#             elif cnt_x % 4 == 2:
#                 for _ in range(2):
#                     result.append('B')
#             else:
#                 result = [-1]
#                 cnt_point = 0
#                 cnt_x = 0
#                 break
# print(*result)



str = input().split('.')
print(str)
# str.remove(str[-1])
result = ''
for x in str:
    if len(x) % 2 == 1:
        print(-1)
        break
    while len(x) >= 4:
        result += 'AAAA'
        x = x[4:]
    if len(x) == 2: 
        result += 'BB'
        x = x[2:]
    if x == '':
        result += '.' 
else:
    print(result[:-1])

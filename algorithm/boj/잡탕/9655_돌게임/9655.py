# N = int(input())

# if N%2 == 0:
#     print('CY')
# else:
#     print('SK')

N = int(input())

lst = [False] * (N+1)
lst[1] = 0 #sk
lst[2] = 1 #cy
lst[3] = 0

for n in range(3, N+1):
    if lst[n-1] == 0 or lst[n-3] == 0:
        lst[n] = 1
    else:
        lst[n] == 0
if lst[N] == 1:
    print('CY')
elif lst[N] == 0:
    print('SK')






#상영이가 항상 먼저 돌을 가져간다.
#돌은 항상 1개 또는 3개를 가져간다.
#최적의 게임을 해서 항상 이길수 있는 사람을 정해라.
# 1 --> 상근
# 2 --> 찬영
# 3 --> 상근
# 4 --> 찬영
# 5 --> 상근
# 6 --> 찬영
# 7 --> 상근
# 8 --> 찬영
# 9 -->
# 10 -->
# 11 -->
# 12 -->
# 13 -->
# 14 -->
# 15 -->
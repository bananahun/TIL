# print('맛있겠다 삼겹살')
# print('껍데기')
# print('참이슬')
# print('동환이는 애피타이저')
# print('집에 가서 본게임')
#
# print('이거 너무 좋다 팜레스트 있어야겠다 팜레스트는 못생겼어 예쁜거 사야겠다')
# print('동현이오빠 태화강 신청 각')
import sys
sys.stdin = open('input.txt')

N = int(input())
for i in range(1, N + 1):
    num = sum((map(int, str(i))))
    sum_num = i + num

    if sum_num == N:
        print(i)
        break
    if i == N:
        print(0)
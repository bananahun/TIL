# 버블 정렬
# def Bubble_Sort(my_list):
#     a = my_list
#     N = len(my_list)
#     for i in range(N-1,0,-1):
#         for j in range(0,i):
#             if a[j] > a[j+1]:
#                 a[j],a[j+1] = a[j+1],a[j]
#     return my_list
#
# # 동일한 숫자가 포함 되지 않았을 떄, 각자리수 별로 loop를 이용해
# # 아래와 같이 구현 할 수 있다.
#
# for i1 in range(1,4):
#     for i2 in range(1,4):
#         if i2 != i1:
#             for i3 in range(1,4):
#                 if i3 != i1 and i3 != i2:
#                     print(i1,i2,i3)
#
# # 각 자릿수를 알아내는 법
#
# num = 456789 # baby gin 확인할 6자리수
# c = [0]*12
# for i in range(6):
#     c[num%10] +=1
#     num //10





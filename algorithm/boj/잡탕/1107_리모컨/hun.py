end = int(input())
n = int(input())
use_lst = [0,1,2,3,4,5,6,7,8,9]
not_use = list(map(int, input().split()))
for num in not_use:
    use_lst.remove(num)
# print(use_lst)

check_minus = 100
check_plus = 100
cnt = 0
while check_plus != end or check_plus != end:
    check_minus = int(check_minus) - 1
    check_plus = int(check_plus) + 1
    cnt += 1
    result_1 = 0
    for num in str(check_minus):
        if num not in use_lst:
            result_1 += 1
        else:
            start = check_minus
    result_2 = 0
    for num in str(check_plus):
        if num not in use_lst:
            result_2 += 1

    if result_1 or result_2 == 0:
        print(check_plus)
        print(cnt)
        break








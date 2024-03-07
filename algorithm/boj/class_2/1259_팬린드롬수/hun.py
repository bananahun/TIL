result = 0
while result == 0:
    lst = list(map(str, input()))
    if lst == ['0']:
        result = 1
        break
    else:
        if lst == lst[::-1]:
            print('yes')
        else:
            print('no')
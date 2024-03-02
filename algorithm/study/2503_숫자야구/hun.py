N = int(input())
case = [0]*988

lst = []
for _ in range(N):
    num, s, b = map(int, input().split())
    num = str(num)
    for i in range(123, 988):
        cnt = 0
        i = str(i)
        if i[0] == i[1] or i[1] == i[2] or i[2] == i[0]:
            case[i] = True
        if s == 1 and b == 0:
            if i[0] == num[0] or i[1] == num[1] or i[2] == num[2]:
                cnt += 1
        if s == 2 and b == 0:
            if i[0] == num[0] and i[1] == num[1]:
                cnt += 1
            elif i[0] == num[0] and i[2] == num[2]:
                cnt +=1
        if s == 0 and b == 1:
            if i[1] == num[0] or i[2] == num[0] or i[3] == num[1] or i[0] == num[1] or i[0] == num[2] or i[1]==num[2]:
                cnt += 1
        if s == 0 and b == 2:
            if i[0] == num[1] and i[1] == num[2]:
                cnt+=1
            elif i[0] == num[2] and i[2] == num[1]:
                cnt+=1
            elif i[0] == num[2] and i[2] == num[0]:
                cnt+=1
            elif i[1] == num[0] and i[2] == num[2]:
                cnt+=1
            elif i[0] == num[1] and i[1] == num[0]:
                cnt+=1
        if s == 1 and b ==1:
            if i[0]==num[0] and i[2] == num[1]:
                cnt+=1
            elif i[0] == num[0] and i[1] == num[2]:
                cnt +=1
            elif i[1] == num[1] and i[2] == num[0]:
                cnt +=1
            elif i[1] == num[1] and i[0] == num[2]:
                cnt +=1
            elif i[0] == num[1] and i[2] == num[2]:
                cnt +=1
            elif i[1] == num[0] and i[2] == num[2]:
                cnt +=1
        if cnt == 4:
            lst.append(i)
    print(lst)



        
# a,b = input('').split()
# a = int(a)
# b = int(b)
# if a<b:
#     print('<')
# elif a>b:
#     print('>')
# else:
#     print('==')

# num = int(input())
# for num in range(1,num+1):
#     print('*'*num)

# a,b,c,d,e = input('').split()
# a = float(a)
# b = float(b)
# c = float(c)
# d = float(d)
# e = float(e)
# print(int((a**2+b**2+c**2+d**2+e**2)%10))

# num = int(input())
# for n in range(1,10):
#     print(f'{num} * {n} = {num*n}')

# S=str(input())
# i=int(input())
# print(S[i-1])

def Bubble_Sort(my_list):
    a = my_list
    N = len(my_list)
    for i in range(N-1,0,-1):
        for j in range(0,i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return my_list


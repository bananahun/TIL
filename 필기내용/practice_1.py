my_list = [False,'False',0,'asd',[True,1,'1',],'123']

print(my_list[0]) # False 
print(my_list[1]) # False 
# print(my_list[0][2]) # TypeError
print(my_list[1][2]) # l
print(my_list[2]) # 0
print(my_list[3]) # 'asd'
print(my_list[4]) # [True,1,'1']
print(my_list[5]) # 123
# print(my_list[6]) # IndexError
print(my_list[4][0]) # True
print(my_list[4][1]) # 1
print(my_list[4][2]) # 1
# print(my_list[4][1][-1]) # TypeError
print(my_list[-1][-1][-1]) # 3
print(my_list[-1][-1][-1][-1][-1][-1][-1][-1]) #3

x, y = 10, 20
print(x)
print(y)
a, b = (10,20)
print(a)
print(b)

my_range1 = range(5)
my_range2 = range(2,10)

print(my_range1)
print(my_range2)

print(list(my_range1))
print(list(my_range2))
    
test_list = [0,None,1]     






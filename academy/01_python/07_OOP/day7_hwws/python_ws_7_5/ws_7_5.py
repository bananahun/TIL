# 아래 클래스를 수정하시오.
# class Shape:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def __str__(self):
#         # return 'Shape: width='+str(self.a)+', height='+str(self.b)
#         return f'Shape: width={self.a}'
           
# shape1 = Shape(5, 3)
# print(shape1)

class Shape:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return f'Shape: width = {self.a} height = {self.b}'

shape1 = Shape(5, 3)
print(shape1)


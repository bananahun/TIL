# 아래 함수를 수정하시오.
def reverse_string(string):
   new_string = string[::-1]
   return new_string

def reverse_string(word):
   return ''.join(reversed(word))
result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH

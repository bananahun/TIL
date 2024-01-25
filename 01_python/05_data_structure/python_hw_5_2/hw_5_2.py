# 아래 함수를 수정하시오.
def count_character(word,char):
    return word.count(char)

def count_character(word,char):
    result = 0
    for text in word:
        if text == char:
            result += 1    
    return result
result = count_character("Hello, World!", "o")
print(result)  # 2

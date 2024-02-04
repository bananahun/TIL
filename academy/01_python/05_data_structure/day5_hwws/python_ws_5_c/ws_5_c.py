def restructure_word(word, arr):
    pass

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []
for i in range(len(original_word)):
    arr.append(original_word[i])
print(arr)

for m in range(len(word)):
    if word[m].isdecimal() == True:
        for m in range(int(word[m])):
            arr.pop()
    else:
        arr.remove(word[m])

print(arr)

result =''.join(arr)

print(result)



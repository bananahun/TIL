up, down, tree = map(int, input().split())


'''
올라가고
내려가고
반복이지만 마지막에 올라갔을 때 길이가 tree의 길이 보다 길어진다면 종료 하므로 
마지막에 올라간 길이를 한번 빼주려고 했다.
그렇다면 총 올라가야할 날짜에서 하루를 더한 상태로 시작
왜냐하면 이미 올라간것을 한번 뺐으므로
'''
tree -= up
if (tree % (up-down)) == 0:
    print(tree // (up-down) + 1)
else:
    print(tree // (up - down) + 2)
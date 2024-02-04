n,c,w = map(int,input().split())
sum=0
list = []
for number in range(n):
    k = int(input())
    list.append(k)
max_k = max(list)
max_money = 0
for i in range(1,max_k+1):
    tree = k//i
    trash = k%i
    if trash != 0:
        money = tree*i*w - c*(tree)
    else:
        money = tree*i*w - c*(tree-1)

        if money <= 0 :
            pass
        
        if max_money <= money:
            max_money = money
    sum = sum + max_money
print(sum)
        

    
    

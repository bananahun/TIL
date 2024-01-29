# 버블 정렬
def Bubble_Sort(my_list):
    a = my_list
    N = len(my_list)
    for i in range(N-1,0,-1):
        for j in range(0,i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return my_list

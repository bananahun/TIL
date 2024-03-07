def average(M,lst):
    num_sum = 0
    for num in lst:
        num_sum += num/M*100
    avreage = num_sum / len(lst)
    return avreage


N = int(input())
lst = list(map(int, input().split()))
M = max(lst)
print(average(M, lst))


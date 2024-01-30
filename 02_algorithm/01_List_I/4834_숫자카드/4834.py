import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    num = int(input())
    num_list = list(map(int,input()))
    count_dict = {}
    for m in range(0,10):
        count_dict[m] = num_list.count(m)
    
    for n in list(count_dict.values()):
        max_value = max(list(count_dict.values()))
        for keys,values in count_dict.items():
            if count_dict[keys] == max_value:
                max_key = keys
    print(f'#{tc} {max_key} {max_value}')
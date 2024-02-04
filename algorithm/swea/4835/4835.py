T = int(input())

for test_case in range(1,T+1):
    l_num,c_num = input().split()
    my_list = list(map(int,input().split()))
    new_list = []
    for index in range(int(l_num)-int(c_num)+1):
        
        num_sum = 0
        for j in range(int(c_num)):
            num_sum += my_list[index+j]
        new_list.append(num_sum)
    print(f'#{test_case} {max(new_list)-min(new_list)}')

T = int(input())


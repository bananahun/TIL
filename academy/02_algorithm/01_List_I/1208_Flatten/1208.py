import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    num_dump = int(input())
    box_list = list(map(int, input().split()))
    for dump in range(num_dump):
        box_list[box_list.index(max(box_list))] -=1
        box_list[box_list.index(min(box_list))] +=1
    print(f'#{tc} {max(box_list)-min(box_list)}')


import sys
sys.stdin = open('18578.txt')

T = int(input())
for tc in range(1, T+1):
    length = int(input())
    height = list(map(int, input().split()))

    lst = []
    for i in range(length):
        count = 0
        for j in range(i+1,length):
            if height[i] > height[j]:
                count += 1
            else:
                pass
        lst.append(count)
    print(f'#{tc} {max(lst)}')


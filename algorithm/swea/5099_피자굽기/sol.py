import sys

sys.stdin = open('input.txt')

from collections import deque
T = int(input())

for tc in range(1, T + 1):
    hd_num, pizza_num = map(int, input().split())
    pizza = list(map(int, input().split()))
    for i in range(len(pizza)):
        # [피자번호, 피자위의 치즈]
        pizza[i] = [i+1, pizza[i]]
    pizza = deque(pizza)
    hd = deque([pizza.popleft()])
    # 치즈가 다 녹은 피자는 여기에 놓을거예요
    result = []
    # 화덕에 피자가 존재 하는 동안
    while hd:
        # 화덕에 담을 피자가 하나도 없으면
        if len(pizza) == 0:
            temp = hd.popleft()
            # 치즈가 다 녹았으면
            if temp[1] // 2 == 0:
                # 피자를 담아둬야죠
                result.append(temp)
            # 치즈가 다 안녹았으면
            else:
                temp[1] = temp[1] // 2
                # 더 녹여야죠
                hd.append(temp)
        # 화덕에 아직까지 담을 피자가 있으면
        elif len(hd) < hd_num:
            # 피자를 화덕에 담아야죠
            hd.append(pizza.popleft())
        # 화덕에 피자가 가득 차 있으면
        else:
            temp = hd.popleft()
            # 치즈가 다 녹았으면
            if temp[1] // 2 == 0:
                # 피자를 빼야죠
                result.append(temp)
                # 새로운 피자를 넣어야죠
                hd.append(pizza.popleft())
            # 치즈가 덜 녹았으면
            else:
                temp[1] = temp[1] // 2
                # 다시 계속 돌려야죠
                hd.append(temp)
    # 결과값에 가장 마지막에 담긴 피자가 가장 마지막 까지 남아 있던 피자
    # 나는 피자라는 큐를 설정할때 [피자번호, 피자위의 치즈] 로 정했기 때문에
    # 피자 번호를 출력하려면 result 의 가장 마지막 [-1] 의 가장 먼저 나오는 값 [0] 을 출력한다
    print(f"#{tc} {result[-1][0]}")

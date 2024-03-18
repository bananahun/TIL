import sys
sys.stdin('sample_input.txt')

for tc in range(1, 11):
    N = int(input())
    data = list(map(int(input())))

    for i in range(2, N-2):
        for j in range(5):
            if j != 2:
                if data[i] - data[i-2+j] < min_vlaue:
                    min_value = data[i] - data[i-2+j]
        if min_value >0:
            redsult += min_value

    for i in range(2, N - 2):
        for j in range(i-2, i+3):
            # 나랑 나는 조사 안함
            if i == j: continue
            if data[j] >= data[i]: continue
            if data[j] < data[i]:
                temp = data[i] - data[j]
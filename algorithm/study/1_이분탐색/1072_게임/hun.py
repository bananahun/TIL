# 게임 횟수, 승리횟수
x, y = map(int, input().split())
# 현재 확률
n_per = int(y * 100 / x)
start = 1
end = x
while start < end:
    mid = (start + end) // 2
    c_per = int((y + mid) * 100 / (x + mid))
    if n_per < c_per:
        end = mid
    else:
        start = mid + 1
if n_per >= 99:
    print(-1)
else:
    print((start+end)//2)

'''
실제 소숫점값과 다른 값이 나온다
--> 이문제는 곱하기를 먼저하고 나누기를 함으로써
해결 했다
'''






'''
1 <= x <= 1000000000
1 <= y <= x
z 는 게임에서 이길 확률이다
'''
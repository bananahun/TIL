import sys
sys.stdin = open('input.txt')
'''
place = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# 상 우상 우 우하 하 좌하 좌 좌상
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
dir = {'T':0, 'RT':1, 'R':2, 'RB':3 ,'B':4, 'LB':5, 'L':6, 'LT':7}


king, stone, num = map(str, input().split())
num = int(num)

king_x = place.index(king[0]) + 1
king_y = int(king[1])

stone_x = place.index(stone[0]) + 1
stone_y = int(stone[1])

def check(x, y):
    return x >= 1 and x <= 8 and y >= 1 and y <= 8
    '''
king, doll, N = map(str,input().split())
king = [int(king[1]),ord(king[0])-64] # 보기편하게 x축 y축으로 설정
doll = [int(doll[1]),ord(doll[0])-64]
N = int(N)
order_form = {'R':[0,1],'L':[0,-1],'B':[-1,0],'T':[1,0],'RT':[1,1],'LT':[1,-1],'RB':[-1,1],'LB':[-1,-1]}
#이동 커맨드 딕셔너리로 저장
for _ in range(N):
    order = input()
    if 1<= king[0] + order_form[order][0] <= 8 and 1<= king[1] + order_form[order][1] <= 8: #범위안일때 이동
        if [king[0] + order_form[order][0],king[1] + order_form[order][1]] == doll:#이동했는데 돌이랑 같고 돌 이동한거 범위 안이다
            if 1<= doll[0] + order_form[order][0] <= 8 and 1<= doll[1] + order_form[order][1] <= 8:
                king = [king[0] + order_form[order][0],king[1] + order_form[order][1]]
                doll = [doll[0] + order_form[order][0],doll[1] + order_form[order][1]]
        else:# 돌이랑 안겹칠때
            king = [king[0] + order_form[order][0],king[1] + order_form[order][1]]
print(chr(king[1]+64)+str(king[0])) # 다시 원래대로 변환
print(chr(doll[1]+64)+str(doll[0]))
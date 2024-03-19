import sys
input = sys.stdin.readline
num, k = map(int,input().split())
people = list(range(1, num + 1))
# 제거된 사람들을 저장할 리스트 생성
removed_people = []
# 제거될 사람이 남아있는 동안 반복
while len(people) > 0:
    # K번째 사람을 제거하고 removed_people 리스트에 추가
    removed_index = (k - 1) % len(people)
    removed_person = people.pop(removed_index)
    removed_people.append(removed_person)

# 결과 출력
print("<" + ", ".join(map(str, removed_people)) + ">")


print('<',end='')
a = [3,6,2,7,5,1,4]
n = len(a)
for i in range(n):
    if i==n-1: print(f'{a[i]} >')
    else: print(f'{a[i]}, ',end='')
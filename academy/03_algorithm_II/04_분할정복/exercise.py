# 분할 정복을 이용한 거듭제곱 구하기
c, n = map(int, input().split())
def recursive_power(x, n):
    if n == 1:
        return c
    if n % 2 == 0:
        y = recursive_power(x, n/2)
        return y * y
    else:
        y = recursive_power(x, (n-1)/2)
        return y * y * x
print(recursive_power(c, n))

# 병합 정렬
# 진행하면서 비교를 한다(정렬)
# 비교를 반복하면서 계속하서 정렬을 시도한다
# logN 이 나오는 경우와 N 이 나오는 경우를 곱해서 
# 시간 복잡도는 NlogN 이다. 

# 병합 정렬
## 그림으로 나타 낼 수는 있어야 합니다

# 퀵 정렬
# 기준아이템(pivot)중심으로 분할한다
# 기준보다 작은 것은 왼편, 큰 것은 오른편에 위치 시킨다


# 이진 검색
arr = [324, 32, 22114, 16, 48, 93, 422, 21, 316]
#1. 정렬된 상태의 데이터
arr.sort()

#2. 이진 검색 - 재귀 함수 버전
def binarySearch(low, high, target):
    if low > high:
        return -1
    # 다음 재귀를 들어가기전에 정답 판별
    mid = (low + high) // 2
    if target == arr[mid]:
        return mid

    # 다음 재귀 함수 호출 (파라미터 생각 잘하기)
    elif target < arr[mid]:
        return binarySearch(low, mid-1, target)
    else:
        return binarySearch(mid+1, high, target)
    
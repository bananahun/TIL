import requests

# 무작위 유저 정보 요청을 위한 경로
API_BASE_URL = 'https://jsonplaceholder.typicode.com/users/'

dummy_data = []

# 1부터 10까지의 사용자 정보를 요청하고 'name' 값을 dummy_data 리스트에 추가
for i in range(1, 11):
    # 각 사용자에 대한 API 요청
    response = requests.get(API_BASE_URL + str(i))

    # 응답이 성공적인 경우에만 'name' 값을 추출하여 dummy_data 리스트에 추가
    if response.status_code == 200:
        user_data = response.json()
        dummy_data.append(user_data['name'])

# 결과 출력
print(dummy_data)
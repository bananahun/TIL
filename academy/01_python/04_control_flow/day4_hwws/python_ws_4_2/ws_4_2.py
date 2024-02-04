import requests

# 무작위 유저 정보 요청을 위한 경로
API_BASE_URL = 'https://jsonplaceholder.typicode.com/users/'

dummy_data = []

# 1부터 10까지의 사용자 정보를 요청하고 'name', 'lat', 'lng', 'company' 값을 추출하여 dummy_data 리스트에 추가
for i in range(1, 11):
    # 각 사용자에 대한 API 요청
    response = requests.get(API_BASE_URL + str(i))

    # 응답이 성공적인 경우에만 'name', 'lat', 'lng', 'company' 값을 추출하여 딕셔너리로 구성
    if response.status_code == 200:
        user_data = response.json()
        
        lat = user_data['address']['geo']['lat']
        lng = user_data['address']['geo']['lng']
        
        # lat와 lng가 각각 80 미만 또는 -80 초과인 경우에만 추가
        if -80 < lat < 80 and -80 < lng < 80:
            user_info = {
                'name': user_data['name'],
                'lat': lat,
                'lng': lng,
                'company': user_data['company']['name']
            }
            
            dummy_data.append(user_info)

# 결과 출력
print(dummy_data)

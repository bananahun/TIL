import requests
from pprint import pprint as print

API_BASE_URL = 'https://jsonplaceholder.typicode.com/users/'

dummy_data = []

for i in range(1, 11):
    response = requests.get(API_BASE_URL + str(i))

    if response.status_code == 200:
        user_data = response.json()
        
        lat = user_data['address']['geo']['lat']
        lng = user_data['address']['geo']['lng']
        
        if float(lat) < 80  and float(lng) > -80:
            user_info = {
                'name': user_data['name'],
                'lat': lat,
                'lng': lng,
                'company': user_data['company']['name']
            }
            
            dummy_data.append(user_info)

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]
censored_user_list = {}

def create_user(dummy_data):
    censored_user_list = {}
    for dummy_dict in dummy_data:
        censored_user_list[dummy_dict['company']]= [dummy_dict['name']]
    return censored_user_list


def censorship(company_name):
    if company_name in black_list:
        # create_user(dummy_data)[company_name]만 하면 value값이 list에 감싸져서 나옴 ex) ['정훈'] 이런느낌
        # 그래서 create_user(dummy_data)[company_name][0]으로 list의 값을 뽑아줘야함 ex) 정훈
        print(f'{company_name}소속의 {create_user(dummy_data)[company_name][0]} 은/는 등록할 수 없습니다.')
        return False
    else:
        # censorship이 함수의 return 값을 가지고 list에 넣어야함
        # censored_user_list[company_name]= create_user(dummy_data)[company_name][0]
        print('이상 없습니다.')
        return True

censored_user_list = {}
for company_name in create_user(dummy_data):
    if censorship(company_name):
        censored_user_list[company_name] = create_user(dummy_data)[company_name][0]
        
    # if company_name in black_list:
    #     print(f'{company_name}소속의 {create_user(dummy_data)[company_name]} 은/는 등록할 수 없습니다.')
    # else:
    #     censored_user_list[company_name]= create_user(dummy_data)[company_name]
    #     print('이상 없습니다.')
        
# 리스트에 제대로 들어갔는데 출력 순서가 다름 이게 문제인데 어떻게 해결할거?
print(censored_user_list)

# def censorship():
#     pass




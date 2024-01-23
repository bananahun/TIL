import requests
import pprint

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

censored_user_list = {}
for company_name in create_user(dummy_data):
    if company_name in black_list:
        print(f'{company_name}소속의 {create_user(dummy_data)[company_name]} 은/는 등록할 수 없습니다.')
    else:
        censored_user_list[company_name]= create_user(dummy_data)[company_name]
        print('이상 없습니다.')
        
print(censored_user_list)

def censorship():
    pass



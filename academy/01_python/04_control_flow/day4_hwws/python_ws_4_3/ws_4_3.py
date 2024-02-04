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

pprint.pprint(dummy_data)

    
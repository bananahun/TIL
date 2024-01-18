import requests

API_URL ='https://jsonplaceholder.typicode.com/users/1'

response = requests.get(API_URL)

parsed_data = response.json()

dummy_data=[]

for i in range(1,11):
    dummy_data.append(parsed_data['company'],parsed_data['lat'], parsed_data['lng'],parsed_data['name'])

print(dummy_data)

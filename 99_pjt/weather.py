import requests
import pprint
API_key = 'fb225900466b377fd2bde50e646b0a6d'

lat = 37.56

lon = 126.97

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
data = requests.get(url).json()
pprint.pprint(data['weather'][0]['description'])

#추가 공부 과제
data['weather']
data.get('weather')
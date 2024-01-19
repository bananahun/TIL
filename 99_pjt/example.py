# 변수 사용법
# 파이썬

# 서버로부터 데이터를 가져와보세요


import requests

url = 'https://fakestoreapi.com/carts'
data = requests.get(url).json()
print(data)

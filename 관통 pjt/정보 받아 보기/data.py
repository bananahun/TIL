import requests
import pandas as pd
import pprint

key = '3c0641b3ddfc7e13e99f2637dc6b18aa'
# targetDt = '20220810'

url = 'http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=f5eef3421c602c6cb7ea224104795888&openStartDt=2023'

response = requests.get(url)
r_data = response.json()
pprint.print(r_data)

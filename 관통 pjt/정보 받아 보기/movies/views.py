from django.shortcuts import render
import requests
from django.conf import settings
# Create your views here.

API_KEY = settings.API_KEY

def get_movie_list(request, title='크루엘라'):
    url='https://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key='+API_KEY+'&movieNm='+title
    response = requests.get(url)
    resdata = response.text
    context = {
        'resdata':resdata
    }
    return render(request, 'movies/index.html', context)


'''
크루엘라를 검색한다!
-> 크루엘라 리스트가 뜬다 (api로 검색한번한다) => 결과가 뜬다
-> 상세페이지를 들어간다 (가져와서 쓴다,api)
'''
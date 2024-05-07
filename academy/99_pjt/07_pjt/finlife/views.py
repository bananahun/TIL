import requests
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.conf import settings
from .serializers import DepositProductsSerializer, DepositOptionsSerializer
from .models import DepositProducts, DepositOptions

# Create your views here.
BASE_URL='http://finlife.fss.or.kr/finlifeapi/'

# @api_view(['GET'])
# def index(request):
#   URL = BASE_URL + 'depositProductsSearch.json'
#   params = {
#     'auth': settings.API_KEY,
#     'topFinGrpNo': '020000',
#     'pageNo' : 1
#   }
  
#   response = requests.get(URL, params=params).json()
#   return Response({'reponse':response})  



@api_view(['GET'])
def save_deposit_products(request):
  URL = BASE_URL + 'depositProductsSearch.json'
  params = {
    'auth': settings.API_KEY,
    'topFinGrpNo': '020000',
    'pageNo' : '1'
  }
  response = requests.get(URL, params=params).json()
  
  for li in response['result']['baseList']:
    fin_prdt_cd = li.get('fin_prdt_cd','')
    kor_co_nm = li.get('kor_co_nm','')
    fin_prdt_nm = li.get('fin_prdt_nm','')
    etc_note = li.get('etc_note','')
    join_deny = li.get('join_deny',False)
    join_member = li.get('join_member','')
    join_way = li.get('join_way','')
    spcl_cnd = li.get('spcl_cnd','')

    save_data = {
      'fin_prdt_cd': fin_prdt_cd,
      'kor_co_nm' : kor_co_nm,
      'fin_prdt_nm' : fin_prdt_nm,
      'etc_note' : etc_note,
      'join_deny' : join_deny,
      'join_member' : join_member,
      'join_way' : join_way,
      'spcl_cnd' : spcl_cnd,
      }
    
    serializer = DepositProductsSerializer(data=save_data) 
    if serializer.is_valid(raise_exception=True):
            # 유효하다면, 저장
      serializer.save()
      
  for lst in response['result']['optionList']:
    product = DepositProducts.objects.get(fin_prdt_cd=lst.get('fin_prdt_cd'))
    if product:
      fin_prdt_cd = lst.get('fin_prdt_cd','')
      intr_rate_type_nm = lst.get('intr_rate_type_nm','')
      intr_rate = lst.get('intr_rate',0.0)
      intr_rate2 = lst.get('intr_rate2',0.0)
      save_trm = lst.get('save_trm',-1)
      
      save_data = {
        'product' : product,
        'fin_prdt_cd': fin_prdt_cd,
        'intr_rate_type_nm' : intr_rate_type_nm,
        'intr_rate' : intr_rate,
        'intr_rate2' : intr_rate2,
        'save_trm' : save_trm,
        }
    
      serializer = DepositOptionsSerializer(data=save_data) 
      if serializer.is_valid(raise_exception=True):
              # 유효하다면, 저장
        serializer.save(product=product)
        
  return JsonResponse({ "message": "okay!" })

@api_view(['GET','POST'])
def deposit_products(request):
  if request.method == 'GET':
    products = DepositProducts.objects.all()
    serializer = DepositProductsSerializer(products, many=True)
    return Response(serializer.data)
  else:
    serializer = DepositProductsSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)

@api_view(['GET'])
def deposit_options(request, fin_prdt_cd):
  options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
  serializer = DepositOptionsSerializer(options, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def top_rate(request):
  option = DepositOptions.objects.all().order_by('-intr_rate2')[0]
  product = DepositProducts.objects.get(fin_prdt_cd=option.fin_prdt_cd)
  serializer = DepositProductsSerializer(product)
  option_serializer = DepositOptionsSerializer(option)
  serial_dict = {'deposit_product':serializer.data, 'options': option_serializer.data}
  return Response(serial_dict)

from django.contrib import admin
from django.urls import path
from . import views


app_name = 'finlife'

urlpatterns = [
    # path('', views.index, name="index"),
    path('save-deposit-products/', views.save_deposit_products, name='save'),
    path('deposit-products/', views.deposit_products, name='deposit_products'),
    path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_options, name='deposit_options'),
    path('deposit-products/top-rate/',views.top_rate)
]
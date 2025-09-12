from django.urls import path
from . import views

app_name='articles'
urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('dinner/', views.dinner),
    path('search/', views.search),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch),
    path('articles/<int:num>/', views.detail),
]

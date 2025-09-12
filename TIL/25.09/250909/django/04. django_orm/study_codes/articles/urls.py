from django.contrib import admin
from django.urls import path
from . import views

app_name="articles"
urlpatterns = [
    path('', views.articles, name='articles'),
    path('index/', views.index, name="index"),
    path('search/', views.search, name="search"),
    path('search_result/', views.search_result, name="search_result"),
    path('detail/<int:num>', views.detail, name="detail"),
]



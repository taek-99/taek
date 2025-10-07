from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path("restaurants/", views.restaurants, name="restaurants"),
    path("best/", views.best, name="best"),
]

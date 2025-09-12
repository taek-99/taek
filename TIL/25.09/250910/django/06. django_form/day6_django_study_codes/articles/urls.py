from django.contrib import admin
from django.urls import path
from . import views

app_name='articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    # path('new/', views.new, name='new'),  # 하나로 통합할거니까 안쓸겁니다.
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    # path('<int:pk>/edit/', views.edit, name='edit'),  # 하나로 통합할거니까 제거
    path('<int:pk>/update/', views.update, name='update'),
]

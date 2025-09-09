from django.urls import path
from . import views

app_name = 'events'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/availability/', views.availability, name='availability'),
    path('<int:pk>/hold/', views.hold, name='hold'),
    path('checkout/confirm/', views.checkout_confirm, name='checkout_confirm'),
]

# urls.py (앱)
from django.urls import path
from .views import click_view

app_name = "tickets"  # 앱명 원하는 걸로
urlpatterns = [
    path("", click_view, name="click"),
]

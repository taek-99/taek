from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)  # 관리자 사이트에서 보고 싶은 모델을 등록하면 된다. 

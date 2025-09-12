from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시에만 업데이트
    updated_at = models.DateTimeField(auto_now=True)  # 수정 시 매번 업데이트 
    
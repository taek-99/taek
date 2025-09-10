from django.db import models

def articles_image_path(instance, filename):
    return f'images/{instance.title}/{filename}'

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 빈 문자열이 저장될 수 있도록 제약 조건 설정
    # 이미지 업로드를 하지 않아도 저장이 가능
    # image = models.ImageField(blank=True)  
    image = models.ImageField(blank=True, upload_to='images/')
    image2 = models.ImageField(blank=True, upload_to="%y/%m/%d/")
    image3 = models.ImageField(blank=True, upload_to=articles_image_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



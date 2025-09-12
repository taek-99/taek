from django import forms
from .models import Article

# Create your models here.
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        

# articles/forms.py
from django import forms
from .models import Article
# class ArticleForm(forms.Form):
    # title = forms.CharField(max_length=10)
    # content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields 에 연결되는 데이터에 , 찍어야하는 이유는 ?
        # field에 연결해야하는 자료형은 tuple 
        # 튜플의 본체는 (), 콤마 
        # tuple 특징
        # 변경 불가(불변) => 한 번 선언되면 바뀌면 안된다. 
        # 순서가 O , 정의된 순서 그대로 렌더링 
        fields = ('title',)
        # exclude = ('title',)

<input type="text" placeholder="Enter the title" class="my-title">
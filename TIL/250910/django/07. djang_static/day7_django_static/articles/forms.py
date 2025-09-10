from django import forms

# Form의 입력 데이터를 컨트롤하자!
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#    # CreatedAt, UpdatedAt은 사용자가 입력할 일이 없기 때문에 제외

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # 모든 필드를 포함
        fields = '__all__'
        # fields = ('content',)
        # exclude = ('content',)


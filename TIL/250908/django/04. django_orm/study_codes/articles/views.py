from django.shortcuts import render
from .models import Article

def articles(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/articles.html', context)



# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def search(request):
    return render(request, 'articles/search.html')

def search_result(request):
    request_data = request.GET
    print(request_data)
    context = {
        'num': request_data.get('num')
    }
    return render(request, 'articles/search_result.html', context)


def detail(request, num):
    context = {
        'num': num
    }
    return render(request, 'articles/detail.html', context)


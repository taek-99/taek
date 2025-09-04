from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):

    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request,"articles/index.html", context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'articles' : article
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    get_data = request.POST

    title = get_data.get('title')
    content = get_data.get('content')

    article = Article.objects.create(title=title, content=content)

    return redirect('articles:detail', article.pk)

def delete(request, pk):
    article = Article.objects.get(pk=pk)

    article.delete()

    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article' : article
    }
    return render (request, 'articles/edit.html', context)


def update(request, pk):
    update_title = request.POST.get('title')
    update_content = request.POST.get('content')

    article = Article.objects.get(pk=pk)
    article.title = update_title
    article.content = update_content
    article.save()

    return redirect('articles:detail', article.pk)
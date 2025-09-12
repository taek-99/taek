from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    data = request.POST
    title = data.get('title')
    content = data.get('content')

    print("title: ", title, content)
    article = Article.objects.create(title=title, content=content)

    return redirect('articles:detail', article.pk)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    data = request.POST
    title = data.get('title')
    content = data.get('content')

    article = Article.objects.get(pk=pk)
    article.title = title
    article.content =content 
    article.save()
    return redirect('articles:detail', article.pk)



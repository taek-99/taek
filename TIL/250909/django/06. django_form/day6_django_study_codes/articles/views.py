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

from .forms import ArticleForm

# def new(request):
#     form = ArticleForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'articles/new.html', context)

# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'form': form,
#         'article': article
#     }
#     return render(request, 'articles/edit.html', context)


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {
#         'article': article
#     }
#     return render(request, 'articles/edit.html', context)



# form 안쓴 버전
# def create(request):
#     data = request.POST
#     title = data.get('title')
#     content = data.get('content')

#     print("title: ", title, content)
#     article = Article.objects.create(title=title, content=content)

#     return redirect('articles:detail', article.pk)

# form 쓴 버전 ( POST 따로 버전)
# def create(request):
#     form = ArticleForm(request.POST)
#     if form.is_valid():
#         article = form.save()  # form 은 이미 모델과 연결되었기 때문에 바로 생성 가능 
#         return redirect('articles:detail', article.pk)  
#     context = {
#         'form': form
#     }
#     return render(request, 'articles/new.html', context)

# form도 쓰고, GEt/POST 합친 버전
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    elif request.method == "GET":  # GET Method인 경우 
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)



# form 쓴 버전 ( 분리 O )
# def update(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(request.POST, instance=article)
#     if form.is_valid():
#         form.save()
#         return redirect('articles:detila', article.pk)
#     context = {
#         'article': article,
#         'form': form
#     }
#     return render(request,'articles/edit.html', context)

# form도 쓰고, GET/POST 합친 버전
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else: 
        form = ArticleForm(instance=article)  # 생성 X , 업데이트구나
    context = {
        'article':article,
        'form': form
    }
    return render(request, 'articles/update.html', context)



def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')



# def update(request, pk):
#     data = request.POST
#     title = data.get('title')
#     content = data.get('content')

#     article = Article.objects.get(pk=pk)
#     article.title = title
#     article.content =content 
#     article.save()
#     return redirect('articles:detail', article.pk)







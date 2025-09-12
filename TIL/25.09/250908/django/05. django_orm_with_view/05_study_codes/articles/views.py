from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # 전체 게시글 조회 
    # DJango ORM => QuerySetAPI 
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

# 단일 게시글 조회 
# pk: 조회하고 싶은 게시글의 고유 ID 
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)


# 게시글 작성 페이지를 반환하는 함수 
def new(request):
    return render(request, 'articles/new.html')


# 사용자가 입력한 데이터를 입력받고, 해당 데이터를 저장하는 함수 
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article.objects.create(title=title, content=content)

    # return render(request, 'articles/create.html')
    return redirect('articles:detail', article.pk)


# 입력받은 pk 게시글을 삭제하는 로직 
def delete(request, pk):
    # 삭제부터 하자. 
    # 어떤 객체를 삭제할 지 먼저 조회를 해야한다.
    article = Article.objects.get(pk=pk).delete()

    # 삭제한 다음에 일반적으로 '삭제를 완료했습니다'
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    update_title = request.POST.get('title')
    update_content = request.POST.get('content')
    print(update_title)
    print(update_content)
    article = Article.objects.get(pk=pk)
    article.title = update_title
    article.content = update_content
    article.save()
    # 업데이트 후에는 게시글 상세페이지로 돌려보내서
    # 제대로 업데이트됐는지 확일할 수 있게 하는게 조금더 정상같죠?
    return redirect('articles:detail', article.pk)

    
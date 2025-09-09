from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def search(request):
    return render(request, 'articles/search.html')

# 검색한 결과를 화면에 보여주자..
# 검색한 결과는 어디에 들어가있어요 ??
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
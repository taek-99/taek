from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "articles/index.html")

def dinner(request):
    foods = ['치킨', '피자', '햄버거']
    context = {
        'foods' : foods
    }
    return render(request, 'articles/dinner.html', context)


def search(request):
    return render(request, 'articles/search.html')

def catch(request):

    context = {
        'name' : request.GET.get('query')
    }

    return render(request, 'articles/catch.html', context)
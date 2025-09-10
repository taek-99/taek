from django.shortcuts import render

# Create your views here.
def index(request):
    name = 'jayden'
    context = {
        'name': name,
        'name_length': len(name)
    }
    return render(request, 'articles/index.html', context)

import random
def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육', '스팸']
    pick_me = random.choice(foods)
    context = {
        'foods': foods,
        'pick_me': pick_me
    }
    return render(request, 'articles/dinner.html', context)

def search(request):
    context = {}
    return render(request, 'articles/search.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

# 아래 로직에서 클라이언트로부터 받은 데이터를 활용할 수 있다. 

def catch(request):
    context = {
        'message': request.GET.get('message')
    }
    return render(request, 'articles/catch.html', context)

def detail(request, num):
    context = {
        'num': num
    }
    return render(request, 'articles/detail.html', context)
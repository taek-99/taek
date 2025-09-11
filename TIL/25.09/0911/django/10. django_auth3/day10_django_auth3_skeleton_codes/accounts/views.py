from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout  
from django.contrib.auth.decorators import login_required
from .forms import CustomUser, CustomChangeUser

def login(request):   
    # 실제로 로그인 과정이 처리되는 경우
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')

    else:  # GET method => 로그인 페이지를 반환
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_login(request)
    return redirect("articles:index")


def signup(request):
    if request.method == 'POST':
        form = CustomUser(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUser()

    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)


def delete(request):
    request.user.delete()
    return redirect('articles:index')


def update(request):
    if request.method =='POST':
        form = CustomChangeUser(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomChangeUser(instance=request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/update.html', context)


from django.contrib.auth import update_session_auth_hash


def change_password(request):
    if request.method =='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form
    }
    return render (request, 'accounts/change_password.html', context)
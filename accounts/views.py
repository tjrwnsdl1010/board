from django.shortcuts import render, redirect
from accounts.form import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)


def login(request):
    # 이미 로그인을 한 상태인데 로그인을 다시 하는경우
    if request.user.is_authenticated:
        return redirect('posts:index')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'posts:index')
            # 1. next 인자가 있을때 => 'posts/create' or 'posts:index' => 'posts/create'
            # 2. next 인자가 없을때 => None or 'posts:index' => 'posts:index'

            # dict = {
            #     'banana': '바나나'
            # }
            # dict['apple'] => KeyError
            # dict.get('apple') => return None
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('posts:index')
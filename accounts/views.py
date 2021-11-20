from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from .forms import CustomUserCreationForm
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
# Create your views here.

@require_http_methods(['GET','POST'])
def signup(request):
    # 로그인 되어있는 사용자라면 되돌려 줌
    if request.user.is_authenticated:
        return redirect(request.GET.get('next') or 'community:index')

    # 로그인이 안되어있는 사용자일 때,
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'community:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['GET','POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('community:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'community:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('community:index')

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        me = request.user
        you = get_object_or_404(get_user_model(), pk=user_pk)
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                isFollowed=False
            else:
                you.followers.add(me)
                isFollowed=True
            context = {
                'isFollowed': isFollowed,
                'followers_count':you.followers.count(),
                'followings_count':you.followings.count(),
            }
            return JsonResponse(context)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')

# 로그인 되어있는 사용자만 profile에 접근 가능
@login_required
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person':person,
    }
    return render(request, 'accounts/profile.html', context)
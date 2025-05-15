from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView


def login_view(request):
    """ログインビュー
    ユーザー名は 'hruser' で始まる必要があります。"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not username.startswith('hruser'):
            # ユーザー名またはパスワードが空の場合の処理
            return render(request, 'registration/login.html', {'error': 'ユーザ名はheaduserで始まる必要があります'})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list-employee')
        else:
            # 認証に失敗した場合の処理
            return render(request, 'registration/login.html', {'error': 'ユーザー名またはパスワードが正しくありません'})
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('logout-success')


class LogoutSuccessView(TemplateView):
    template_name = 'registration/logout.html'
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .forms import LoginForm


def index_view(request):
    """Главная страница приложения"""
    login_form = LoginForm()
    context = {
        "login_form": login_form,
    }
    return render(request, "base.html", context)


def user_login(request):
    """Авторизация пользователя"""
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
    if is_ajax:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                username = cd.get("username")
                password = cd.get("password")
                user = authenticate(request, username=username, password=password)
                if user and user.is_active:
                    login(request, user)
                    return JsonResponse({"login_status": "success"})
    return JsonResponse({"login_status": "fail"})


def user_logout(request):
    """Выход из аккаунта пользователем"""
    logout(request)
    return redirect("accounts:index")

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from .forms import LoginForm, RegistrationForm
from .models import Profile


@require_POST
def user_login(request):
    """Авторизация пользователя"""
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
    if not is_ajax:
        return redirect("accounts:index")

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


@require_POST
def user_registration(request):
    """Регистрация пользователя"""
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
    if not is_ajax:
        return redirect("accounts:index")

    form = RegistrationForm(request.POST)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data["password1"])
        new_user.save()
        Profile.objects.create(user=new_user)
        return JsonResponse({"registration_status": "success"})

    form_errors = str(form.errors)

    return JsonResponse({"registration_status": "fail", "reg_errors": form_errors})


def user_logout(request):
    """Выход из аккаунта пользователем"""
    logout(request)
    return redirect("index:index")

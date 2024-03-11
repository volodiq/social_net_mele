from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from .forms import AccountSettingsForm, ChangePasswordForm, LoginForm, RegistrationForm
from .models import Profile


def is_ajax(request) -> bool:
    """Является ли запрос ajax-запросом"""
    return request.headers.get("X-Requested-With") == "XMLHttpRequest"


@require_POST
def user_login(request):
    """Авторизация пользователя"""
    if not is_ajax(request):
        return redirect("index:index")

    form = LoginForm(request.POST)

    if not form.is_valid():
        return JsonResponse({"login_status": "fail"})

    cd = form.cleaned_data
    username = cd.get("username")
    password = cd.get("password")

    user = authenticate(request, username=username, password=password)

    if user and user.is_active:
        login(request, user)
        return JsonResponse({"login_status": "success"})


@require_POST
def user_registration(request):
    """Регистрация пользователя"""
    if not is_ajax(request):
        return redirect("index:index")

    form = RegistrationForm(request.POST)

    if not form.is_valid():
        form_errors = str(form.errors)
        return JsonResponse({"registration_status": "fail", "reg_errors": form_errors})

    new_user = form.save(commit=False)
    new_user.set_password(form.cleaned_data["password1"])
    new_user.save()

    Profile.objects.create(user=new_user)

    return JsonResponse({"registration_status": "success"})


@login_required
def user_logout(request):
    """Выход из аккаунта пользователем"""
    logout(request)
    return redirect("index:index")


@require_POST
@login_required
def user_change_password(request):
    """Смена пароля пользователя"""
    if not is_ajax(request):
        return redirect("index:index")

    form = ChangePasswordForm(request.POST)

    if not form.is_valid():
        return JsonResponse({"change_password_status": "fail"})

    cd = form.cleaned_data
    user = request.user

    if not user.check_password(cd["current_password"]):
        return JsonResponse({"change_password_status": "fail"})

    user.set_password(cd["new_password"])
    user.save()

    return JsonResponse({"change_password_status": "success"})


@require_POST
@login_required
def user_change_image(request):
    """Смена аватарки пользователя"""
    if not is_ajax(request):
        return redirect("index:index")

    form = AccountSettingsForm(files=request.FILES)

    if not form.is_valid():
        return JsonResponse({"account_settings_status": "fail"})

    user = request.user
    user.profile.image = form.cleaned_data["image"]
    user.profile.save()

    return JsonResponse({"account_settings_status": "success"})

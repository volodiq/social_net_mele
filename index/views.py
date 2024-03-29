from django.shortcuts import render
from django.core.paginator import Paginator

from accounts.forms import (
    AccountSettingsForm,
    ChangePasswordForm,
    LoginForm,
    RegistrationForm,
)
from posts.forms import PostCreateForm, PostFastCreateForm
from posts.models import Post


def index_view(request):
    """Главная страница приложения"""

    login_form = LoginForm()
    registration_form = RegistrationForm()
    change_password_form = ChangePasswordForm()
    account_settings_form = AccountSettingsForm()
    post_fast_create_form = PostFastCreateForm()
    post_create_form = PostCreateForm()

    posts = Post.objects.all()

    context = {
        "login_form": login_form,
        "registration_form": registration_form,
        "change_password_form": change_password_form,
        "account_settings_form": account_settings_form,
        "post_fast_create_form": post_fast_create_form,
        "post_create_form": post_create_form,
        "posts": posts,
    }

    return render(request, "base.html", context)


def is_ajax(request) -> bool:
    """Является ли запрос ajax-запросом"""
    return request.headers.get("X-Requested-With") == "XMLHttpRequest"


def load_posts(request):
    """Отправляет посты при прокрутке страницы"""

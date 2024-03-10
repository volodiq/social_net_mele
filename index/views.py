from django.shortcuts import render

from accounts.forms import LoginForm, RegistrationForm, ChangePasswordForm


def index_view(request):
    """Главная страница приложения"""
    login_form = LoginForm()
    registration_form = RegistrationForm()
    change_password_form = ChangePasswordForm()
    context = {
        "login_form": login_form,
        "registration_form": registration_form,
        "change_password_form": change_password_form,
    }
    return render(request, "base.html", context)

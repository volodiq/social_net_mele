from django.shortcuts import render

from accounts.forms import LoginForm, RegistrationForm


def index_view(request):
    """Главная страница приложения"""
    login_form = LoginForm()
    registration_form = RegistrationForm()
    context = {
        "login_form": login_form,
        "registration_form": registration_form,
    }
    return render(request, "base.html", context)

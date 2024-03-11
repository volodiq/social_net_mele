from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    """Форма для входа в аккаунт пользователя"""

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "id": "form2Example1",
                "class": "form-control",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "id": "form2Example2",
                "class": "form-control",
            }
        )
    )


class RegistrationForm(forms.ModelForm):
    """Форма для регистрации аккаунта"""

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "PASSWORD*"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "PASSWORD CONFIRM*"}
        )
    )

    class Meta:
        model = get_user_model()
        fields = ("username", "first_name", "last_name", "email")
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "USERNAME*"}
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "FIRST NAME*"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "LAST NAME*"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "EMAIL*"}
            ),
        }

    def clean_password2(self):
        """Сравнения введенных паролей"""
        cd = self.cleaned_data
        if cd.get("password1") != cd.get("password2"):
            raise ValidationError("Passwords don't match")
        return cd.get("password2")

    def clean_email(self):
        cd = self.cleaned_data
        user = get_user_model()

        if user.objects.get(email=cd.get("email")).exist():
            raise ValidationError("Email already registered")

        return cd.get("email")


class ChangePasswordForm(forms.Form):
    """Форма смены пароля пользователя"""

    current_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "CURRENT PASSWORD*"}
        )
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "NEW PASSWORD*"}
        )
    )


class AccountSettingsForm(forms.Form):
    """Настройки аккаунта пользователя"""

    image = forms.ImageField()

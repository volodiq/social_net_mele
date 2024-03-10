from accounts import views
from django.urls import path

app_name = "accounts"

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("registration/", views.user_registration, name="registration"),
]

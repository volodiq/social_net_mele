from accounts import views
from django.urls import path

app_name = "accounts"

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("registration/", views.user_registration, name="registration"),
    path("change_password/", views.user_change_password, name="change_password"),
    path("change_image/", views.user_change_image, name="change_image"),
]

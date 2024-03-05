from accounts import views
from django.urls import path

app_name = "accounts"

urlpatterns = [
    path("", views.index_view, name="index"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
]

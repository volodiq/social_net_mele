from django.urls import path

from posts import views

app_name = "posts"

urlpatterns = [
    path("fast_create/", views.fast_create_post, name="fast_create"),
    path("create/", views.create_post, name="create"),
    path("like/", views.like, name="like"),
]

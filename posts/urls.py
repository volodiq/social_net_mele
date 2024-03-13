from django.urls import path

from posts import views

app_name = "posts"

urlpatterns = [
    path("fast_create/", views.fast_create_post, name="fast_create"),
    # create default
    path("like/", views.like, name="like"),
]

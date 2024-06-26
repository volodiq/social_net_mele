from django.contrib import admin
from django.urls import include, path
from social_core.pipeline import social_auth

from .settings import DEBUG, MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("index.urls")),
    path("accounts/", include("accounts.urls")),
    path("social_auth/", include("social_django.urls", namespace="social_auth")),
    path("posts/", include("posts.urls")),
]

if DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

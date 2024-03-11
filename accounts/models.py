from django.contrib.auth import get_user_model
from django.db import models


class Profile(models.Model):
    """Профиль пользователя"""

    user = models.OneToOneField(
        get_user_model(),
        related_name="profile",
        verbose_name="user profile",
        on_delete=models.CASCADE,
    )

    image = models.ImageField(
        upload_to="users/%Y/%m/%d", default="default_user.jpg", blank=True
    )

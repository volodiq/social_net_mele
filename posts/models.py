from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    """Посты пользователей"""

    author = models.ForeignKey(
        get_user_model(),
        related_name="post_created",
        verbose_name="Автор поста",
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    image = models.ImageField(upload_to="posts/%Y/%m/%d", blank=True, null=True)
    users_like = models.ManyToManyField(
        get_user_model(),
        related_name="posts_like",
        verbose_name="Пользователи поставившие лайк",
        blank=True,
    )

    class Meta:
        indexes = (models.Index(fields=["-created"]),)
        ordering = ["-created"]

    def __str__(self):
        return self.text[:30]

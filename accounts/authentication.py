from .models import Profile


def create_profile(backend, user, *args, **kwargs):
    """Создает профиль если его не существует при входе через social-auth"""
    Profile.objects.get_or_create(user=user)

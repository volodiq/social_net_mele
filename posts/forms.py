from django import forms

from posts.models import Post


class PostFastCreateForm(forms.ModelForm):
    """Быстрое создание поста без картинки"""

    class Meta:
        model = Post
        fields = ("text",)
        widgets = {
            "text": forms.TextInput(
                attrs={
                    "placeholder": "What's on your mind about Django?",
                    "id": "create-post",
                }
            )
        }


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("text", "image")
        widgets = {
            "text": forms.Textarea(
                attrs={
                    "placeholder": "Text...",
                }
            )
        }

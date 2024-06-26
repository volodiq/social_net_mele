from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from index.views import is_ajax
from posts.forms import PostCreateForm, PostFastCreateForm
from posts.models import Post
from actions.utils import create_action


@login_required
@require_POST
def create_post(request):
    """Создание поста"""
    if not is_ajax(request):
        return redirect("<Up>index:index")

    form = PostCreateForm(request.POST)

    if not form.is_valid():
        return redirect("index:index")

    cd = form.cleaned_data

    post = Post(
        author=request.user, text=cd.get("text"), image=request.FILES.get("image")
    )
    post.save()

    create_action(request.user, "Create post", post)

    return JsonResponse({"create_post_status": "success"})


@login_required
@require_POST
def fast_create_post(request):
    """Быстрое создание поста без картинки"""
    if not is_ajax(request):
        return redirect("index:index")

    form = PostFastCreateForm(request.POST)

    if not form.is_valid():
        return redirect("index:index")

    post = Post(author=request.user, text=form.cleaned_data["text"])
    post.save()

    create_action(request.user, "Create post", post)

    return JsonResponse({"create_post_status": "success"})


@login_required
@require_POST
def like(request):
    """Ставит или убирает лайк на пост"""
    if not is_ajax(request):
        return redirect("index:index")

    post_id = request.POST.get("post_id")
    post = Post.objects.get(pk=post_id)

    if request.user in post.users_like.all():
        post.users_like.remove(request.user)
        return JsonResponse({"like_status": "remove"})

    post.users_like.add(request.user)
    create_action(request.user, "like", post)

    return JsonResponse({"like_status": "add"})

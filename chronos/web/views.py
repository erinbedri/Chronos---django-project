from django.shortcuts import render
from chronos.post.models import Post


def show_homepage(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'common/index.html', context)













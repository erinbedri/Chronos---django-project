from django.shortcuts import render, redirect

from chronos.post.forms import PostCommentForm
from chronos.post.models import Post, PostComment


def show_post(request, pk):
    post = Post.objects.get(pk=pk)
    comments = PostComment.objects.filter(post_id=pk)
    comment_count = PostComment.objects.filter(post_id=pk).count()

    if request.method == 'POST':
        form = PostCommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('show post', pk)
    else:
        form = PostCommentForm()

    context = {
        'post': post,
        'form': form,
        'comments': comments,
        'comment_count': comment_count,
    }
    return render(request, 'post/post_details.html', context)
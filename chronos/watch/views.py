import os

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from chronos.watch.forms import CreateWatchForm, WatchCommentForm, EditWatchForm, DeleteWatchForm
from chronos.watch.models import Watch, WatchComment


def show_all_watches(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    watches = Watch.objects \
        .filter(
            Q(brand__icontains=q) |
            Q(model__icontains=q) |
            Q(style__icontains=q) |
            Q(year__icontains=q) |
            Q(condition__icontains=q) |
            Q(description__icontains=q) |
            Q(owner__username=q))\
        .order_by('-created_at')

    brands = {watch.brand for watch in Watch.objects.all()}
    styles = {watch.style for watch in Watch.objects.all()}

    context = {
        'watches': watches,
        'brands': brands,
        'styles': styles,
    }
    return render(request, 'common/../../templates/watch/watch_show_all.html', context)


@login_required
def add_watch(request):
    if request.method == 'POST':
        form = CreateWatchForm(request.POST, request.FILES)
        if form.is_valid():
            watch = form.save(commit=False)
            watch.owner = request.user
            watch.save()
            return redirect('show dashboard')
    else:
        form = CreateWatchForm()

    context = {
        'form': form,
    }
    return render(request, 'watch/watch_add.html', context)


def show_watch(request, pk):
    watch = Watch.objects.get(pk=pk)
    comments = WatchComment.objects.filter(watch_id=pk)
    comment_count = WatchComment.objects.filter(watch_id=pk).count()
    like_count = Watch.like_count(watch)

    liked = False
    if watch.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == 'POST':
        form = WatchCommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.watch = watch
            new_comment.author = request.user
            new_comment.save()
            return redirect('show watch', pk)
    else:
        form = WatchCommentForm()

    context = {
        'watch': watch,
        'comment_form': form,
        'comments': comments,
        'comment_count': comment_count,
        'like_count': like_count,
        'liked': liked,
    }
    return render(request, 'watch/watch_details.html', context)


@login_required
def edit_watch(request, pk):
    watch = Watch.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditWatchForm(request.POST, request.FILES, instance=watch)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')
    else:
        form = EditWatchForm(instance=watch)

    context = {
        'watch': watch,
        'form': form
    }
    return render(request, 'watch/watch_edit.html', context)


@login_required
def delete_watch(request, pk):
    watch = Watch.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeleteWatchForm(request.POST, request.FILES, instance=watch)
        if form.is_valid():
            image_path = watch.image.path
            os.remove(image_path)
            watch.delete()
            return redirect('show dashboard')
    else:
        form = DeleteWatchForm(instance=watch)

    context = {
        'watch': watch,
        'form': form
    }
    return render(request, 'watch/watch_delete.html', context)


@login_required
def like_watch(request, pk):
    watch = Watch.objects.get(pk=pk)
    liked = False

    if watch.likes.filter(id=request.user.id).exists():
        watch.likes.remove(request.user)
        liked = False
    else:
        watch.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('show watch', args=[str(pk)]))

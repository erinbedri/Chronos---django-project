import os

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from chronos.web.forms import CreateWatchForm, DeleteWatchForm, EditWatchForm, EditProfileForm, \
    DeleteProfileForm, NewUserForm, PrettyAuthenticationForm, WatchCommentForm, PostCommentForm
from chronos.web.models import Watch, WatchComment, Post, PostComment


def show_homepage(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)


def show_dashboard(request):
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

    return render(request, 'dashboard.html', context)


def register_profile(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('show dashboard')
        messages.error(request, 'Unsuccessful registration. Invalid information.')
    else:
        form = NewUserForm()

    context = {
        'form': form,
    }

    return render(request, 'profile_register.html', context)


def login_profile(request):
    if request.method == 'POST':
        form = PrettyAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}!')
                return redirect('show dashboard')
            else:
                messages.error(request, 'Invalid username or password!')
        else:
            messages.error(request, 'Invalid username or password!')
    form = PrettyAuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'profile_login.html', context)


@login_required
def logout_profile(request):
    logout(request)
    messages.info(request, 'You are successfully logged out.')
    return redirect('show homepage')


@login_required
def show_profile(request):
    profile = request.user
    watch_count = len(Watch.objects.filter(owner=profile))

    context = {
        'profile': profile,
        'watch_count': watch_count,
    }

    return render(request, 'profile_details.html', context)


@login_required
def edit_profile(request):
    profile = request.user

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profile_edit.html', context)


@login_required
def delete_profile(request):
    profile = request.user

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile.delete()
            return redirect('show homepage')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profile_delete.html', context)


@login_required
def add_watch(request):
    profile = request.user

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
        'profile': profile,
    }

    return render(request, 'watch_add.html', context)


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

    return render(request, 'watch_details.html', context)


@login_required
def edit_watch(request, pk):
    profile = request.user
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
        'profile': profile,
        'form': form
    }

    return render(request, 'watch_edit.html', context)


@login_required
def delete_watch(request, pk):
    profile = request.user
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
        'profile': profile,
        'form': form
    }

    return render(request, 'watch_delete.html', context)


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

    return render(request, 'post_details.html', context)

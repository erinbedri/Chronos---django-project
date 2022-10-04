import os

from django.contrib import messages
from django.contrib.auth import login
from django.db.models import Q
from django.shortcuts import render, redirect
from chronos.web.forms import CreateWatchForm, DeleteWatchForm, EditWatchForm, EditProfileForm, \
    DeleteProfileForm, NewUserForm
from chronos.web.models import Profile, Watch


def get_profile():
    profile = Profile.objects.all().first()
    return profile


def show_homepage(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'index.html', context)


def show_dashboard(request):
    profile = get_profile()

    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    watches = Watch.objects \
        .filter(
            Q(brand__icontains=q) |
            Q(model__icontains=q) |
            Q(style__icontains=q) |
            Q(year__icontains=q) |
            Q(condition__icontains=q) |
            Q(description__icontains=q))\
        .order_by('-created_at')

    brands = {watch.brand for watch in Watch.objects.all()}
    styles = {watch.style for watch in Watch.objects.all()}

    context = {
        'profile': profile,
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


def show_profile(request):
    profile = get_profile()
    watch_count = len(Watch.objects.filter(owner=profile))

    context = {
        'profile': profile,
        'watch_count': watch_count,
    }

    return render(request, 'profile_details.html', context)


def edit_profile(request):
    profile = get_profile()

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


def delete_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            image_path = profile.image.path
            os.remove(image_path)
            profile.delete()
            return redirect('show homepage')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profile_delete.html', context)


def add_watch(request):
    profile = get_profile()

    if request.method == 'POST':
        form = CreateWatchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')
    else:
        form = CreateWatchForm()

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'watch_add.html', context)


def show_watch(request, pk):
    profile = get_profile()
    watch = Watch.objects.get(pk=pk)

    context = {
        'watch': watch,
        'profile': profile,
    }

    return render(request, 'watch_details.html', context)


def edit_watch(request, pk):
    profile = get_profile()
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


def delete_watch(request, pk):
    profile = get_profile()
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

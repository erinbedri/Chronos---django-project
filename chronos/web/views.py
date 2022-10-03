from django.shortcuts import render, redirect

from chronos.web.forms import RegisterProfileForm, CreateWatchForm, DeleteWatchForm, EditWatchForm, EditProfileForm
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
    watches = Watch.objects.all()

    context = {
        'profile': profile,
        'watches': watches,
    }

    return render(request, 'dashboard.html', context)


def register_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = RegisterProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show homepage')
    else:
        form = RegisterProfileForm()

    context = {
        'form': form,
        'profile': profile,
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


def add_watch(request):
    profile = get_profile()

    if request.method == 'POST':
        form = CreateWatchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show watch')
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


from django.shortcuts import render, redirect

from chronos.web.forms import RegisterProfileForm, CreateWatchForm
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

    return render(request, 'register.html', context)


def show_profile(request):
    profile = get_profile()
    watch_count = len(Watch.objects.filter(owner=profile))

    context = {
        'profile': profile,
        'watch_count': watch_count,
    }

    return render(request, 'profile.html', context)


def add_watch(request):
    profile = get_profile()

    if request.method == 'POST':
        form = CreateWatchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show homepage')
    else:
        form = CreateWatchForm()

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'add_watch.html', context)





from django.shortcuts import render, redirect

from chronos.web.forms import RegisterProfileForm
from chronos.web.models import Profile


def get_profile():
    profile = Profile.objects.all().first()
    return profile


def show_homepage(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'index.html', context)


def register_profile(request):
    if request.method == 'POST':
        form = RegisterProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show homepage')
    else:
        form = RegisterProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'register.html', context)


def show_profile(request):
    return render(request, 'profile.html')

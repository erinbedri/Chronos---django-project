from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from chronos.user_profile.forms import NewUserForm, PrettyAuthenticationForm, EditProfileForm, DeleteProfileForm
from chronos.web.models import Watch


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
    return render(request, 'profile/profile_register.html', context)


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
    return render(request, 'profile/profile_login.html', context)


@login_required
def logout_profile(request):
    logout(request)
    messages.info(request, 'You are successfully logged out.')
    return redirect('show homepage')


@login_required
def show_profile(request):
    watch_count = len(Watch.objects.filter(owner=request.user))

    context = {
        'watch_count': watch_count,
    }
    return render(request, 'profile/profile_details.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('show profile')
    else:
        form = EditProfileForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'profile/profile_edit.html', context)


@login_required
def delete_profile(request):
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            request.user.delete()
            return redirect('show homepage')
    else:
        form = DeleteProfileForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'profile/profile_delete.html', context)
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from chronos.user_profile.forms import NewUserForm, PrettyAuthenticationForm, EditProfileForm, DeleteProfileForm
from chronos.watch.models import Watch

REGISTRATION_SUCCESS_MESSAGE = 'Registration successful!'
REGISTRATION_ERROR_MESSAGE = 'Unsuccessful registration. Invalid information.'

LOGIN_SUCCESS_MESSAGE = 'You are successfully logged in '
LOGIN_ERROR_MESSAGE = 'Invalid username or password!'

LOGOUT_SUCCESS_MESSAGE = 'You are successfully logged out.'

PROFILE_EDIT_SUCCESS_MESSAGE = 'You successfully updated your profile information!'

PROFILE_DELETE_SUCCESS_MESSAGE = 'You successfully deleted your profile information!'


def register_profile(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, REGISTRATION_SUCCESS_MESSAGE)
            return redirect('show dashboard')
        else:
            messages.error(request, REGISTRATION_ERROR_MESSAGE)
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
                messages.success(request, LOGIN_SUCCESS_MESSAGE + f'as {username}!')
                return redirect('show dashboard')
            else:
                messages.error(request, LOGIN_ERROR_MESSAGE)
        else:
            messages.error(request, LOGIN_ERROR_MESSAGE)

    form = PrettyAuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'profile/profile_login.html', context)


@login_required
def logout_profile(request):
    logout(request)
    messages.success(request, LOGOUT_SUCCESS_MESSAGE)
    return redirect('show homepage')


@login_required
def show_profile(request):
    watch_count = Watch.objects.filter(owner=request.user).count()

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
            messages.success(request, PROFILE_EDIT_SUCCESS_MESSAGE)
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
            messages.success(request, PROFILE_DELETE_SUCCESS_MESSAGE)
            return redirect('show homepage')
    else:
        form = DeleteProfileForm(instance=request.user)

    context = {
        'form': form
    }

    return render(request, 'profile/profile_delete.html', context)

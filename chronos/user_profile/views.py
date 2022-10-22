from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View

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
            messages.error(request, form.errors)
    else:
        form = NewUserForm()

    context = {
        'form': form,
    }

    return render(request, 'user_profile/profile_register.html', context)


# class RegisterView(View):
#     form_class = NewUserForm
#     template_name = 'user_profile/profile_register.html'
#
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('show homepage')
#
#         return super(RegisterView, self).dispatch(request, *args, **kwargs)
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, REGISTRATION_SUCCESS_MESSAGE)
#             return redirect('show dashboard')
#         else:
#             messages.error(request, REGISTRATION_ERROR_MESSAGE)
#
#         return render(request, self.template_name, {'form': form})


def login_profile(request):
    if request.method == 'POST':
        form = PrettyAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data.get('remember_me')
            user = authenticate(username=username, password=password)
            if user is not None:
                if not remember_me:
                    request.session.set_expiry(0)
                    request.session.modified = True
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

    return render(request, 'user_profile/profile_login.html', context)


@login_required
def logout_profile(request):
    logout(request)
    messages.success(request, LOGOUT_SUCCESS_MESSAGE)
    return redirect('show homepage')


@login_required
def show_profile(request):
    watch_count = Watch.objects.filter(owner=request.user).count()
    total_paid = sum(
        [watch.price_paid if watch.price_paid is not None else 0 for watch in Watch.objects.filter(owner=request.user)])

    context = {
        'watch_count': watch_count,
        'total_paid': total_paid,
    }

    return render(request, 'user_profile/profile_details.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, PROFILE_EDIT_SUCCESS_MESSAGE)
            return redirect('show profile')
        else:
            messages.error(request, form.errors)
    else:
        form = EditProfileForm(instance=request.user)

    context = {
        'form': form
    }

    return render(request, 'user_profile/profile_edit.html', context)


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

    return render(request, 'user_profile/profile_delete.html', context)

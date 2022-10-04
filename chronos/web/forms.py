from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from chronos.web.models import Profile, Watch

"""
class RegisterProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')
"""


class NewUserForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        max_length=30,
        widget=forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                    'class': 'form-control',
                }
        )
    )
    last_name = forms.CharField(
        required=True,
        max_length=30,
        widget=forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                    'class': 'form-control',
                }
        )
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                    'class': 'form-control',
                }
        )
    )
    username = forms.CharField(
        required=True,
        max_length=30,
        widget=forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                    'class': 'form-control',
                }
        )
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
                attrs={
                    'placeholder': 'Password',
                    'class': 'form-control',
                }
        )
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
                attrs={
                    'placeholder': 'Confirm Password',
                    'class': 'form-control',
                }
        )
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = '*First Name'
        self.fields['last_name'].label = "*Last Name"
        self.fields['email'].label = '*Email Address'
        self.fields['username'].label = "*Username"
        self.fields['password1'].label = '*Password'
        self.fields['password2'].label = "*Confirm Password"

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()


class CreateWatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = ('owner', 'brand', 'model', 'reference_number', 'year', 'style', 'condition', 'description', 'image')
        widgets = {
            'owner': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'brand': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'model': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'reference_number': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'year': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'style': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'condition': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 1
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 2
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }


class DeleteWatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = ()


class EditWatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = ('owner', 'brand', 'model', 'reference_number', 'year', 'style', 'condition', 'description', 'image')
        widgets = {
            'owner': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'brand': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'model': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'reference_number': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'year': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'style': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'condition': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 1
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 2
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }

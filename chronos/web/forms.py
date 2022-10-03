from django import forms

from chronos.web.models import Profile, Watch


class RegisterProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')


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

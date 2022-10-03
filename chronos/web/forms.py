from django import forms

from chronos.web.models import Profile, Watch


class RegisterProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')


class CreateWatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = ('owner', 'brand', 'model', 'reference_number', 'year', 'style', 'condition', 'description', 'image')


class DeleteWatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = ()


class EditWatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = ('owner', 'brand', 'model', 'reference_number', 'year', 'style', 'condition', 'description', 'image')


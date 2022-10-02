from django import forms

from chronos.web.models import Profile


class RegisterProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')


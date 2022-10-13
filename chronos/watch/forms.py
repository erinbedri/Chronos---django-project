from django import forms

from chronos.watch.models import Watch, WatchComment


class CreateWatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = ('brand', 'model', 'reference_number', 'year', 'style', 'condition', 'description', 'image')
        widgets = {
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
                    'rows': 3
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
        fields = ('brand', 'model', 'reference_number', 'year', 'style', 'condition', 'description', 'image')
        widgets = {
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
                    'rows': 3
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }


class WatchCommentForm(forms.ModelForm):
    class Meta:
        model = WatchComment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your comment',
                    'rows': 2,
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].label = ''
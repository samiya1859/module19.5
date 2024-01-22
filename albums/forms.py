from django import forms
from .models import AlbumModel


class AlbumModelForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = '__all__'
        widgets = {
            'releaseDate': forms.DateInput(attrs={'type': 'date'}),
        }


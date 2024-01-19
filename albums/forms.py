from django import forms
from .models import MusicianModel


class AlbumModelForm(forms.ModelForm):
    class Meta:
        model = MusicianModel
        fields = '__all__'

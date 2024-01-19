from django import forms
from .models import MusicianModel

class MusicianModelForm(forms.ModelForm):
    class Meta:
        model = MusicianModel
        fields = '__all__'
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = MusicianModel
        exclude = ['instrument_type']

class ChangeUserForm(forms.ModelForm):
    password = None
    class Meta:
        model = MusicianModel
        fields = '__all__'

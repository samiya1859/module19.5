from django import forms
from .models import MusicianModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class MusicianModelForm(forms.ModelForm):
    class Meta:
        model = MusicianModel
        fields = '__all__'
    

class MusicianLoginForm(AuthenticationForm):
    def __init__(self,request,*args,**kwargs):
        super().__init__(*args,**kwargs) 

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class ChangeUserForm(forms.ModelForm):
    password = None
    class Meta:
        model = MusicianModel
        fields = '__all__'

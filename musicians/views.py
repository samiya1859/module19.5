from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponse as HttpResponse
from django.shortcuts import render,redirect
from .forms import MusicianModelForm,ChangeUserForm,RegistrationForm,MusicianLoginForm,User
from django.contrib import messages
from .models import MusicianModel
from django.views.generic import CreateView,UpdateView,DeleteView,TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib import messages

class MusicianCreateView(CreateView):
    model = MusicianModel
    form_class = MusicianModelForm
    template_name= 'addMusician.html'
    success_url = reverse_lazy('addMusician')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request,'Added musician Successfully')
        return response

class RegisterView(CreateView):
    model=User
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('user_login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request,'Registration successfully done')
        return response 



class editMusicianView(UpdateView):
    model = MusicianModel
    form_class = MusicianModelForm
    template_name = 'addMusician.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg='id'

class MusicianDeleteView(DeleteView):
    model = MusicianModel
    success_url = reverse_lazy('musician')
    pk_url_kwarg='id'
    template_name = 'musician.html'

# musicianprofile
class MusicianProfileView(TemplateView):
    model = MusicianModel
    template_name = 'musician.html'
    success_url = reverse_lazy('musician')
    
        
    
    

class MusicianLoginView(LoginView):
    template_name = 'login.html'
    form_class = MusicianLoginForm
    def get_success_url(self):
        return reverse_lazy('home')
    def form_valid(self,form):
        messages.success(self.request,'LOgged in Successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request,'Logging information incorrect')
        return super().form_invalid(form)
    
   
def user_logout(request):
    logout(request)
    messages.success(request,'Loggedout Successfully')
    return redirect('home')

     
# class MusicianLogoutView(LogoutView):
#     def get_next_page(self):
#         messages.success(self.request,'Logged out successfully')
#         return reverse_lazy('home')

# class MusicianLogoutView(LogoutView):
#     next_page = reverse_lazy('home')  # Replace 'home' with the actual name of your homepage URL

#     def dispatch(self, request, *args, **kwargs):
#         messages.success(request, 'Logged out successfully')
#         return super().dispatch(request, *args, **kwargs)



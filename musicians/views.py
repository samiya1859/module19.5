from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponse as HttpResponse
from django.shortcuts import render,redirect
from .forms import MusicianModelForm,ChangeUserForm,RegistrationForm
from django.contrib import messages
from .models import MusicianModel
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView

class MusicianCreateView(CreateView):
    model = MusicianModel
    form_class = MusicianModelForm
    template_name= 'addMusician.html'
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request,'Added musician Successfully')
        return response

class RegisterView(CreateView):
    model=MusicianModel
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
    pk_url_kwarg='pk'

class MusicianDeleteView(DeleteView):
    model = MusicianModel
    success_url = reverse_lazy('musician')
    pk_url_kwarg='pk'
    template_name = 'musician.html'

class MusicianLoginView(LoginView):
    template_name = 'addMusician.html'
    form_class = MusicianModelForm
    def get_success_url(self):
        return reverse_lazy('home')
    def form_valid(self,form):
        messages.success(self.request,'LOgged in Successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request,'Logging information incorrect')
        return super().form_invalid(form)
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['type'] = 'Login'
    #     return context

     
class MusicianLogoutView(LogoutView):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'Logged out successfuly')
        return super().dispatch(request,*args, **kwargs)



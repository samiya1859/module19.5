from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from . import models
from . import forms
# Create your views here.


# Adding album
@method_decorator(login_required,name='dispatch')
class AddAlbumView(CreateView):
    model = models.AlbumModel
    form_class = forms.AlbumModelForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('musician')
    def form_valid(self, form):
        form.instance.musicians = self.request.user
        return super().form_valid(form)



# editing Album
@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    model = models.AlbumModel
    form_class = forms.AlbumModelForm
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('musician')


# deleting album
@method_decorator(login_required, name='dispatch')    
class DeleteAlbumView(DeleteView):
    model = models.AlbumModel
    template_name = 'delete.html'
    success_url = reverse_lazy('musician')
    pk_url_kwarg='id'


# detail of album
class AlbumDetailView(DetailView):
    model = models.AlbumModel
    pk_url_kwarg = 'id'
    template_name = 'album_details.html'
    def album_detail(request,id):
        album = models.AlbumModel.objects.get(pk=id)
        return render(request,'album_details.html',{'item':album})








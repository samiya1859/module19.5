from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from albums.models import AlbumModel
# def home(request):
#     return render(request,'home.html')

class HomeView(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data= AlbumModel.objects.all()
        context['data']=data
        return context 
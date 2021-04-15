from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from CrudApp import models
from django.urls import reverse_lazy

# Create your views here.
app_name='CrudApp'


class IndexView(ListView):
    context_object_name = 'musician_list'
    model=models.Musician
    template_name='CrudApp/index.html'


class MusicianDetail(DetailView):
    context_object_name = 'musician'
    model = models.Musician
    template_name = 'CrudApp/musician_details.html'

class AddMusician(CreateView):
    model=models.Musician
    fields=('first_name','last_name','instrument')
    template_name='CrudApp/musician_form.html' #optional

class UpdateMusician(UpdateView):
    fields = ('first_name','last_name', 'instrument')
    model = models.Musician
    template_name = 'CrudApp/musician_form.html'

class DeletMusician(DeleteView):
    context_object_name = 'musician'
    model = models.Musician
    success_url = reverse_lazy("CrudApp:index")
    template_name = 'CrudApp/delete_musician.html'

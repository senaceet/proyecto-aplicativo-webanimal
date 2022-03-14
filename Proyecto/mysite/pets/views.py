from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Pets

class PetsListView(ListView): 
    template_name = 'index.html'
    queryset = Pets.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pets'] = context['pets_list']
        print(context)
        return context

class PetsDetailView(DetailView):
    model = Pets
    template_name = 'pets/pet.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        print (context)
        return context

class PetsSearchListView(ListView):
    template_name = 'pets/search.html'

    def get_queryset(self):
        return Pets.objects.filter(name=self.query())

    def query(self):
        return self.request.GET.get('q')
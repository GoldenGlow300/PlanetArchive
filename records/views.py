from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls.base import get_script_prefix
from records.forms import PlanetForm
from .models import Planet
from django.views.generic import ListView, DetailView, FormView, UpdateView
from django.urls import reverse

# Create your views here.

class RecordListView(ListView):
    queryset = Planet.objects.all()
    context_object_name = 'planet_records'
    template_name = 'list.html'

class RecordDetailView(DetailView): 
    model = Planet
    context_object_name = 'planet'
    template_name = 'detail.html'

    def get_object(self, queryset=None):
        slug = self.kwargs['name']
        planet = get_object_or_404(Planet, name=slug)

        return planet

class RecordUpdateView(UpdateView):
    model = Planet
    fields = ['name', 'ordinality', 'description', 'size', 'distance']
    template_name = "update.html"
    success_url = "/records/"

    def get_object(self, queryset=None):
        slug = self.kwargs['name']
        planet = get_object_or_404(Planet, name=slug)

        return planet
    
class RecordFormView(FormView):
    form_class = PlanetForm
    template_name = "add.html"
    success_url = "/records/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def record_delete(request, name):
    planet = get_object_or_404(Planet, name = name)
    planet.delete()

    return HttpResponseRedirect(reverse('records:record_list'))

    




from django.shortcuts import get_object_or_404
from records.forms import PlanetForm
from .models import Planet
from django.views.generic import ListView, DetailView, FormView
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
    
class RecordFormView(FormView):
    form_class = PlanetForm
    template_name = "add.html"
    success_url = "/records/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

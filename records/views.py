from django.shortcuts import get_object_or_404, render

from records.forms import PlanetForm
from django.http import HttpResponseRedirect
from .models import Planet
from django.views.generic import ListView
from django.urls import reverse

# Create your views here.

class RecordListView(ListView):
    queryset = Planet.objects.all()
    context_object_name = 'planet_records'
    template_name = 'list.html'

def record_detail(request, planet_name):
    planet = get_object_or_404(Planet, name= planet_name)

    return render(request, 'detail.html', {'planet': planet})
    
def record_add(request):
    if request.method == "POST":
        new_form = PlanetForm(request.POST)

        if new_form.is_valid():
            new_form.save()
            return HttpResponseRedirect(reverse('records:record_list'))
    else:
        new_form = PlanetForm()
    
    return render(request, 'add.html', {'form': new_form})

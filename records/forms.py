from .models import Planet
from django import forms

class PlanetForm(forms.ModelForm):    
    class Meta:
        model = Planet
        fields = ("name", "ordinality", "description", "size", "distance")

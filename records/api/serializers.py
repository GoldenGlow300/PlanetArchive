from django.db import models
from rest_framework import serializers
from ..models import Planet

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ["name", "description", "ordinality", "size", "distance"]
        lookup_field = 'name'
        # extra_kwargs = { 'path': {'lookup_field' :'name'} }
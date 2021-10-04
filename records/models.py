from django.db import models
from django.urls import reverse

# Create your models here.
class Planet(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    ordinality = models.IntegerField(unique=True)
    size = models.FloatField()
    distance = models.FloatField()

    def get_absolute_url(self):
        return reverse("records:record_detail", kwargs={'name': self.name})
    

    class Meta: 
        ordering = ('ordinality',)
    
# this func is the default human redable representation of the object
    def __str__(self):
        return self.name
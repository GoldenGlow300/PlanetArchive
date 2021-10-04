from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('records/', include('records.urls', namespace='records'))
]

from rest_framework import generics
from rest_framework.response import Response
from ..models import Planet
from .serializers import RecordSerializer

# curl -X POST -d '{"name":"Earth","description":"Hottest Planet","ordinality":3,"size":1.0,"distance":4.5}' 
# -H 'Content-Type: application/json' http://127.0.0.1:8000/api/records/add/
class RecordCreateView(generics.CreateAPIView):
    serializer_class = RecordSerializer

# curl -X DELETE http://127.0.0.1:8000/api/records/Earth/delete/
class RecordDeleteView(generics.DestroyAPIView):
    queryset = Planet.objects.all() #optimize this later
    serializer_class = RecordSerializer
    lookup_field = 'name'

# curl -X PUT -d '{"name":"Earth","description":"Hottest Planet","ordinality":3,"size":1.0,"distance":4.5}' 
# -H 'Content-Type: application/json' http://127.0.0.1:8000/api/records/<name>/update/
class RecordUpdateView(generics.UpdateAPIView):
    queryset = Planet.objects.all()
    serializer_class = RecordSerializer
    lookup_field = 'name'

# curl http://127.0.0.1:8000/api/records/Mercury/ # requests Mercury Planet
# curl http://127.0.0.1:8000/api/records/ | json_pp # formats JSON
class RecordListView(generics.ListAPIView):
    queryset = Planet.objects.all()
    serializer_class = RecordSerializer

class RecordDetailView(generics.RetrieveAPIView):
    queryset = Planet.objects.all()
    serializer_class = RecordSerializer
    lookup_field = 'name'

# queryset: The base QuerySet to use to retrieve objects
# serializer_class: The class to serialize objects

# {"name":"Mercury","description":"Hottest Planet","ordinality":1,"size":1.0,"distance":4.5}
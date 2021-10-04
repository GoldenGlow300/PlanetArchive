from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
    path('', views.RecordListView.as_view(), name='record_list'),
    path('add/', views.record_add, name='record_add'),
    path('<slug:planet_name>/', views.record_detail, name='record_detail'),
]
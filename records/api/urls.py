from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
    path('records/', views.RecordListView.as_view(), name='records_list'),
    path('records/add/', views.RecordCreateView.as_view(), name='record_add'),
    path('records/<name>/', views.RecordDetailView.as_view(), name='record_detail'),
    path('records/<name>/update/', views.RecordUpdateView.as_view(), name='record_update'),
    path('records/<name>/delete/', views.RecordDeleteView.as_view(), name='record_delete'),
    
]



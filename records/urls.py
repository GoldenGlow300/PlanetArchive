from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
    path('', views.RecordListView.as_view(), name='record_list'),
    path('add/', views.RecordFormView.as_view(), name='record_add'),
    path('<name>/', views.RecordDetailView.as_view(), name='record_detail'),
    path('<name>/update/', views.RecordUpdateView.as_view(), name='record_update'),
    path('<name>/delete/', views.record_delete, name='record_delete'),

]
from django.urls import path
from .views import (HomeView, AddView, UpdateView, DeleteView)

app_name = 'todo'

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('add/', AddView.as_view(), name = 'add'),
    path('update/', UpdateView.as_view(), name = 'update'),
    path('delete/', DeleteView.as_view(), name = 'delete'),
]
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from .models import TodoModel

class HomeView(TemplateView):
    template_name = 'todo/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Ejecutar el metodo get_context_data del padre
        context['todos'] = TodoModel.objects.all()
        return context
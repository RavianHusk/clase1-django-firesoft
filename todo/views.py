from django.shortcuts import render

# Create your views here.
from django.views import generic

from .models import TodoModel

class HomeView(generic.TemplateView):
    template_name = 'todo/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Ejecutar el metodo get_context_data del padre
        context['todos'] = TodoModel.objects.all()
        return context

class AddView(generic.TemplateView):
    template_name = 'todo/add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Ejecutar el metodo get_context_data del padre
        context['todos'] = TodoModel.objects.all()
        return context

class UpdateView(generic.TemplateView):
    template_name = 'todo/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Ejecutar el metodo get_context_data del padre
        context['todos'] = TodoModel.objects.all()
        return context

class DeleteView(generic.TemplateView):
    template_name = 'todo/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Ejecutar el metodo get_context_data del padre
        context['todos'] = TodoModel.objects.all()
        return context

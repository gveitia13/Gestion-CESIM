from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from core.models import Proyecto


class ProjectCreate(generic.CreateView):
    model = Proyecto
    fields = '__all__'
    template_name = 'form_project.html'
    success_url = reverse_lazy('project-add')

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from core.forms import ProyectoForm
from core.models import Proyecto


class ProjectCreate(generic.CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'project/form_project.html'
    success_url = reverse_lazy('project-list')

    def get_context_data(self, **kwargs):
        context = super(ProjectCreate, self).get_context_data()
        context['title'] = 'Insertar proyecto'
        return context


class ProjectUpdate(generic.UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'project/form_project.html'
    success_url = reverse_lazy('project-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Editar proyecto'
        return context


class ProjectList(LoginRequiredMixin, generic.ListView):
    model = Proyecto
    template_name = 'project/list_card_project.html'
    queryset = Proyecto.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProjectList, self).get_context_data()
        context['title'] = 'Listado de proyectos'
        return context


class ProjectDetails(generic.DetailView):
    model = Proyecto
    template_name = 'project/details_project.html'

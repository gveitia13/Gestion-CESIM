from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, JsonResponse
from django.urls import reverse_lazy
from django.views import generic

from core.forms import ProyectoForm, MemberForm, RecursosHumanosForm
from core.models import Proyecto, Miembro


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


class ProjectList(generic.ListView):
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

    def get_context_data(self, **kwargs):
        context = super(ProjectDetails, self).get_context_data()
        project = self.get_object()
        context['title'] = f'Detalles de {project}'
        context['object_list'] = Miembro.objects.all()
        context['form'] = MemberForm()
        context['form2'] = RecursosHumanosForm()
        print(project)
        return context

    def post(self, request: HttpRequest, *args, **kwargs):
        data = {}
        print(request.POST)
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise ValueError(Exception)
        #
        # try:
        #     member = Miembro.objects.create(request.POST)
        # except Exception as e:
        #     data['error'] = str(e)
        # except Exception as e:
        # data['error'] = 'errpr'
        return JsonResponse(data, safe=False)
        # return redirect(reverse_lazy('denuncia-list'))

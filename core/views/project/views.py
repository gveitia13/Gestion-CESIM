from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render, resolve_url
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from core.forms import ProyectoForm, MemberForm, RecursosHumanosForm
from core.models import Proyecto, Miembro, RecursosHumanos


class ProjectCreate(generic.CreateView):
    model = Proyecto
    form_class = ProyectoForm
    # fields = '__all__'
    template_name = 'project/form_project.html'
    success_url = reverse_lazy('project-list')

    def get_context_data(self, **kwargs):
        context = super(ProjectCreate, self).get_context_data()
        context['title'] = 'Insertar proyecto'
        context['all_projects'] = Proyecto.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)
        print(request.FILES)
        return super().post(request, *args, **kwargs)


class ProjectUpdate(generic.UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'project/form_project.html'
    success_url = reverse_lazy('project-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Editar proyecto'
        context['all_projects'] = Proyecto.objects.all()
        return context


class ProjectList(generic.ListView):
    model = Proyecto
    template_name = 'project/list_card_project.html'
    queryset = Proyecto.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProjectList, self).get_context_data()
        context['title'] = 'Listado de proyectos'
        context['all_projects'] = Proyecto.objects.all()
        return context

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args: list, **kwargs: dict):
        data = {}
        print(request.POST)
        try:
            action = request.POST['action']
            if action == 'delete':
                project = Proyecto.objects.get(pk=request.POST.get('pk'))
                project.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
            return JsonResponse(data, safe=False)
        return JsonResponse(data, safe=False)


class ProjectDetails(generic.DetailView):
    model = Proyecto
    template_name = 'project/details_project.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetails, self).get_context_data()
        project = self.get_object()
        context['title'] = f'Detalles de {project}'
        object_list = []
        for i in Miembro.objects.filter(proyecto=self.get_object()):
            item = i.toJSON()
            item['rrhh'] = RecursosHumanos.objects.filter(miembro_id=i.pk, proyecto_id=project.pk)[0].toJSON()
            object_list.append(item)
        context['object_list'] = object_list
        context['form'] = MemberForm()
        context['form2'] = RecursosHumanosForm()
        context['all_projects'] = Proyecto.objects.all()
        print(project)
        return context

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args, **kwargs):
        data = {}
        print(request.POST)
        try:
            action = request.POST['action']
            if action == 'create':
                with transaction.atomic():
                    member = Miembro()
                    member.nombre = request.POST.get('nombre')
                    member.apellidos = request.POST.get('apellidos')
                    member.ci = request.POST.get('ci')
                    member.categoria_ocupacional = request.POST.get('categoria_ocupacional')
                    member.categoria_cientifica = request.POST.get('categoria_cientifica')
                    member.cuenta_bancaria = request.POST.get('cuenta_bancaria')
                    member.save()

                    project = self.get_object()

                    rrhh = RecursosHumanos()
                    rrhh.miembro_id = member.pk
                    rrhh.proyecto_id = project.pk
                    rrhh.cargo = request.POST.get('cargo')
                    rrhh.institucion = request.POST.get('institucion')
                    rrhh.clasificador_entidad = request.POST.get('clasificador_entidad')
                    rrhh.porciento_de_participacion = request.POST.get('porciento_de_participacion')
                    rrhh.porciento_de_remuneracion = request.POST.get('porciento_de_remuneracion')
                    rrhh.tiempo = request.POST.get('tiempo')
                    rrhh.salario_mensual_basico = request.POST.get('salario_mensual_basico')
                    rrhh.salario_mensual = float(request.POST.get('salario_mensual_basico')) * float(
                        request.POST.get('porciento_de_participacion')) / 100
                    rrhh.mce = float(request.POST.get('salario_mensual_basico')) * float(
                        request.POST.get('porciento_de_remuneracion')) / 100
                    rrhh.anual = float(request.POST.get('salario_mensual_basico')) * float(
                        request.POST.get('porciento_de_remuneracion')) / 100 * float(request.POST.get('tiempo'))
                    rrhh.save()
                data['success'] = 'Se creo bien'
            elif action == 'edit':
                with transaction.atomic():
                    project = self.get_object()

                    member = Miembro.objects.get(pk=request.POST.get('pk'))
                    member.nombre = request.POST.get('nombre')
                    member.apellidos = request.POST.get('apellidos')
                    member.ci = request.POST.get('ci')
                    member.categoria_ocupacional = request.POST.get('categoria_ocupacional')
                    member.categoria_cientifica = request.POST.get('categoria_cientifica')
                    member.cuenta_bancaria = request.POST.get('cuenta_bancaria')
                    member.save()

                    rrhh = RecursosHumanos.objects.get(miembro_id=member.pk, proyecto_id=project.pk)
                    rrhh.cargo = request.POST.get('cargo')
                    rrhh.institucion = request.POST.get('institucion')
                    rrhh.clasificador_entidad = request.POST.get('clasificador_entidad')
                    rrhh.porciento_de_participacion = request.POST.get('porciento_de_participacion')
                    rrhh.porciento_de_remuneracion = request.POST.get('porciento_de_remuneracion')
                    rrhh.tiempo = request.POST.get('tiempo')
                    rrhh.salario_mensual_basico = request.POST.get('salario_mensual_basico')
                    rrhh.salario_mensual = float(request.POST.get('salario_mensual_basico')) * float(
                        request.POST.get('porciento_de_participacion')) / 100
                    rrhh.mce = float(request.POST.get('salario_mensual_basico')) * float(
                        request.POST.get('porciento_de_remuneracion')) / 100
                    rrhh.anual = float(request.POST.get('salario_mensual_basico')) * float(
                        request.POST.get('porciento_de_remuneracion')) / 100 * float(request.POST.get('tiempo'))
                    rrhh.save()
            elif action == 'search_member':
                print('entro')
                project = self.get_object()
                member = Miembro.objects.get(pk=request.POST.get('pk'))
                rrhh = RecursosHumanos.objects.get(miembro_id=member.pk, proyecto_id=project.pk)
                data = member.toJSON()
                data.update(rrhh.toJSON())
            elif action == 'del-project':
                project = Proyecto.objects.get(pk=request.POST.get('pk'))
                project.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
            return JsonResponse(data, safe=False)
        # return redirect(reverse_lazy('project-details', kwargs={'pk': project.pk}))
        return JsonResponse(data, safe=False)

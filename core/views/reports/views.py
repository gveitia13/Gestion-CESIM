from django.views import generic

from core.models import Proyecto, Miembro, RecursosHumanos


class ProjectSalario(generic.DetailView):
    model = Proyecto
    template_name = 'reports/project_salario.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectSalario, self).get_context_data()
        project = self.get_object()
        context['title'] = f'Estadísticas del proyecto {project}'
        object_list = []
        for i in Miembro.objects.filter(proyecto=self.get_object()):
            item = i.toJSON()
            item['rrhh'] = RecursosHumanos.objects.filter(miembro_id=i.pk, proyecto_id=project.pk)[0].toJSON()
            object_list.append(item)
        context['object_list'] = object_list
        context['all_projects'] = Proyecto.objects.all()
        total, salario_anual_externo, salario_anual_ejecutora = 0.0, 0.0, 0.0
        for i in object_list:
            total += float(i['rrhh']['anual'])
            salario_anual_externo += float(i['rrhh']['salario_anual_externo'])
            salario_anual_ejecutora += float(i['rrhh']['salario_anual_ejecutora'])
        context['total_anual'] = total
        context['total_salario_anual_externo'] = salario_anual_externo
        context['total_salario_anual_ejecutora'] = salario_anual_ejecutora
        return context

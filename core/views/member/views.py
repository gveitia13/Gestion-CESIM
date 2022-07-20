from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from core.forms import MemberForm
from core.models import Miembro, Proyecto


class MemberCreate(generic.CreateView):
    model = Miembro
    template_name = 'member/form_basic_member.html'
    success_url = reverse_lazy('member-list')
    form_class = MemberForm

    def get_context_data(self, **kwargs):
        context = super(MemberCreate, self).get_context_data()
        context['title'] = 'Registrar nuevo miembro'
        context['all_projects'] = Proyecto.objects.all()
        return context


class MemberUpdate(generic.UpdateView):
    model = Miembro
    template_name = 'member/form_basic_member.html'
    success_url = reverse_lazy('member-list')
    form_class = MemberForm

    def get_context_data(self, **kwargs):
        context = super(MemberUpdate, self).get_context_data()
        context['title'] = 'Actualizar un miembro'
        context['all_projects'] = Proyecto.objects.all()
        return context


class MemberList(generic.ListView):
    model = Miembro
    template_name = 'member/list_member.html'
    queryset = Miembro.objects.all()

    def get_queryset(self):
        qs = super(MemberList, self).get_queryset()
        qs = [i.toJSON() for i in qs]
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MemberList, self).get_context_data()
        context['title'] = 'Listado de miembros'
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
                member = Miembro.objects.get(pk=request.POST.get('pk'))
                member.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
            return JsonResponse(data, safe=False)
        return JsonResponse(data, safe=False)

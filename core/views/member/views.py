from django.urls import reverse_lazy
from django.views import generic

from core.forms import MemberForm
from core.models import Miembro


class MemberCreate(generic.CreateView):
    model = Miembro
    template_name = 'member/form_basic_member.html'
    success_url = reverse_lazy('member-list')
    form_class = MemberForm

    def get_context_data(self, **kwargs):
        context = super(MemberCreate, self).get_context_data()
        context['title'] = 'Registrar nuevo miembro'
        return context


class MemberUpdate(generic.UpdateView):
    model = Miembro
    template_name = 'member/form_basic_member.html'
    success_url = reverse_lazy('member-list')
    form_class = MemberForm

    def get_context_data(self, **kwargs):
        context = super(MemberUpdate, self).get_context_data()
        context['title'] = 'Actualizar un miembro'
        return context


class MemberList(generic.ListView):
    model = Miembro
    template_name = 'member/list_member.html'
    queryset = Miembro.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MemberList, self).get_context_data()
        context['title'] = 'Listado de miembros'
        return context

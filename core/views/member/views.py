from django.urls import reverse_lazy
from django.views import generic

from core.models import Miembro


class MemberCreate(generic.CreateView):
    model = Miembro
    template_name = 'member/form_basic_member.html'
    success_url = reverse_lazy('member-list')


class MemberList(generic.ListView):
    model = Miembro
    template_name = 'member/list_member.html'
    queryset = Miembro.objects.all()

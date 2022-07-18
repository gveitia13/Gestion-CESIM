from django.urls import path

from core.views.member.views import *
from core.views.project.views import *

urlpatterns = [
    path('project/list/', ProjectList.as_view(), name='project-list'),
    path('project/create/', ProjectCreate.as_view(), name='project-add'),
    path('project/update/<int:pk>/', ProjectUpdate.as_view(), name='project-update'),
    path('project/details/<int:pk>/', ProjectDetails.as_view(), name='project-details'),

    path('member/list/', MemberList.as_view(), name='member-list'),
    path('member/create/', MemberCreate.as_view(), name='member-create'),
]

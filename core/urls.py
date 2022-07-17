from django.urls import path
from .views import *

urlpatterns = [
    path('project/list/', ProjectList.as_view(), name='project-list'),
    path('project/create/', ProjectCreate.as_view(), name='project-add'),
    path('project/update/<int:pk>/', ProjectUpdate.as_view(), name='project-update'),
]

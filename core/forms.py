from django import forms
from django.forms import ModelForm

from core.models import Proyecto


class ProyectoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Proyecto
        fields = '__all__'
        widgets = {
            'resumen': forms.Textarea(
                attrs={
                    'placeholder': '',
                    'rows': 3,
                }
            ),
            'tipo': forms.Select()
        }

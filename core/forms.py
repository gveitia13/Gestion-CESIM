from django import forms
from django.forms import ModelForm

from core.models import Proyecto, Miembro, RecursosHumanos


class ProyectoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['placeholder'] = 'Escriba el nombre completo'
        self.fields['abreviacion'].widget.attrs['placeholder'] = 'Escriba las siglas identificativas'
        self.fields['programa'].widget.attrs['placeholder'] = 'Programa al que pertenece'
        self.fields['resumen'].widget.attrs['placeholder'] = 'Breve descripción o resumen del proyecto'
        self.fields['area'].widget.attrs['placeholder'] = 'Área administrativa a la que pertenece'
        self.fields['codigo'].widget.attrs['placeholder'] = 'Código del proyecto'
        self.fields['tipo'] = forms.ChoiceField(choices=(
            ('', 'Seleccione una opción'),
            ('n', 'Nacional'),
            ('s', 'Sectorial'),
            ('i', 'Institucional'),
        ))

    class Meta:
        model = Proyecto
        fields = '__all__'
        widgets = {
            'resumen': forms.Textarea(
                attrs={
                    'placeholder': '',
                    'rows': 2,
                }
            ),
            'tipo': forms.Select()
        }


class MemberForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['placeholder'] = 'Escriba el/los nombre(s)'
        self.fields['apellidos'].widget.attrs['placeholder'] = 'Escriba los apellidos'
        self.fields['ci'].widget.attrs['placeholder'] = 'Escriba el número del carnet'
        self.fields['categoria_cientifica'].widget.attrs['placeholder'] = 'Categoría científica (opcional)'
        self.fields['cuenta_bancaria'].widget.attrs['placeholder'] = 'Número de cuenta bancaria'
        self.fields['categoria_ocupacional'] = forms.ChoiceField(choices=(
            ('', 'Seleccione una opción'),
            ('', '---------------------------'),
            ('C', 'Cuadro'),
            ('TI', 'Técnico de investigación'),
            ('OT', 'Otros técnicos'),
            ('O', 'Obreros'),
            ('S', 'Servicios'),
        ))
        # self.fields['proyecto'] =

    class Meta:
        model = Miembro
        fields = '__all__'
        exclude = ('proyecto',)


class RecursosHumanosForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cargo'] = forms.ChoiceField(choices=(
            ('', 'Seleccione una opción'),
            ('', '---------------------'),
            ('1', 'Jefe de proyecto'),
            ('2', 'Profesor'),
            ('3', 'Estudiante'),
            ('4', 'Analista'),
            ('5', 'Desarrollador'),
            ('6', 'Gestor'),
        ))
        self.fields['clasificador_entidad'] = forms.ChoiceField(choices=(
            ('', 'Seleccione un número'),
            ('', '-----------------------'),
            ('1', '1'),
            ('0', '0'),
        ), help_text='1 si es Empresa, 0 si es Presupuestada')
        self.fields['institucion'].widget.attrs['placeholder'] = 'Escriba el nombre de la institución'
        self.fields['porciento_de_participacion'].widget.attrs[
            'placeholder'] = 'Escriba el % de participación en el proyecto'
        self.fields['porciento_de_remuneracion'].widget.attrs[
            'placeholder'] = 'Escriba el % de remuneración en el proyecto'
        self.fields['tiempo'].widget.attrs['placeholder'] = 'Escriba el tiempo en meses'
        self.fields['salario_mensual_basico'].widget.attrs['placeholder'] = 'Escriba el salario básico'

    class Meta:
        model = RecursosHumanos
        fields = '__all__'

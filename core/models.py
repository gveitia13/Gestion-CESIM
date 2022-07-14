from django.core.validators import MaxValueValidator
from django.db import models


# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre del proyecto')
    programa = models.CharField(max_length=100, verbose_name='Programa')
    codigo = models.CharField(max_length=100, verbose_name='Código del proyecto')
    tipo = models.CharField(max_length=100, verbose_name='Tipo de proyecto', choices=(
        ('n', 'Nacional'),
        ('s', 'Sectorial'),
        ('i', 'Institucional'),
    ))
    area = models.CharField(max_length=100, verbose_name='Área administrativa')
    resumen = models.CharField(max_length=500, verbose_name='Resumen del proyecto')


class Miembro(models.Model):
    proyecto = models.ManyToManyField(Proyecto, verbose_name='Proyecto asociado', through='RecursosHumanos')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellidos = models.CharField(max_length=100, verbose_name='Apellidos')
    ci = models.CharField(max_length=11, verbose_name='Carnet de identidad')
    categoria = models.CharField(max_length=100, verbose_name='Categoría científica')
    cuenta_bancaria = models.CharField(max_length=16, verbose_name='Cuenta bancaria')
    clasificador_entidad = models.CharField(verbose_name='Clasificar de entidad', max_length=10, )


class RecursosHumanos(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=10, verbose_name='Cargo que ocupa', choices=(
        ('1', 'Jefe de proyecto'),
        ('2', 'Profesor'),
        ('3', 'Estudiante'),
        ('4', 'Analista'),
        ('5', 'Desarrollador'),
        ('6', 'Gestor'),
    ), blank=True, null=True)
    institucion = models.CharField(max_length=100, verbose_name='Institución', choices=(
        ('e', 'Empresa'),
        ('p', 'Presupuestado'),
    ))
    porciento_de_participacion = models.DecimalField(verbose_name='% de Participación', decimal_places=2, max_digits=10)
    salario_mensual = models.DecimalField(verbose_name='Salario mensual', decimal_places=2, max_digits=10, null=True,
                                          blank=True)
    salario_anual = models.DecimalField(verbose_name='Salario anual', decimal_places=2, max_digits=10, null=True,
                                        blank=True)
    salario_externo = models.DecimalField(verbose_name='Salario externo', decimal_places=2, max_digits=10, null=True,
                                          blank=True)
    porciento_de_remuneracion = models.DecimalField(verbose_name='% de Remuneración', decimal_places=2, max_digits=10)
    # calculados
    mce = models.DecimalField(verbose_name='MCE', decimal_places=2, null=True, blank=True, max_digits=10)
    tiempo = models.PositiveSmallIntegerField(verbose_name='Tiempo en meses', validators=[MaxValueValidator(12)])
    # calculados
    anual = models.DecimalField(decimal_places=2, verbose_name='Anual', max_digits=10, null=True, blank=True)
    salario_mensual_basico = models.DecimalField(verbose_name='Salario básico mensual', decimal_places=2,
                                                 max_digits=10, )

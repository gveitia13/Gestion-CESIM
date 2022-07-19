from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models

# Create your models here.
from cesim_gestion.settings import MEDIA_URL, STATIC_URL


class Proyecto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre del proyecto')
    abreviacion = models.CharField(max_length=100, verbose_name='Abreviación del nombre')
    logo = models.ImageField(upload_to='fotos/', null=True, blank=True, verbose_name='Logo del proyecto')
    programa = models.CharField(max_length=100, verbose_name='Programa')
    codigo = models.CharField(max_length=100, verbose_name='Código del proyecto')
    tipo = models.CharField(max_length=100, verbose_name='Tipo de proyecto', choices=(
        ('n', 'Nacional'),
        ('s', 'Sectorial'),
        ('i', 'Institucional'),
    ))
    area = models.CharField(max_length=100, verbose_name='Área administrativa')
    resumen = models.CharField(max_length=500, verbose_name='Resumen del proyecto')

    def __str__(self):
        return self.abreviacion

    def get_logo(self):
        if self.logo:
            return '{}{}'.format(MEDIA_URL, self.logo)
        return '{}{}'.format(STATIC_URL, 'img/uci.jpg')


class Miembro(models.Model):
    proyecto = models.ManyToManyField(Proyecto, verbose_name='Proyecto asociado', through='RecursosHumanos', )
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellidos = models.CharField(max_length=100, verbose_name='Apellidos')
    ci = models.CharField(max_length=11, verbose_name='Carnet de identidad', validators=[MinLengthValidator(11)])
    categoria_ocupacional = models.CharField(max_length=100, verbose_name='Categoría ocupacional', choices=(
        ('C', 'cuadro'),
        ('TI', 'técnico de investigación'),
        ('OT', 'otros técnicos'),
        ('O', 'obreros'),
        ('S', 'servicios'),
    ))
    categoria_cientifica = models.CharField(max_length=100, verbose_name='Categoría científica', null=True, blank=True)
    cuenta_bancaria = models.CharField(max_length=16, verbose_name='Cuenta bancaria')

    def __str__(self):
        return self.nombre


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
    institucion = models.CharField(max_length=100, verbose_name='Institución a que pertenece')
    clasificador_entidad = models.CharField(verbose_name='Clasificar de entidad', max_length=10, choices=(
        ('1', '1'),
        ('0', '0'),
    ), help_text='1 si es Empresa, 0 si es Presupuestada')
    #  Salario por Participación en el Proyecto
    porciento_de_participacion = models.DecimalField(verbose_name='Porciento de Participación', decimal_places=2,
                                                     max_digits=10,
                                                     validators=[MaxValueValidator(100)],
                                                     help_text='Debe ser menor que 100')
    salario_mensual = models.DecimalField(verbose_name='Salario mensual', decimal_places=2, max_digits=10, null=True,
                                          blank=True)  # Salario basico mensual x porciento de participacion
    salario_anual_ejecutora = models.DecimalField(verbose_name='Salario Anual Ejecutora Principal', decimal_places=2,
                                                  max_digits=10, null=True, blank=True)  # Calcular
    salario_anual_externo = models.DecimalField(verbose_name='Salario anual externo', decimal_places=2, max_digits=10,
                                                null=True, blank=True)  # Calcular
    # Remuneración por Participación en el Proyecto
    porciento_de_remuneracion = models.DecimalField(verbose_name='Porciento de Remuneración', decimal_places=2,
                                                    max_digits=10, validators=[MaxValueValidator(100)],
                                                    help_text='Debe ser menor que 100')
    mce = models.DecimalField(verbose_name='MCE', decimal_places=2, null=True, blank=True, max_digits=10)  # calculados
    tiempo = models.PositiveSmallIntegerField(verbose_name='Tiempo en meses', validators=[MaxValueValidator(12)],
                                              help_text='Debe ser menor que 12')
    anual = models.DecimalField(decimal_places=2, verbose_name='Anual', max_digits=10, null=True,
                                blank=True)  # MCE * tiempo
    salario_mensual_basico = models.DecimalField(verbose_name='Salario básico mensual', decimal_places=2,
                                                 max_digits=10, )

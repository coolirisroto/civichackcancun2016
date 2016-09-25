from django.db import models


class Funcionario(models.Model):
    nombre = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=200)
    apellido_materno = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    # picture = models.ImageField(upload_to='funcionarios/fotos', help_text='Max 200px X 200px', null=True, blank=True)
    institution = models.ForeignKey('Institucion')
    tags = models.ManyToManyField('Tag')
    telefono = models.CharField(max_length=200, null=True, blank=True)
    extension = models.CharField(max_length=10, null=True, blank=True)
    id_puesto = models.CharField(max_length=200, null=True, blank=True)
    unidad = models.CharField(max_length=200, null=True, blank=True)
    nombre_superior = models.CharField(max_length=200, null=True, blank=True)
    sueldo_base = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    compensacion_garantizada = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    total_bruto = models.DecimalField(decimal_places=2, null=True, max_digits=20, blank=True)
    total_neto = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    currency = models.CharField(max_length=3, default='MXN', null=True, blank=True)
    seguro_institucional = models.CharField(max_length=200, null=True, blank=True)
    seguro_colectivo_retiro = models.CharField(max_length=200, null=True, blank=True)
    seguro_gastos_medicos = models.CharField(max_length=200, null=True, blank=True)
    seguro_separacion_individualizado = models.CharField(max_length=200, null=True, blank=True)
    prima_vacacional = models.CharField(max_length=200, null=True, blank=True)
    prima_antiguedad = models.CharField(max_length=200, null=True, blank=True)
    gratificacion_fin_ano = models.CharField(max_length=200, null=True, blank=True)
    pagas_defuncion = models.CharField(max_length=200, null=True, blank=True)
    ayuda_despensa = models.CharField(max_length=200, null=True, blank=True)
    vacaciones = models.CharField(max_length=200, null=True, blank=True)
    ISSSTE = models.CharField(max_length=200, null=True, blank=True)
    FOVISSSTE = models.CharField(max_length=200, null=True, blank=True)
    SAR = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return ' '.join([self.nombre, self.apellido_materno, self.apellido_paterno])

class Institucion(models.Model):
    nombre = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)


class Tag(models.Model):
    nombre = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)













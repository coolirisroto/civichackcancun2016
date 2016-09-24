from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin



class FuncionarioResource(resources.ModelResource):

    class Meta:
        model = Funcionario
        fields = ('id', 'nombre', 'apellido_paterno', 'apellido_materno'
        	,'email','institution','telefono','extension','id_puesto',
        	'nombre_superior','sueldo_base','compensacion_garantizada',
        	'total_bruto','total_neto','currency','seguro_institucional',
        	'seguro_colectivo_retiro','seguro_gastos_medicos',
        	'seguro_separacion_individualizado','prima_vacacional',
        	'prima_antiguedad','gratificacion_fin_ano','pagas_defuncion',
        	'ayuda_despensa','vacaciones','ISSSTE','FOVISSSTE','SAR')
        #export_order = ('section', 'title')

class FuncionarioAdmin(ImportExportModelAdmin):
	resource_class = FuncionarioResource
	#list_display = ['title', 'section', 'get_grandstand']
    #list_filter = ['section', 'section__grandstand']


admin.site.register(Institucion)

admin.site.register(Funcionario, FuncionarioAdmin)
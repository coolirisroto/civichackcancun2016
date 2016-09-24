from rest_framework import serializers
from .models import Funcionario


class FuncionarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Funcionario
        fields = ['id', 'nombre', 'apellido_materno', 'apellido_paterno', 'email', 'institution', 'tags',
                  'telefono', 'extension', 'id_puesto', 'unidad', 'nombre_superior', 'sueldo_base',
                  'compensacion_garantizada', 'total_bruto', 'total_neto', 'currency', 'seguro_institucional',
                  'seguro_colectivo_retiro', 'seguro_gastos_medicos', 'seguro_separacion_individualizado',
                  'prima_vacacional', 'prima_antiguedad', 'gratificacion_fin_ano', 'pagas_defuncion',
                  'ayuda_despensa', 'vacaciones', 'ISSSTE', 'FOVISSSTE', 'SAR',
                  ]

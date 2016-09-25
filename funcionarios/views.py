from rest_framework import viewsets, mixins
from .serializers import FuncionarioSerializer
from .models import Funcionario


class FuncionarioViewSet(viewsets.ModelViewSet):
    serializer_class = FuncionarioSerializer
    queryset = Funcionario.objects.none()
    permission_classes = []

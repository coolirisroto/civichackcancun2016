from .views import FuncionarioViewSet
from django.conf.urls import url, include
from rest_framework_bulk.routes import BulkRouter

router = BulkRouter()
router.register(r'funcionarios', FuncionarioViewSet, base_name='funcionarios')

urlpatterns = [
    url(r'^', include(router.urls)),
]

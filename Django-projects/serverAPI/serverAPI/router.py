from dprocess.viewsets import AnalisisViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Analisis', AnalisisViewset)
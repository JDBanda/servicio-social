from rest_framework import viewsets
from django.http import HttpResponse
from . import models
from . import serializers
from .deteccion.deteccion import Detect

class AnalisisViewset(viewsets.ModelViewSet):
    queryset = models.Analisis.objects.all()
    serializer_class = serializers.AnalisisSerializers

    def post(self, request, *args, **kwargs):
        titulo = request.data['titulo']
        imagenOriginal = request.data['imagenOriginal']
        Analisis.objects.create(titulo=titulo, imagenOriginal=imagenOriginal)
        return HttpResponse({'message':'Imagen procesada'}, status=200)
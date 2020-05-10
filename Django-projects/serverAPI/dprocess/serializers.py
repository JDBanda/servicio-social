from rest_framework import serializers
from . models import Analisis
from . models import Conversion

class AnalisisSerializers(serializers.ModelSerializer):
    class Meta:
        model = Analisis
        fields = '__all__'

class ConversionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Conversion
        fields = ['imagenProcesada', 't']
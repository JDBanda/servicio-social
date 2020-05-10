from django.db import models

def upload_path(instance, filename):
    return '/'.join(['imagenes', str(instance.titulo), filename])

# Create your models here.
class Analisis(models.Model):
    titulo = models.CharField(max_length=32, blank=False)
    imagenOriginal = models.ImageField(blank=True, null=True, upload_to=upload_path)

class Conversion(models.Model):
    imagenProcesada = models.ImageField(blank=True, upload_to=upload_path, null=True)

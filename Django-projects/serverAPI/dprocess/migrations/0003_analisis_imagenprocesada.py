# Generated by Django 3.0.5 on 2020-04-29 22:08

from django.db import migrations, models
import dprocess.models


class Migration(migrations.Migration):

    dependencies = [
        ('dprocess', '0002_analisis_imagenoriginal'),
    ]

    operations = [
        migrations.AddField(
            model_name='analisis',
            name='imagenProcesada',
            field=models.ImageField(blank=True, null=True, upload_to=dprocess.models.upload_path),
        ),
    ]

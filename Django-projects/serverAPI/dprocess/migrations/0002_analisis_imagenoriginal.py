# Generated by Django 3.0.5 on 2020-04-29 17:27

from django.db import migrations, models
import dprocess.models


class Migration(migrations.Migration):

    dependencies = [
        ('dprocess', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='analisis',
            name='imagenOriginal',
            field=models.ImageField(blank=True, null=True, upload_to=dprocess.models.upload_path),
        ),
    ]

# Generated by Django 2.1.7 on 2019-06-11 16:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('puntosvista', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='puntos',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de publicación'),
            preserve_default=False,
        ),
    ]
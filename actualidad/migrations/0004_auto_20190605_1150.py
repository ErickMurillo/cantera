# Generated by Django 2.1.7 on 2019-06-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actualidad', '0003_auto_20190604_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualidad',
            name='category',
            field=models.CharField(choices=[('noticias', 'Noticias'), ('situacion-regional-genero', 'Situación regional de género'), ('campanas', 'Campañas'), ('concursos', 'Concursos')], max_length=50, verbose_name='Categoría'),
        ),
    ]

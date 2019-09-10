# Generated by Django 2.1.7 on 2019-09-06 16:09

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0002_auto_20190806_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='hora_fin',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora fin'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='position',
            field=location_field.models.plain.PlainLocationField(blank=True, max_length=63, null=True, verbose_name='Posición'),
        ),
    ]
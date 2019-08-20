# Generated by Django 2.1.7 on 2019-08-07 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizaciones', '0002_auto_20190624_1011'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudesNuevasOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_org', models.CharField(max_length=200)),
                ('siglas_org', models.CharField(help_text='Siglas o nombre corto de la oganización', max_length=200, verbose_name='Siglas o nombre corto')),
                ('aprobado', models.BooleanField()),
                ('pais_org', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='organizaciones.Pais')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Solicitud para crear una organización',
                'verbose_name_plural': 'Solicitudes nuevas organizaciones',
            },
        ),
        migrations.CreateModel(
            name='SolicitudesOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aprobado', models.BooleanField()),
                ('organizacion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='organizaciones.Contraparte')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Solicitud para unirse a una organización',
                'verbose_name_plural': 'Solicitudes a organizaciones',
            },
        ),
    ]
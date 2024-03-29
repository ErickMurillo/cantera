# Generated by Django 2.1.7 on 2019-06-21 15:10

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_actualidad', sorl.thumbnail.fields.ImageField(blank=True, help_text='1350x230', null=True, upload_to='configuracion/')),
                ('foto_eventos', sorl.thumbnail.fields.ImageField(blank=True, help_text='1350x230', null=True, upload_to='configuracion/')),
                ('foto_galerias_videos', sorl.thumbnail.fields.ImageField(blank=True, help_text='1350x230', null=True, upload_to='configuracion/')),
                ('foto_galerias_imagenes', sorl.thumbnail.fields.ImageField(blank=True, help_text='1350x230', null=True, upload_to='configuracion/')),
                ('foto_foros', sorl.thumbnail.fields.ImageField(blank=True, help_text='1350x230', null=True, upload_to='configuracion/')),
                ('foto_puntos_vista', sorl.thumbnail.fields.ImageField(blank=True, help_text='1350x230', null=True, upload_to='configuracion/')),
                ('foto_quienes_somos', sorl.thumbnail.fields.ImageField(blank=True, help_text='1350x230', null=True, upload_to='configuracion/')),
                ('foto_guias_metodologicas', sorl.thumbnail.fields.ImageField(blank=True, help_text='1350x230', null=True, upload_to='configuracion/')),
                ('foto_publicaciones', sorl.thumbnail.fields.ImageField(blank=True, help_text='1350x230', null=True, upload_to='configuracion/')),
                ('foto_campanias', sorl.thumbnail.fields.ImageField(blank=True, help_text='1350x230', null=True, upload_to='configuracion/')),
                ('foto_concursos', sorl.thumbnail.fields.ImageField(blank=True, help_text='1350x230', null=True, upload_to='configuracion/')),
                ('foto_alianzas', sorl.thumbnail.fields.ImageField(blank=True, help_text='1350x230', null=True, upload_to='configuracion/')),
            ],
            options={
                'verbose_name_plural': 'Configuracion imagenes del sitio',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_1', models.CharField(max_length=60, verbose_name='Texto')),
                ('foto_1', sorl.thumbnail.fields.ImageField(upload_to='slider/', verbose_name='Foto')),
                ('credito_1', models.CharField(max_length=100, verbose_name='Credito')),
                ('texto_2', models.CharField(blank=True, max_length=60, null=True, verbose_name='Texto')),
                ('foto_2', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='slider/', verbose_name='Foto')),
                ('credito_2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Credito')),
                ('texto_3', models.CharField(blank=True, max_length=60, null=True, verbose_name='Texto')),
                ('foto_3', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='slider/', verbose_name='Foto')),
                ('credito_3', models.CharField(blank=True, max_length=100, null=True, verbose_name='Credito')),
            ],
            options={
                'verbose_name_plural': 'Slider inicio',
            },
        ),
    ]

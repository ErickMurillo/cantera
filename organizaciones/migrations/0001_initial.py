# Generated by Django 2.1.7 on 2019-06-19 17:57

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contraparte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('siglas', models.CharField(blank=True, help_text='Siglas o nombre corto de la oganización', max_length=200, null=True, verbose_name='Siglas o nombre corto')),
                ('logo', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='contrapartes/logos/')),
                ('fundacion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Año de fundación')),
                ('temas', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('generalidades', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('contacto', models.CharField(blank=True, max_length=200, null=True)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefono', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(editable=False, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Alianzas',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('slug', models.SlugField(editable=False, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Países',
            },
        ),
        migrations.CreateModel(
            name='Redes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcion', models.CharField(choices=[('Sitio web', 'Sitio web'), ('Facebook', 'Facebook'), ('Twitter', 'Twitter'), ('Youtube', 'Youtube'), ('Instagram', 'Instagram'), ('Linkedin', 'Linkedin'), ('Flickr', 'Flickr'), ('Pinterest', 'Pinterest'), ('Vimeo', 'Vimeo'), ('Otra', 'Otra')], max_length=25)),
                ('url', models.URLField()),
                ('organizacion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='organizaciones.Contraparte')),
            ],
            options={
                'verbose_name': 'Red',
                'verbose_name_plural': 'Redes',
            },
        ),
        migrations.AddField(
            model_name='contraparte',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='organizaciones.Pais'),
        ),
    ]

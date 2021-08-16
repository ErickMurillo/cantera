# Generated by Django 2.1.7 on 2019-08-06 20:49

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('actualidad', '0004_auto_20190806_1038'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galerias', '0003_auto_20190806_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('portada', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='galerias/', verbose_name='Imagen')),
                ('descripcion', ckeditor_uploader.fields.RichTextUploadingField()),
                ('slug', models.SlugField(editable=False, max_length=200)),
                ('aprobado', models.BooleanField()),
                ('tematica', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='actualidad.Temas')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Galería audios',
                'verbose_name_plural': 'Galerías audios',
            },
        ),
        migrations.CreateModel(
            name='ListAudios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=90)),
                ('archivo', models.FileField(upload_to='audios/')),
                ('audios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galerias.Audios')),
            ],
            options={
                'verbose_name': 'Audio',
                'verbose_name_plural': 'Lista audios',
            },
        ),
        migrations.CreateModel(
            name='ListVideos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=90)),
                ('url', embed_video.fields.EmbedVideoField()),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Lista videos',
            },
        ),
        migrations.RemoveField(
            model_name='galeriavideos',
            name='url',
        ),
        migrations.AddField(
            model_name='listvideos',
            name='videos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galerias.GaleriaVideos'),
        ),
    ]
